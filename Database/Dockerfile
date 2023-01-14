FROM postgres:latest

RUN apt-get update && apt-get install -y software-properties-common postgresql-9.3 postgresql-client-9.3 postgresql-contrib-9.3

USER postgres

COPY create.sql /docker-entrypoint-initdb.d/

ENV POSTGRES_PASSWORD=postgresPW

EXPOSE 5432