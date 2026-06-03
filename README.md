
# Hugging Face Docker Port

Hugging Face Docker Spaces expect applications to run on **port 7860**.

Before deploying, to use port **7860**, update:
* `app.py` -> app.run( port=7860 )
* `Dockerfile` -> EXPOSE 7860

---

# Docker

## Build Image
sudo docker build -t <image_name> .
```bash
sudo docker build -t iris .
```

## Run Container
sudo docker run -d -p <host_port>:<container_port> --name <container_name> <image_name>
```bash
sudo docker run -d -p 5000:5000 --name iris-container iris
```

## View Running Containers
```bash
docker ps -a
```

## Open Bash Inside Container
```bash
docker exec -it <container_id> bash
docker exec -it <container_name> bash
```

---

# Docker Compose

## Start Services
```bash
sudo docker-compose up -d
```

## Stops containers and removes the internal network.
```bash
sudo docker-compose down
```

## Check Logs
```bash
sudo docker-compose logs -f
```
