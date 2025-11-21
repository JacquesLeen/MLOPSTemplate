# MLOPS Template

This directory contains the necessary code to train a very simple ML model and deploy it through a docker container with FastAPI()

## Usage

### Build Image

```bash
docker build -t <your_image_name> .
```

### Run Image

```bash
docker run <your_container_name> -p 8000:8000 <your_image_name>
```

## Testing
Don't forget to have the container running 

### Client.py


```bash
python client.py
```

### Curl

```bash
curl -v http://localhost:8000/predict/   -H 'Content-Type: application/json'   -d '{"features": [5.1, 3.5, 1.4, 0.2]}'
```