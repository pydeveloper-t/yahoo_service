# Simple REST service for Yahoo finance scraper

The FastAPI based simple REST service with two endpoints for Yahoo parser



## Requirements

- MySQL 
- Docker


## How to install?
- Install Docker (https://docs.docker.com/get-docker/)
- Download folder Docker from this repo
- Build image
```
	../Docker/build
```	
```	

## How to run?

### Edit run.sh
Set 
- the actual credentials for MySQL:  DBHOST, DBPORT, DBBASE, DBUSER, DBPASSWORD 
- set actual ports mapping for running docker (The service listen port 8000 within container)
 

### Run service
```
run.sh  
```

  

