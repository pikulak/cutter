FROM postgres:9.6.5

COPY ./create_db.sh /docker-entrypoint-initdb.d/create_db.sh

# we have to chown this file, otherwise Permisson Denied will occur
RUN chown postgres:postgres /docker-entrypoint-initdb.d/create_db.sh