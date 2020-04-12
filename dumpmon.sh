#!/usr/bin/env bash

sudo chmod -R 777 database/mysql/data
sudo chmod -R 777 web-ui/grafana

case $1 in
	build)
		docker-compose build
		;;
	down)
		docker-compose down
		;;
	start)
		docker-compose up
		;;
	up)
		docker-compose up
		;;
	*)
		echo "Sorry, I don't understand"
		;;
esac
