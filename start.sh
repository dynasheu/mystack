#!/bin/bash

sudo apt update
sudo apt install docker
sudo apt install -y docker-compose
sudo usermod -aG docker $USER

pip install pyyaml