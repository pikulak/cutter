#!/usr/bin/env bash
set -eo pipefail

BASE_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
COMPOSE_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && cd docker/ && pwd )"

_usage()
{
cat << EOF
### Docker Compose helper for cutter project
### usage: manage.sh COMMAND

PROJECT RELATED COMMANDS:
   clean             Remove everything in docker from cutter project
   clean-up          Remove everything in docker from cutter project, create and start containers
   up                Create and start containers
   up-background     Create and start containers in background
   down              Stop and remove containers, networks, images, and volumes

DOCKER RELATED COMMANDS:
   stop              Stop running containers without removing them. They can be started again with "manage.sh start"
   start             Start existing containers (after they were stopped)
   restart           Restart containers
   rm                Stop all containers and delete them
   ps                List containers
   logs              View combined logs from all containers (use "manage.sh logs -f" to follow output)
   logs CONTAINER    View specified container logs (use "manage.sh logs -f CONTAINER" to follow output)
   shell CONTAINER   Log into a bash session inside a running container
   full-clean        Clean your docker environment (removes all containers and all images)
EOF
}


# cd to dir containing .env file
cd ${COMPOSE_DIR}

case "${1}" in
    'clean')
        echo "Clearing docker environment..."
        docker-compose down
        docker-compose rm -sfv
        ;;

    'clean-up')
        echo "Clearing docker environment..."
        docker-compose down
        docker-compose rm -sfv

        echo "Starting containers in the background..."
        docker-compose up --build -d
        ;;

    'rm')
        echo "Stopping and removing..."
        docker-compose down
        docker-compose rm -sfv
        ;;

    'full-clean')
        echo "Clearing docker environment..."
        if [ "`docker ps -a -q | wc -l`" != "0" ]; then
           docker stop $(docker ps -a -q)
           docker rm -f $(docker ps -a -q)
        fi
        [ "`docker images -q | wc -l`" != "0" ] && docker rmi -f $(docker images -q)
        ;;

    'up-background')
        echo "Starting containers in the background..."
        docker-compose up -d
        ;;

    'up')
        echo "Starting containers..."
        docker-compose up
        ;;

    'down')
        echo "Destroying all containers..."
        docker-compose down
        ;;

    'restart')
        echo "Restarting containers..."
        docker-compose restart ${@:2}
        ;;

    'ps')
        echo "Listing containers..."
        docker-compose ps
        ;;

    'logs')
        echo "Accessing logs..."
        docker-compose logs ${@:2}
        ;;

    'shell')
        DOCKER_SHELL_CONTAINER=$(docker-compose ps | grep ${@:2} | cut -d ' ' -f 1 | head -n 1)
        echo "Logging into container ${DOCKER_SHELL_CONTAINER}..."
        docker exec -it ${DOCKER_SHELL_CONTAINER} bash
        ;;

    *)
        _usage
        exit 0
        ;;
esac