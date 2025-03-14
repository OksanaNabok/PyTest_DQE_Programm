# AdventureWorks Robot Framework Tests

## Task
1. Create 2 DIFFERENT test cases for data checks on "AdventureWorks2012" database (3 different tables) and document them (name, steps, expected results).
Example TC#1 count for column; TC#2 average function for column, TC#3 max\min values, TC#4 values in range of list ...... etc.
Tables to use: 
-[Person].[Address]
-[Production].[Document]
-[Production].[UnitMeasure]
As a result you should have 6 different test cases for 3 different tables (2 per table).
2. Create user in MSSQL to connect from RF
3. Create a project for running Pytest tests.
4. Automate test cases from step 1 so that they can connect to MS SQL DB from SQL Module on your localhost.
5. Store a test report.


## Overview
This project uses **Pytest** to test data integrity in the AdventureWorks2012 database. The tests connect to MSSQL Server and validate: 
1. Record counts
2. Data consistency
3. Format and range validations

## Prerequisites
- MSSQL Server (with AdventureWorks2012 database installed)
- Python 3.8+
- Required Python packages (install via `requirements.txt`)

## Setup
1. - Create the MSSQL login using the script in `resources/SQLQuery_createUser.sql` Or 
- creating new user in SSMS:
go to Object Explorer -> Security -> Logins -> right button -> new login... -> create new Login with next credentials: 
- Login name: RobotTestUser1
- choose "sql server authentication"
- default database -> AdventureWorks2012
- -> press ok
next go to AdventureWorks2012 db -> security -> Users -> right button -> new user... -> create new User with next credentials: 
general 
- User name: RobotTestUser1
- Login name: RobotTestUser1
- default schema: dbo
membership:
- database role membership: db_datareader
- -> press ok

## Install dependencies
pip install -r requirements.txt

## Running Tests
Run tests and generate an HTML report:
pytest --html=reports/pytest_report.html --self-contained-html

## Viewing Reports
Open `reports/pytest_report.html` in any browser to view the detailed test report.