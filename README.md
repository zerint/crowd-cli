# Crowd CLI
CLI application aimed to provide the missing functionalities when it comes to managing Atlassian Crowd's.

## Installation
### Linux
```commandline
git clone <repo>
cd crowd-cli
python3 -m venv venv
venv/bin/pip3 install -r requirements.txt
cp config.yml.example config.yml
# Configure config.yml
venv/bin/python3 crowd.py --help
```
### Windows
```commandline
git clone <repo>/Download zip and extract.
cd crowd-cli
python3 -m venv venv
venv\Scripts\python.exe -m pip install -r requirements.txt
copy config.yml.example config.yml
# Configure config.yml (just type "config.yml" in the cmd)
venv\Scripts\python.exe crowd.py --help
```
As ZIP:
```commandline
curl -L -o crowd-cli.zip <ZIP url>
tar -xf crowd-cli.zip
move crowd-cli-main crowd-cli
cd crowd-cli
```

## Usage
### Linux
```commandline
cd crowd-cli
venv/bin/python3 crowd.py --help
```
### Windows
```commandline
cd crowd-cli
venv\bin\python.exe crowd.py --help
```
