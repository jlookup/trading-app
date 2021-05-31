#
# Algo Trading App
# Using FastAPI, Alpaca Markets
#
# Container Image Setup


# latest Ubuntu version
FROM python:3

# Transfer setup files
ADD tradeapp/setup /root/setup

# change rights for the script and execute it
RUN chmod u+x /root/setup/install.sh
RUN /root/setup/install.sh

# Expose a port for the app
EXPOSE 4445
