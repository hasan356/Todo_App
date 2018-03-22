# Todo App using Django Rest Framework and Cassandra DataBase
Designing Restful Api for pulling data from Cassandra Databases using Django Framework

## Technologies used
* [Django](https://www.djangoproject.com/): The web framework for perfectionists with deadlines (Django builds better web apps with less code).
* [DRF](www.django-rest-framework.org/): A powerful and flexible toolkit for building Web APIs
* [Django_Cassandra_Engine](https://r4fek.github.io/django-cassandra-engine//): first Cassandra backend for Django Framework.

## Installation
* If you wish to run your own build, first ensure you have python globally installed in your computer. If not, you can get python [here](https://www.python.org").

* After doing this, confirm that you have installed virtualenv globally as well. If not, run this:
    ```bash
        $ pip install virtualenv
    ```
* Now, create a virtual environment within the project directory by typing
    ```bash
        $ virtualenv newenv
    ```
    
* To install packages into the isolated environment, you must activate the virtual enviroment by typing
    ```bash
        $ source newenv/bin/activate
    ```
 * Set-up Cassandra into your system
    
    * Add a Personal Package Archives (PPA) using this command to install Oracle JRE package
    
    ```bash
        sudo add-apt-repository ppa:webupd8team/java
    ```
    * Update the package database:
    
    ```bash
        sudo apt-get update
    ```
    * Then install the Oracle JRE
    
    ```bash
       sudo apt-get install oracle-java8-set-default
    ```
    * After installing it, verify that it's now the default JRE:
   ```bash 
        java -version
    ```
    * We’ll install Cassandra using packages from the official Apache Software Foundation repository provided by Datastax, so start by adding the repo so that the packages are available to your system.
    * DataStax source for stable version of Cassandra
    ```bash
        echo "deb http://debian.datastax.com/community stable main" | sudo tee -a /etc/apt/sources.list.d/cassandra.sources.list
    ```
    * To avoid package signature warnings during package updates, we need to add three public keys from the Apache Software Foundation associated with the package repositories.
    ```bash
        gpg --keyserver pgp.mit.edu --recv-keys F758CE318D77295D
    ```
    ```bash
        gpg --export --armor F758CE318D77295D | sudo apt-key add -
    ```
    ```basg
        gpg --keyserver pgp.mit.edu --recv-keys 2B5C1B00
    ```
    ```bash
        gpg --export --armor 2B5C1B00 | sudo apt-key add -
    ```
    ```bash    
        gpg --keyserver pgp.mit.edu --recv-keys 0353B12C
    ```
    ```bash
        gpg --export --armor 0353B12C | sudo apt-key add -
    ```    
    * Update the package database once again:
    ```bash
        sudo apt-get update
    ```
    * Finally, install Cassandra
    ```bash
        sudo apt-get install cassandra
    ```
    
    * If you were able to successfully start Cassandra, check the status of the cluster. If the status is UN, it means it's Up and Normal.
    ```bash
        sudo nodetool status
    ```
    * Then connect to it using its interactive command line interface cqlsh.
    ```bash
        cqlsh
    ```
    * Type exit to quit
    ```bash
        exit
    ```

* Then, Git clone this repo to your PC
    ```bash
        $ git clone https://github.com/hasan356/Todo_App.git
    ```
    * #### Dependencies
    1. Cd into your the cloned repo as such:
        ```bash
            $ cd Todo_App/myproject/
        ```
    2. Install the dependencies needed to run the app:
        ```bash
            $ pip install -r requirements.txt
        ```
    3. Make those migrations work
         Sync it with Cassandra DB

        ```bash
            $ python manage.py sync_cassandra
        ```
# REST_API

    # http://localhost:8000/todo api for creating the todo task
    # http://localhost:8000/todo/<key>/detail to see the detail of specific task
    # http://localhost:8000/todo/<key>/update for update the specific task
    # http://localhost:8000/todo/<key>/delete for delete the specific task
    




