# REST service

## How to build
  docker build -t "rest-svc:0.0.1" .

## How to run
  docker run -e PORT=8080 -p 8080:8080 --name "rest-svc" -d --rm "rest-svc:0.0.1"

## How to use
The service is accessible then at: http://localhost:8080

OpenAPI docs are at: http://localhost:8080/docs
