# Inventory Management System

## Overview
This project is an inventory management system (Let's call it InvtrackPRO, Thank ChatGPT for this name😂)
 using the `Django web framework` and `PostgreSQL` as the relational database.

This inventory management system focuses on wholesale business where it needs to have warehouses, suppliers, and orders from customers. Anyway, this project will rely much on admin functionality, and the admin needs to manually add transactions.


**For more information about design and development** : [Wiki Page](https://github.com/Sosokker/Inventory-Management-System/wiki) 
- [Database Design](https://github.com/Sosokker/Inventory-Management-System/wiki/Database-Design)
- [Query Example](https://github.com/Sosokker/Inventory-Management-System/wiki/Query-Example)

## Installation

Here are the overview of steps to install and run this project.

1. Install `Python`
2. Install `PostgreSQL` via `docker` or `installer`
3. Create virutal environment then install requirements
4. Migrate database, load fixture, and run server

---

### Install Python and PostgreSQL

#### Install python

1. Download python installer and follow the guide in [Python website](https://www.python.org/downloads/)

2. Check python installation
```
python --version
```
#### Install PostgreSQL via docker

0. First of all [download and install docker desktop](https://docs.docker.com/desktop/) that contain docker engine, docker CLI, and etc.

1. Pull docker `postgres` Image
```bash
docker pull postgres
```
2. Create a Docker container for PostgreSQL. Adjust these variable in the command below
- `YOUR_CONTAINER_NAME`
- `YOUR_POSTGRE_USERNAME`
- `YOUR_POSTGRE_PASSWORD`
```bash
docker run --name YOUR_CONTAINER_NAME -e POSTGRES_USER=YOUR_POSTGRE_USERNAME -e POSTGRES_PASSWORD=YOUR_POSTGRE_PASSWORD -p 5432:5432 -d postgres
```
3. Wait for the container to start. You can check the logs with
```bash
docker logs YOUR_CONTAINER_NAME
```

> Extra: you can download pgadmin4 via docker which is a tool for manage postgres database. [Click here For more information](https://www.pgadmin.org/download/pgadmin-4-container/)

Host: `localhost`
Port: `5432` (or the port you specified)
Database: `postgres`
Database User: `YOUR_POSTGRE_USERNAME`
Password: `YOUR_POSTGRE_PASSWORD`

#### Install PostgreSQL via Installer

We recommend to [install postgres](https://www.postgresql.org/download/) with [pgadmin4](https://www.pgadmin.org/download/)

After install `postgres` and `pgadmin4` you must

1. Create new database.
2. Specify username, password and host as you desired.

Usually Host name will be `localhost` , port will be `5432`, and default postgres database user is `postgres`

---

### Setup Environment and Django

#### Clone this repository and Create virtual environment with `venv` or `virtualenv`.

1. Clone this repository
```bash
git clone https://github.com/Sosokker/Inventory-Management-System
cd Inventory-Management-System
```

2. Create virtual environment and use it to install require packages

```bash
python -m venv venv
```
(Optional: You can use venv instead)Install virtualenv via pip
```bash
python -m pip install --user virtualenv
python -m virtualenv venv
```
```bash
# Access virtual environment using
# Windows
.\venv\Scripts\activate
# Linux or MacOS
source venv/bin/activate
```
3.  Install require module.
```
pip install -r requirements.txt
```

#### Setup Django
1. Create file `.env` to provide environment varible for Django
**You can look at `sample.env` for more information and others environment variables to set.**
```bash
SECRET_KEY=your_secret_key
DEBUG=True # Set False on production
ALLOWED_HOSTS=localhost, 127.0.0.1, ::1
DB_NAME=YOUR_DATABASENAME # ex: postgres
DB_USER=YOUR_POSTGRE_USERNAME 
DB_PASSWORD=YOUR_POSTGRE_PASSWORD
DB_HOST=YOUR_DB_HOST # ex: localhost
DB_PORT=your_DB_PORT # ex: 5432
```
Generate` Secret key` from  [Djecrety](https://djecrety.ir/)

**Don't forget to change `your_secret_key` to your secret key (without quote)**

2. Migrate database, load fixture, and then runserver
```bash
python manage.py migrate
python manage.py loaddata fixtures/data.json
python manage.py runserver
```

You can now access webpage via [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
or you can change port by

```bash
python manage.py runserver <PORT>
```

## For Testing

<table>
<thead>
  <tr>
    <th>Username</th>
    <th>Password</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>sirin</td>
    <td>helloworld123</td>
  </tr>
</tbody>
</table>

Or you can create new super user by

```bash
python manage.py createsuperuser
```

## Resource

1. [startbootstrap-sb-admin-2](https://github.com/startbootstrap/startbootstrap-sb-admin-2) for UI
