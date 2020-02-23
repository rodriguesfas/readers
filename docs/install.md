This installation has been tested on the Ubuntu 19.04 Linux environment.

## Requeriment Computer

- CPU (Undefined)
- Memory RAM 1GB
- Storage space (Undefined)
- Conection RJ45

## Requeriment System
- Operational System (Linux Ubuntu 19.04)
- Anaconda 4.7.12
- Python 3.7.1
- Pip 19.3.1
- MongoDB

## Network
To get started you must have a wired network configured with static IP.<br>
<img src="http://127.0.0.1:8000/assets/img/network.png"><br>

- Configuration Example:<br>
<b>IP Address:</b> 192.168.0.98 <br>
<b>Network Mask:</b> 255.255.255.0<br>
<b>Default Route:</b> 192.168.0.1<br>
<b>Broadcast Address:</b> 192.168.0.255<br>

<img src="http://127.0.0.1:8000/assets/tutorial/access_cgi_impinj/00.png">

## Access CGI Impinj
Open the browser and access the IP you set for the Impinj reader.<br>

Enter your login and password.<br>
<img src="http://127.0.0.1:8000/assets/tutorial/access_cgi_impinj/01.png">

- By default:<br>
<b>Login:</b> <br>
<b>Password:</b>

You will be redirected to a page like this:
<img src="http://127.0.0.1:8000/assets/tutorial/access_cgi_impinj/02.png">

This means your network is set up correctly and you can now access your player through it.

## Download CheckPoint

> Private repository, you must have access credentials to clone.
 
    $ git clone https://RodriguesFAS@bitbucket.org/RodriguesFAS/checkpoint.git

## Create Enviroment (Dev)
    $ conda create --name checkpoint python=3.7
    $ conda activate checkpoint
    
    (checkpoint)$

## Dependency Install Auto

    (checkpoint) checkpoint$ pip install -r requirements.txt

## Dependency Install Manual
    (checkpoint) checkpoint$ pip install bson

    (checkpoint) checkpoint$ pip install flask
    (checkpoint) checkpoint$ pip install flask_pymongo
    (checkpoint) checkpoint$ pip install flask_bcrypt
    (checkpoint) checkpoint$ pip install flask_socketio

    (checkpoint) checkpoint$ pip install playsound
    (checkpoint) checkpoint$ pip install gobject PyGObject

## Project layout

    mkdocs.yml    # The configuration file.
    docs/
        index.md  # The documentation homepage.
        ...       # Other markdown pages, images and other files.

## Tests Install

    $ 

