# Redis rate-limiting example

![alt text](https://github.com/deliveryweb/redis-rate-limiting-python)

## Development

```
git clone https://github.com/RemoteCraftsmen/redis-rate-limiting/
```


### Run docker compose or install redis manually
```sh
docker network create global
docker-compose up -d --build
```


#### If you install redis manually open django-backend/configuration folder and copy `.env.example` to create `.env`. And provide the values for environment variables
    - REDIS_HOST: Redis server host
    - REDIS_PORT: Redis server port
    - REDIS_DB: Redis server db index


#### Setup and run 
``` sh
python3 -m venv venv
source ./venv/bin/activate
pip3 install -r requirements.txt
cd django-backend
python3 manage.py migrate
python3 manage.py collectstatic
python3 manage.py runserver

```

