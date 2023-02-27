## Docker
### Build
```bash
docker build -t <image_name> .
```

### Run
```bash
docker run -it --rm -p 8080:8080 <image_name>
```

### Push
```bash
docker push <image_name>
```

### Pull
```bash
docker pull <image_name>
```

### Run from Docker Hub
```bash
docker run -it --rm -p 8080:8080 <image_name>
```