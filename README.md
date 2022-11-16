# PIS - Personal Information System
[![codecov](https://codecov.io/github/IsHaltEchtSo/pis_data_server/branch/main/graph/badge.svg?token=99zm6caCg0)](https://codecov.io/github/IsHaltEchtSo/pis_data_server)  
*This product aims at improving the workflow for storing and displaying information to ultimately aid in building new frameworks*

[**What**](#the-zettelkasten-method) |
[**Why**](#the-zettelkasten-hybrid) |
[**How**](#pis-and-zk) |
[**Setup**](#setup) 

## The Zettelkasten Method

[The Zettelkasten Method](https://zettelkasten.de/posts/overview/) is a framework to build your own knowledge management system with pen and paper. Every idea or thought is saved on a single piece of paper and then put into a container for storage. Over time, your (already linked) zettels accumulate and wait for you to build something nice!

## The Zettelkasten Hybrid

While working analoguely gives you huge benefits in terms of creativity, freedom, heightened concentration and a desired degree of difficulty, it lacks a proper form of management which is where the PIS (and soon the ZK) come into play: with as little overhead as possible, they improve the management and displayability of the zettels by using the least amount of technology possible.

## PIS and ZK 

The PIS and ZK roughly translate to a backend/frontend relationship: while the PIS is concerned with storing the zettel on a server and making them easy to retrieve, the ZK's task is to display them nicely and easying the task of organising them to (re)build something.  
To use the PIS, simply upload your hand-written zettel and name them - that's it! Now you're able to use the ZK and it's visualisation tools to work with your accumulated knowledge.

## SETUP

```
git clone https://github.com/IsHaltEchtSo/pis_data_server.git

cd pis_data_server

python -m venv venv && . venv/bin/activate

pip install -r requirements.txt

mkdir instance && cp pis_app/config.py instance/private_config.py
```
### Database Migration
- Uncomment and update the settings in instance/private_config.py to connect to your database

- Change sqlalchemy.url value under pis_app/alembic.ini to connect to your database
``` 
cd pis_app 
alembic upgrade head
sh run.sh
```