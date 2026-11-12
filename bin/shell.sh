#!/usr/bin/env bash

set -e

cd "$(dirname "$0")/.."

docker compose exec django python manage.py shell