#!/bin/bash
echo "Configuring Git safe directory..."
git config --global --add safe.directory /app

echo "Starting deployment..."

git pull origin master
docker build -t p-clicker-counter-app .

# remove existing container
docker stop p-clicker-counter-app || true
docker rm p-clicker-counter-app || true

# Run updated container
docker run -d -p 8077:8077 -v /home/ubuntu/code/p-clicker-counter-app/app.db:/app/app.db --name p-clicker-counter-app p-clicker-counter-app

echo "Deployment finished."
