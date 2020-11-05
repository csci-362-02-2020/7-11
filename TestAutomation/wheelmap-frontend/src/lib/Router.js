const pathToRegexp = require('path-to-regexp');
const queryString = require('query-string');

class Router {
  constructor(routes) {
    this.routes = routes;
    this.compiledRouteCache = new Map();
  }

  match(pathname) {
    for (let i = 0; i < this.routes.length; i++) {
      const route = this.routes[i];
      const compiledRoute = this.getCompiledRoute(route);
      const match = compiledRoute.pattern.exec(pathname);

      if (!match) {
        continue;
      }

      const params = {};

      for (let i = 1; i < match.length; i++) {
        const key = compiledRoute.keys[i - 1];
        const value = match[i];

        if (value === undefined) {
          continue;
        }

        params[key.name] = key.repeat ? value.split(key.delimiter) : value;
      }

      return { route, params };
    }

    return null;
  }

  generatePath(name, params = {}) {
    const route = this.getRoute(name, true);

    if (!route) {
      return null;
    }

    const compiledRoute = this.getCompiledRoute(route);
    const path = compiledRoute.generate(params);

    const query = {};

    const keys = Object.keys(params);

    for (let i = 0; i < keys.length; i++) {
      const key = keys[i];

      if (compiledRoute.keyNames.indexOf(key) === -1) {
        query[key] = params[key];
      }
    }

    if (Object.keys(query).length > 0) {
      return `${path}?${queryString.stringify(query)}`;
    }

    return path;
  }

  getParams(route, routeParams) {
    const compiledRoute = this.getCompiledRoute(route);
    const params = {};
    const query = {};

    const keys = Object.keys(routeParams);

    for (let i = 0; i < keys.length; i++) {
      const key = keys[i];

      if (compiledRoute.keyNames.indexOf(key) === -1) {
        query[key] = routeParams[key];
      } else {
        params[key] = routeParams[key];
      }
    }

    return { params, query };
  }

  getRoute(nameOrPath, strict = false) {
    const route = this.routes.find(route => route.name === nameOrPath || route.path === nameOrPath);
    if (strict && !route) {
      console.log(`Could not find route ${nameOrPath} in router configuration`);
      return null;
    }

    return route;
  }

  getCompiledRoute(route) {
    let compiledRoute = this.compiledRouteCache.get(route.path);

    if (!compiledRoute) {
      const keys = [];
      compiledRoute = {
        keys,
        pattern: pathToRegexp(route.path || '', keys),
        keyNames: keys.map(key => key.name),
        generate: pathToRegexp.compile(route.path),
      };

      this.compiledRouteCache.set(route.path, compiledRoute);
    }

    return compiledRoute;
  }
}

module.exports = Router;
