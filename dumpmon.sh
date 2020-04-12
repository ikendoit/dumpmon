#!/usr/bin/env bash

sudo chmod -R 777 database/mysql/data
sudo chmod -R 777 web-ui/grafana

case $1 in
	build)
		docker-compose build "${@:2}"
		;;
	down)
		docker-compose down "${@:2}"
		;;
	purge)
		docker-compose down --rmi all
		;;
	start)
		docker-compose up "${@:2}"
		;;
	up)
		docker-compose up "${@:2}"
		;;
	restart)
		docker-compose restart "${@:2}"
		;;
	*)
		echo "Sorry, I don't understand"
		;;
esac
