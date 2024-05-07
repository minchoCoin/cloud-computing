# cloud-computing
assignments of cloud computing subject

# HW1 - Simple auto-scaling
## requirements
- virtualbox
- python

## demo videos
you can watch the demo video by clicking the picture below

[![Video Label](http://img.youtube.com/vi/QX3QC_KCreQ/0.jpg)](https://youtu.be/QX3QC_KCreQ)
# HW2 - Docker
## requirements
- docker
- node docker image
```
docker pull node
```
## How to run-1
sample_server.js is in the C:\Users\user\Documents\cloud_computing directory
```
docker run -it -p 3000:3000 -v C:\Users\user\Documents\cloud_computing:/src node node /src/sample_server.js
```
## How to run-2
```
docker build --tag=myserver .
```
```
docker run -p 3000:3000 myserver
```
## How to run-3(Traefik)
- Read [Basic Traefik configuration tutorial](https://dev.to/karvounis/basic-traefik-configuration-tutorial-593m)
```
docker pull traefik:v2.6
docker pull tecnativa/docker-socket-proxy:latest
docker pull traefik/whoami:v1.7.1
docker network create traefik_public
docker network create socket_proxy
```
- making compose.yml : [code of compose.yml](https://dev.to/karvounis/basic-traefik-configuration-tutorial-593m#complete-configuration)
- send 2 or more requests
```
curl -H "Host: whoami.karvounis.tutorial" http://localhost/
curl -H "Host: whoami.karvounis.tutorial" http://localhost/
...
```
- then you can find that requests arrive at different host
## demo videos
- simple server with docker and nodejs image

[![Video Label](http://img.youtube.com/vi/Ng98W-G2Pw4/0.jpg)](https://youtu.be/Ng98W-G2Pw4)

- making docker image with Dockerfile

[![Video Label](http://img.youtube.com/vi/NLJF-zoF2Ok/0.jpg)](https://youtu.be/NLJF-zoF2Ok)

- Load Balancer with Traefik

[![Video Label](http://img.youtube.com/vi/ddfVtTJ7wPQ/0.jpg)](https://youtu.be/ddfVtTJ7wPQ)

