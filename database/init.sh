#!/bin/bash
set -e
export PGPASSWORD=postgres;
psql -v ON_ERROR_STOP=1 --username "postgres" --dbname "postgres" <<-EOSQL
  CREATE SCHEMA IF NOT EXISTS lesson;
  CREATE SCHEMA IF NOT EXISTS correction;
EOSQL
