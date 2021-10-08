# POC Analytics Logs

This is a simple sample Python application intended to run inside a k8s cluster
and generate analytics logs and tracing during its processing in JSON format.

Clone the repository and deploy the application into your k8s cluster by running:

```sh
$ kubectl apply -f app-manifest.yml
```

Monitor the pod logs (updated each 5 minutes):

```sh
$ kubectl logs poc-analytics-logs
```

## Build and install

This Python application is intended to run in a docker container inside a k8s cluster.

1. Generate the docker image with the application.

```sh
$ docker build -t bolzon/poc-analytics-logs:latest .
```

2. Push the image to Docker Hub.

```sh
$ docker login
$ docker push bolzon/poc-analytics-logs:latest
```

3. Deploy the application into your k8s cluster.

```sh
$ kubectl apply -f app-manifest.yml
```

## Run locally

Install the application locally with pipenv and run.

```sh
$ pipenv install
$ pipenv run python src/main.py
```
