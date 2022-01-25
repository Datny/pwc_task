!!!  IMPORTANT !!!
Usernames and passwords should not be placed in github. 
I took liberty of passing them this way for ease of use.
This task is for recruitment. Normally placeholders would be used instead of them or environment variables + secrets.


Requirements:
Odoo community ver. 14
wkhtmltopdf 0.12.5
Python 3.6+ (Recommended by Odoo)  
Created and tested with Python 3.8.10
Postgresql version 10.0


To run project on Linux:
0. Pull odoo 14.0 from official repository and call it odoo-14-official. 
1. Activate virtual env You are using for the project.
2. sudo apt install python3-pip python3-dev libxml2-dev libxslt1-dev libldap2-dev libsasl2-dev libssl-dev libpq-dev libjpeg-dev
3. Go to odoo-14-official directory 
4. Install packages: pip install -r requirements.txt
5. Install wkhhtmltopdf 0.12.5
6. Install PostgreSQL ver > 10.0
7. Call commands below to create database, user and grant user access to database
```sudo -u postgres createuser -s odoo-u P
   sudo -u postgres createdb odoo-db
   sudo -u postgres psql 
   alter user "odoo-db" with encrypted password 'odoo-u';
   grant all privileges on database "odoo-db" to "odoo-u";
   \q
```
8. Change directory in run_odoo.sh and odoo.conf to fit Your project
9. To run project: ./run_odoo.sh  *After initial run you can change -i to -u(in run_odoo.sh) or remove it completely.