# simple-site-requester
A web app which help in cutting your audio file

### Requirements:
  * docker-compose
  * docker

### Tested on:
  * docker-compose==*1.14.0*
  * docker==*17.06.0-ce*
  
## Using:
  ### Build Docker images
    ./manage.sh build --no-cache
  ### Start whole app
    ./manage.sh up
  ### Start whole app in the background
    ./manage.sh up-background
  ### Look into logs
    ./manage.sh logs -f
  ### Start API only
    ./manage.sh up cutter_api
  ### Start Celery worker only
    ./manage.sh up cutter_celery
  ### Stop whole app
    ./manage.sh down
  ### More
  For more commands type:
   `./manage.sh`
   
 ## API
 Whole API will be available on `http://127.0.0.1:8000`

 
