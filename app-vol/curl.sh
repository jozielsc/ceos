#!/usr/bin/env bash

TOKEN=$(curl -s -X POST -H 'Accept: application/json' -H 'Content-Type: application/json' --data '{"email":"jozielsc@gmail.com","password":"123mudar"}' http://127.0.0.1:5000/api/v1/auth/login | jq -r '.access_token')

curl -X POST -H 'Accept: application/json' -H "Authorization: Bearer ${TOKEN}" -H 'Content-Type: application/json' --data '{"name": "Esse eh um teste"}' http://127.0.0.1:5000/api/v1/bucketlists/
