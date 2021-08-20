### Step Setup:
This is a Guide for setup for this application.

1. Installing Git

    <pre>$ sudo apt install git</pre>
        
2. Install and Setup virtualenv (Also includes setup for workon).

    1. First we need to install python3-pip
       
        <pre>$ sudo apt install python3-pip</pre>
        
    2. Once done, we can now install virtualenv
        
        <pre>$ sudo pip3 install virtualenv</pre>
        
    3. Create Virtual Environment

        <pre>$ python3 -m venv "your virtual env name"</pre>

3. Clone Repository:

    <pre>$ git clone https://github.com/vkscnb/multiple-database-in-django.git</pre>

4. Create a new Environments for "Multiple Database withDjango".

    1. Create

        <pre>$ python3 -m venv "your virtual env name"</pre>
    
    2. Activate env

        <pre>$ source "env name"/bin/activate</pre>
        
5. Go to the cloned directory ,Location of this is supposed to be "/home/vikas/Desktop".

    1. Go to locations

        <pre>$ cd multiple-database-in-django</pre>

    2. Install below command for install all requirements and db migrations.

        <pre>
            $ pip install -r requirments.txt

            $ python manage.py makemigrations

            $ python manage.py migrate --database=user_db

            $ python manage.py migrate --database=product_db product
        </pre>
    
    3. If all setup are done. Run the Project by-

        <pre>$ python manage.py runserver</pre>

    4. Open in browser-
        <pre>http://127.0.0.1:8000</pre>
        


### Note. The project are runing using default SqlLite with different databse for user and product.
## Run project with using SqlLite and PostgresSql Data base
## Setup.
1. Intall postgres.
    <pre>
        $ sudo apt update

        $ sudo apt install postgresql postgresql-contrib
    </pre>

2. Create database and user.

    <pre>
        $ sudo su -  postgres

        $ psql

        $ CREATE DATABASE product_db;

        $ CREATE USER test WITH PASSWORD 'test1';

        $ ALTER ROLE test1 SET client_encoding TO 'utf8';

        $ ALTER ROLE test1 SET default_transaction_isolation TO 'read committed';

        $ ALTER ROLE test1 SET timezone TO 'UTC';

        $ GRANT ALL PRIVILEGES ON DATABASE product_db TO test1;
    </pre>

3. Modify code of tradexa/settings.py

    <pre>
        1. Comment the code from line 92 to 95.
        2. Uncomment the code from line 99 to 106.
    </pre>

4. Run the comman after the step 3 are done. 

    <pre>
        $ python manage.py migrate --database=product_db product
        $ python manage.py runserver
    </pre>
