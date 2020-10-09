#!/usr/bin/env sh

set -o errexit
set -o nounset

echo "Run manage.py migrate"
  python /code/manage.py migrate --noinput
#  echo "Flushing database"
#  python /code/manage.py flush --noinput
#  echo "Importing test data"
#  python /code/manage.py loaddata test_data.json
  echo "Run server"
  exec  python -Wd manage.py runserver 0.0.0.0:9000