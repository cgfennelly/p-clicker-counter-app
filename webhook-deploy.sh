#!/bin/bash

echo "Starting deployment..."

docker build -f Dockerfile.webhook -t webhook-listener-clicker .

docker run -d -p 8076:8076 -v /var/run/docker.sock:/var/run/docker.sock -v /home/ubuntu/code/clicker-counter-app:/app -v /home/ubuntu/.ssh:/root/.ssh:ro --name webhook-listener-clicker webhook-listener-clicker

echo "Deployment finished."mk
