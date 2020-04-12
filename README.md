# Dumpmon for monitoring

Forked from https://github.com/jordan-wright/dumpmon/ 

Modified, to do local monitoring, as well as patches + fixes where I see fit.

```
1. Run Monitor Guide
2. Visualization Guide
3. FAQ, Tips
	What if I want to update the code ?
	I tried doing docker-compose build, but the ./data directory is having a 600 permission for all files
	The Grafana Database mongo is not working.
```

## Monitor Guide:
```
	docker-compose build 	
	docker-compose up	
```

You can now view the data inside of ./data directory

## Visualization Guide:
```
	Hopefully soon ? If we survive Corvid
```

## FAQ, TIPS:

 - Q: What if I want to update the code ?

 	 A: Well someone is feeling energized.
 		
		<update code>
		docker-compose down
		docker-compose build 
		docker-compose up

 - Q: I tried doing docker-compose build, but the ./data directory is having a 600 permission for all files

 		sudo chmod -R 777 ./data

 - Q: The Grafana Database mongo is not working

   A: Check the database source, confirm if the URL matches the DB instance url.

	 	docker exec monitoring_grafana env | grep DB_PORT_27017_TCP_ADDR
