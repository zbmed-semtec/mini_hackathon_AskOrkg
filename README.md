# Mini Hackathon AskORKG
A repository for testing different technologies related to information retrieval inspired in the AskORKG project.

# Instructions

To run the project, you need to have run the following steps:

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

## Text Embeddings Inference installation guide

Install the Python dependencies using the requirements.txt

```bash
pip install -r requirements.txt
```

Make sure you have CUDA and Docker installed locally, then run:

```bash
model=sentence-transformers/msmarco-MiniLM-L-12-v3
volume=$PWD/data

sudo docker run --gpus all -p 8080:80 -v $volume:/data --pull always ghcr.io/huggingface/text-embeddings-inference:1.5 --model-id $model
```

Alternatively you can run it on CPU using:

```bash
model=sentence-transformers/msmarco-MiniLM-L-12-v3 
volume=$PWD/data

sudo docker run -p 8080:80 -v $volume:/data --pull always ghcr.io/huggingface/text-embeddings-inference:1.5 --model-id $model
```
