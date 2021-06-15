<div style="position: absolute; top: 0px; right: 0px;">
    <img width="200" height="200" src="https://redislabs.com/wp-content/uploads/2020/12/RedisLabs_Illustration_HomepageHero_v4.svg">
</div>
<div style="height: 150px"></div>

# Basic Redis Rate-limiting Demo Python (Django)

Show how the redis works with Python (Django).


## Try it out

<p>
    <a href="https://heroku.com/deploy" target="_blank">
        <img src="https://www.herokucdn.com/deploy/button.svg" alt="Deploy to Heorku" width="200px"/>
    <a>
</p>

<p>
    <a href="https://vercel.com/new/git/external?repository-url=https://github.com/redis-developer/basic-rate-limiting-demo-python/tree/master&env=REDIS_HOST,REDIS_PORT,REDIS_PASSWORD" target="_blank">
        <img src="https://vercel.com/button" alt="Deploy with Vercel" width="200px" height="50px"/>
    </a>
</p>

<p>
    <a href="https://deploy.cloud.run/?dir=google-cloud-run" target="_blank">
        <img src="https://deploy.cloud.run/button.svg" alt="Run on Google Cloud" width="200px"/>
    </a>
    
</p>

## How to run on Google Cloud

###  1. Click "Run on Google Cloud" 
        
Open up the link under "Manage this application at Cloud Console"

![](https://raw.githubusercontent.com/redis-developer/basic-rate-limiting-demo-python/master/image1.jpg?v=2&s=2)


        
### 2. Click “Edit and Deploy New Revision”
        
![](https://raw.githubusercontent.com/redis-developer/basic-rate-limiting-demo-python/master/image2.jpg?v=2&s=2)


### 3. Click “Variables and Secrets” 

Supply Redis Enterprise Cloud Endpoint URL
        
![](https://raw.githubusercontent.com/redis-developer/basic-rate-limiting-demo-python/master/image3.jpg?v=2&s=2)
        
### 4. Enable HTTP/2
        
Ensure that you have Redis Enterprise Cloud DB created under GCP.
        
![](https://raw.githubusercontent.com/redis-developer/basic-rate-limiting-demo-python/master/image_4.jpg?v=2&s=2)

### 5. Allow all the traffic
        
![](https://raw.githubusercontent.com/redis-developer/basic-rate-limiting-demo-python/master/image_5.jpg?v=2&s=2)
        
        
Hence, you should be able to access Rate Limiting app


![](https://raw.githubusercontent.com/redis-developer/basic-rate-limiting-demo-python/master/image_6.pjpg?v=2&s=2)

---

# How it works?

## 1. How the data is stored:
<ol>
    <li>New responses are added key-ip:<pre> SETNX your_ip:PING limit_amount
 Example: SETNX 127.0.0.1:PING 10 </pre><a href="https://redis.io/commands/setnx">
 more information</a> 
 <br> <br>
 </li>
 <li> Set a timeout on key:<pre>EXPIRE your_ip:PING timeout
Example: EXPIRE 127.0.0.1:PING 1000 </pre><a href="https://redis.io/commands/expire">
 more information</a>
 </li>
</ol>
<br/>

## 2. How the data is accessed:
<ol>
    <li>Next responses are get bucket: <pre>GET your_ip:PING
Example: GET 127.0.0.1:PING   
</pre><a href="https://redis.io/commands/get">
more information</a>
<br> <br>
</li>
    <li> Next responses are changed bucket: <pre>DECRBY your_ip:PING amount
Example: DECRBY 127.0.0.1:PING 1</pre>
<a href="https://redis.io/commands/decrby">
more information</a>  </li>
</ol>
 
---

## How to run it locally?

```
git clone https://github.com/redis-developer/basic-rate-limiting-demo-python.git
```


### Run docker compose or install redis manually
Install docker (on mac: https://docs.docker.com/docker-for-mac/install/)
```sh
docker network create global
docker-compose up -d --build
```


#### Open directory server (cd server/configuration): copy .env.example to create .env (copy .env.example .env  or cp .env.example .env). And provide the values for environment variables (if needed)
    - DJANGO_DEBUG: Django debug mode
    - ALLOWED_HOSTS: Allowed hosts
    - REDIS_URL: Redis server url
    - REDIS_HOST: Redis server host
    - REDIS_PORT: Redis server port
    - REDIS_DB: Redis server db index
    - REDIS_PASSWORD: Redis server password

#### Run backend

Install python, pip and venv (on mac: https://installpython3.com/mac/)

Use python version: 3.8
``` sh
python3 -m venv venv
source ./venv/bin/activate
pip3 install -r requirements.txt
python3 server/manage.py collectstatic
python3 server/manage.py runserver
```

#### Run frontend

Static сontent runs automatically with the backend part.
