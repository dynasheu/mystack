#!/bin/bash

echo "installing required software"
sudo apt update

# curl and git
sudo apt install -y curl

# docker
curl -fsSL https://get.docker.com | sh
sudo apt install -y docker-compose

# fix user permissions
sudo groupadd docker
sudo usermod -aG docker $USER
newgrp docker

# install python, pip and yaml parser
sudo apt install -y python3
sudo apt install -y python3-pip
pip install pyyaml

echo "reboot please"