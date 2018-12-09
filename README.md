project 1
=============

# Log Analysis
This is a project for Udacity full stack web developer

# Project Description:
Using sql query to fetch some data from a 'newsdata.sql' database and make connection to this database.

# Prerequisites
This project running in virtual machine using vagrant so you need to install :    
1- Install virtualbox

2- Install vagrant 

3- Git bash on Windows

4- Download	a FSND virtual machine:https://github.com/udacity/fullstack-nanodegree-vm

5- Download “newsdata.sql” it is a database.


## Start the Virtual Machine:
1- Open git bash
2-Create project folder “log-analysis-project”	and move 'newsdata.sql' to it . 
3- cd to file which has a vagrant file
5- Run vagrant up then vagrant ssh
6- pip3 install psycopg2 --user
7- pip3 install pycodestyle --user


## Connect to database :
Run these instruction in git bash
1- psql -d news -f newsdata.sql 		
2-use news database by this command 'psql -d news'
3-to close connection with 'news' database and return to vagrant vm ' \q ' press enter.

## Questions Are:
1- What	are	the	most popular three articles of all time?
2- Who are the most	popular	article	authors	of	all	time?
3- On which	days did more than 1% of requests lead to errors?

## Running the tests
You can run sql query like 'SELECT' in git bash .
or by run a python file in git bash 'python filename.py '
python file ,it contains of function to connect code with database and execute sql query.
