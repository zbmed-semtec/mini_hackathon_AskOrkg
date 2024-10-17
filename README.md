# Mini Hackathon AskORKG
A repository for testing different technologies related to information retrieval inspired in the AskORKG project.

# Instructions

You need the latest version of docker and docker-compose to run the project.

To run the project, you need to execute the following steps:

```
docker-compose build
```

```
docker-compose up -d
```

Then enter the container:
```
docker exec -it python-app /bin/bash
```

And finally, run the following command to check if everthing is working:
```
python3 -m main.py
```

To run the backend, you need to execute the following command:
```
python3 -m components/backend.py
```


