# Sentiment Analysis App with Luigi Pipelines
Sentiment Analysis App with Luigi Pipelines

## 🖼️ **Screenshot**

![](https://paper-attachments.dropbox.com/s_2EAB53F891FDAF5B66CFA57800D2345F9C33E58D86F3B19A9CD5BBB46B2FE1D4_1607737280082_luigi-dashboard.png)
![](https://paper-attachments.dropbox.com/s_2EAB53F891FDAF5B66CFA57800D2345F9C33E58D86F3B19A9CD5BBB46B2FE1D4_1607737276571_luigi-depgraph.png)
![](https://paper-attachments.dropbox.com/s_2EAB53F891FDAF5B66CFA57800D2345F9C33E58D86F3B19A9CD5BBB46B2FE1D4_1607737267427_openapi-docs.png)
![](https://paper-attachments.dropbox.com/s_2EAB53F891FDAF5B66CFA57800D2345F9C33E58D86F3B19A9CD5BBB46B2FE1D4_1607737251482_api.png)


## ❓ **How To Use**

### Install Dependencies

this app uses poetry, so u need to install it first. after that u can install the dependencies with command

    $ poetry install


### Run Application

to run this app u need to add this app folder into PYTHONPATH. here some references https://bic-berkeley.github.io/psych-214-fall-2016/using_pythonpath.html

then u can run this app using existing makefile or run it manualy.

**Run Luigi**
with makefile

    make run-luigi

without makefile

    poetry run luigid --logdir ./logs

**Run Pipeline**
with makefile

    make run-pipeline

without makefile

    poetry run python ./app/run_pipeline.py Entrypoint

**Run API**
with makefile

    make run

without makefile

    poetry run uvicorn app.main:app --reload

## 📔 **To Do**

[ ] Add Dockerfile & Docker Compose File
[ ] Create Frontend
[ ] Add Unittest
[ ] Add Doctest

