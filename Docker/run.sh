#!/usr/bin/env bash
docker stop yahoo_service
docker rm yahoo_service
sudo docker run -d  --name yahoo_service  --net=host -p 8000:8000 -e DBHOST='localhost' -e DBPORT=3306 -e DATABASE='traxessag' -e DBUSER='admin' -e DBPASSWORD='Qwerty@123'  service:yahoo

