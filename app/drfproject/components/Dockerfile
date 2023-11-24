FROM postgres:13

RUN echo "CREATE DATABASE api_logs;" >> /docker-entrypoint-initdb.d/01_init.sql

COPY init.sql /docker-entrypoint-initdb.d/01_init.sql

VOLUME /var/lib/postgresql/data

CMD ["postgres"]