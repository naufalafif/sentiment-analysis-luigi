# Sentiment Analysis App with Luigi Pipelines
Sentiment Analysis App with Luigi Pipelines

## 🖼️ **Screenshot**

![](/screenshot/luigi-dashboard.png)
![](/screenshot/luigi-depgraph.png)
![](/screenshot/openapi-docs.png)
![](/screenshot/api.png)


## Routes


#### Sentiment API. Port 80

- / contain link to each api version
- /v1 return version detail information
- /v1/sentiment?text api to check sentiment of string
- /v1/control/control/start-pipeline api to start luigi piple

#### Luigi Web Dashboard. Port 8082


## ❓ **How To Use**


### 1) Docker

-- Docker Compose

    docker-compose up

running using docker-compose will create 3 volumes. dataset, preprocessed_dataset & model.
1) dataset : dir where you place dataset. filename must be dataset.csv
2) preprocessed_dataset : dir where you can access preprocessed version of dataset
3) model : dir where you can access created model using pickle
you can replace dataset.csv file, if u want to build using different dataset.

### 2) Manual

#### Install Dependencies

this app uses poetry, so u need to install it first. after that u can install the dependencies with command

    $ poetry install


#### Run Application

to run this app u need to add this app folder into PYTHONPATH. here some references https://bic-berkeley.github.io/psych-214-fall-2016/using_pythonpath.html

then u can run this app using existing makefile or run it manualy.

-- Run Luigi

with makefile

    make run-luigi

without makefile

    poetry run luigid --logdir ./logs

-- Run Pipeline

with makefile

    make run-pipeline

without makefile

    poetry run python ./app/run_pipeline.py Entrypoint

-- Run API

with makefile

    make run

without makefile

    poetry run uvicorn app.main:app --reload

## 📔 **To Do**

- [x] Add Dockerfile & Docker Compose File
- [ ] Create Frontend
- [ ] Add Unittest
- [ ] Add Doctest

