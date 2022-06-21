### how to setup
---
#### install all necessities
  - install docker engine   
    ```cmd
    url for installation cmds:
    https://docs.docker.com/engine/install/ubuntu/
    ```
  - mongo-db in a container
    ```cmd
    cd largoserver
    chmod +x mongo.sh
    ./mongo.sh

    can use Compass mongo-db client, or 
    cmd-line-client:
    mongo
    or 
    mongosh

    ```
  - install all python packages
    ```cmd
    install python virtualenv:
    sudo apt-get install python3-pip
    sudo pip3 install virtualenv
    virtualenv ven
    source ven/bin/activate

    install packages under (ven):
    pip install -r requirements.txt

    to get out of ven:
    source deactivate

    ```
  - run fastAPI
    ```cmd
    python3 fapiserver.py
    ```
    For modifying settings for port-numbers and db names, 
    modify config.toml

    Basic test usage of fastAPI:
    in Chrome-browser (or Edge):

    ```cmd
    localhost:5002/docs

    Basic test:
    get /  should see 'Hello World'

    load meta-DB
    get /load_meta
    check mongo-db - should see 2 collections in META

    load app-db
    get /load_db
    check mongo-db - should see 2 collections in LDB
    ```
    
