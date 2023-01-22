# mystack
server docker stack

install git using:  
`sudo apt install git`  
and download the script:  
`git clone https://github.com/dynasheu/mystack.git ~/mystack`  

change default passwords in `.env` file

*I am still learning. Not everything is correct yet* :smile:

## included services (exposed ports)
- heimdall (8880, 8843)
- portainer-ce (9000)
- portainer-agent (9001)
- mosquitto (1883, 9002)
- zigbee2mqtt (8080)
- influxdb (8086)
- grafana (3000)
- traefik (80, 8080)
- pihole (53, 9080)
- node-red (1880)

### to be decided services
- chronograf
- kapacitor
- telegraf
- wireguard
- prometheus (9090)
- mariadb