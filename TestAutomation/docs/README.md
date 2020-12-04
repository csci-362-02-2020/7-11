## Installation Instructions

ASSUMING FRESH Ubuntu 18 install, run the following from the terminal:

```
sudo apt update
sudo apt install curl 
sudo apt install git 

# making sure `node -v` is > version 10 for wheelmap to run
sudo apt purge nodejs
curl -sL https://deb.nodesource.com/setup_10.x
sudo -E bash -
sudo apt-get install -y nodejs

# getting the driver set packages set up
sudo apt-get install python3-pip python-dev
pip3 install selenium
wget https://github.com/mozilla/geckodriver/releases/download/v0.27.0/geckodriver-v0.27.0-linux64.tar.gz
tar -xvzf geckodriver* 
chmod +x geckodriver
sudo mv geckodriver /usr/local/bin/

# running the server 
git clone https://github.com/csci-362-02-2020/7-11
cd wheelmap-frontend
cp .env.example .env
npm install 
sudo apt install transifex
npm run dev

# running the testing framework 
cd 7-11/TestAutomation
./scripts/runAllTests.sh
```
