FROM nodered/node-red:latest
USER root
RUN apk update && apk add --no-cache eudev-dev
USER node-red

RUN cd /usr/src/node-red && npm install --save  node-red-configurable-ping
RUN cd /usr/src/node-red && npm install --save  node-red-contrib-boolean-logic
RUN cd /usr/src/node-red && npm install --save  node-red-contrib-influxdb
RUN cd /usr/src/node-red && npm install --save  node-red-dashboard
RUN cd /usr/src/node-red && npm install --save  node-red-node-rbe
RUN cd /usr/src/node-red && npm install --save  node-red-contrib-config
RUN cd /usr/src/node-red && npm install --save  node-red-contrib-diode
RUN cd /usr/src/node-red && npm install --save  node-red-contrib-home-assistant-websocket
RUN cd /usr/src/node-red && npm install --save  node-red-node-openweathermap
RUN cd /usr/src/node-red && npm install --save  node-red-node-email
RUN cd /usr/src/node-red && npm install --save  node-red-node-google
RUN cd /usr/src/node-red && npm install --save  node-red-node-random
RUN cd /usr/src/node-red && npm install --save  node-red-node-smooth
RUN cd /usr/src/node-red && npm install --save  node-red-node-darksky
RUN cd /usr/src/node-red && npm install --save  node-red-contrib-sunevents
RUN cd /usr/src/node-red && npm install --save  node-red-contrib-timeout
RUN cd /usr/src/node-red && npm install --save  node-red-contrib-moment
RUN cd /usr/src/node-red && npm install --save  node-red-contrib-telegrambot
RUN cd /usr/src/node-red && npm install --save  node-red-contrib-discord-advanced
RUN cd /usr/src/node-red && npm install --save  node-red-contrib-isonline
RUN cd /usr/src/node-red && npm install --save  node-red-contrib-zigbee2mqtt
