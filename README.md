# POC JSON logs on k8s 🐋

This is a simple sample Python application intended to run inside a k8s cluster
and generate JSON logs and tracing during its processing.

Deploy the application into your k8s cluster by running:

```sh
$ kubectl apply -f app-manifest.yml
```

Monitor the pod logs (updated each 5 minutes):

```sh
$ kubectl logs poc-analytics-logs
```

## Build, install and run

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

## `NieLogger` class with samples

To achieve JSON logs in Python I've used [python-json-logger](https://github.com/madzak/python-json-logger/) with some few customizations: parent classes `JsonFormatter` and `Logger` were slightly customized in which 2 new dedicated methods have emerged to differentiate each usage: one for analytics and other for application tracing.

Logger creation is pretty similar to the native `logging.getLogger(__name__)`:

```python
import logger

log = logger.get_logger(__name__)
```

Usage was separated into 2 methods:

1) `log.analytics` to register analytics payloads (identified by _log_type = "analytics"_ in the logs).
2) `log.trace` to register application tracing (identified by _log_type = "app"_ in the logs).

```python
log.analytics({
    'my_custom_param': 123,
    'metadata': {
        'name': 'foo',
        'description': 'bar'
    }
})
```

```python
log.trace('Now app will sum 2 nums') # only message
a = 1 + 2

try:
    a = b + c
except Exception as ex:
    log.trace('Error summing', ex) # message + ex

    # will generate a detailed stack:
    #
    #    Traceback (most recent call last):
    #    a = b + c
    #    NameError: name 'b' is not defined
```
