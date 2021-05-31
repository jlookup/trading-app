#!/bin/bash
#
# Startup for new container
# Script to Install
# Linux System Tools and Basic Python Components
#
# Python for Algorithmic Trading
# (c) Dr. Yves J. Hilpisch
# The Python Quants GmbH


# GENERAL LINUX
apt-get update # updates the package index cache
apt-get upgrade -y # updates packages

# install system tools
apt-get install -y build-essential git # system tools
apt-get install -y screen htop vim wget # system tools
apt-get upgrade -y bash # upgrades bash if necessary
apt-get clean # cleans up the package index cache

# COPYING FILES AND CREATING DIRECTORIES
mkdir -p /root/.jupyter/custom
# persistent storage
mkdir -p /root/tradeapp

# for Jupyter Notebooks
# mv /root/setup/tradeapp-ssl-cert.pem /root/.jupyter
# mv /root/setup/tradeapp-ssl-key.key  /root/.jupyter


# INSTALLING PYTHON LIBRARIES
pip install --upgrade pip
pip install -r /root/setup/requirements.txt

# Launch FastAPI web app using uvicorn
