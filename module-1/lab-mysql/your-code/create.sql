/* Challenge 1 - Design the Database 

1. What entities and attributes should be included in the database?
Since we want to build a database for a dealership company, it's important to have all the following entities: 
- cars (which we'll have all information about the product that the company is selling);
- customers (which we'll have all information about the people who are willing to buy those products);
- salespersons (which we'll have all information about the employee who is selling that product);
- invoices (which we'll have all information about the process of buying the product).

To get all the main information about which entity, it's important to have a bunch of attributes who are able to define each one specifically:
- cars:
	-> vehicle_identification_number (data type: Primary Key, because it's an unique number used to identify each vehicle)
	-> manufacturer (data type: TEXT, because it's the name of the manufacturer who produced the car)
	-> model (data type: TEXT NOT NULL)
	-> year (data type: INTEGER, it'll say the year which the car was produced)
	-> color (data type: TEXT)
- customers:
	-> customer_id (data type: Primary Key, because each customer has an unique number)
	-> name (data type: TEXT NOT NULL)
	-> phone_number (data type: NUMERIC)
	-> email (data type: TEXT)
	-> address (data type: TEXT)
	-> city (data type: TEXT)
	-> state/province (data type: TEXT)
	-> country (data type: TEXT)
	-> postal_code (data type: NUMERIC)
- salespersons:
	-> staff_id (data type: Primary Key, because each employee is identified by an unique number)
	-> salesperson_name (data type: TEXT)
	-> store (data type: TEXT)
- invoices:
	-> invoice_number (data type: Primary Key, because each purchase is identified by a different number)
	-> date (data type: NUMERIC DATE)
	-> vehicle_identification_number (data type: Foreign Key from the cars column)
	-> customer_id (data type: Foreign Key from the customers column)
	-> staff_id (data type: Foreign Key from the salespersons column)
	
2. What are the relations between these entities? Which relations are one-to-one vs one-to-many vs many-to-many?



3. How can you use foreign keys to normalize your database design?
The only table which will have foreign keys is the invoices one, because it's the one that relates all of the three columns before
(cars, customers and salespersons).


Challenge 2 - Create the database and tables 
I created a database by entering the following commands in the terminal:
1.º Go to the folder you want to create the database
2.º Write the command sqlite3 lab_mysql.db
	You'll enter the prompt of the database and its absolute path /home/almsasantos/Desktop/Ironhack/dataptmad1019/module-1/lab-mysql/your-code/
	Write .quit to get out from the prompt of sqlite
3.º Write the command sqlite3 lab_mysql.db .dump > lab_mysql.sql
4.º Write the command sqlite3 lab_mysql.db < lab_mysql.sql to finally create the database and have it functioning on the DBeaver
*/

CREATE TABLE IF NOT EXISTS cars (
ID INT PRIMARY KEY AUTOINCREMENT,
vehicle_identification_number INT PRIMARY KEY, 
manufacturer VARCHAR(20), 
model VARCHAR(20), 
year YEAR NOT NULL, 
color VARCHAR(10)
);

CREATE TABLE IF NOT EXISTS customers (
ID INT PRIMARY KEY AUTOINCREMENT,
customer_id INT PRIMARY KEY,
name VARCHAR(20),
phone_number NUMERIC,
email VARCHAR(30),
address VARCHAR(30),
city VARCHAR(20),
state VARCHAR(20),
country VARCHAR(15),
postal_code NUMERIC
);

CREATE TABLE IF NOT EXISTS salespersons(
ID INT PRIMARY KEY AUTOINCREMENT,
staff_id INT PRIMARY KEY,
name VARCHAR(20),
store VARCHAR(20)
);

CREATE TABLE IF NOT EXISTS invoices(
ID INT PRIMARY KEY AUTOINCREMENT,
invoice_number TEXT PRIMARY KEY,
invoice_date TEXT,
vehicle_identification_number INT,
customer_id INT,
staff_id INT,
FOREIGN KEY(vehicle_identification_number) REFERENCES cars(vehicle_identification_number),
FOREIGN KEY(customer_id) REFERENCES customers(customer_id),
FOREIGN KEY(staff_id) REFERENCES salespersons(staff_id)
);

DROP TABLE IF EXISTS cars;
DROP TABLE IF EXISTS customers;
DROP TABLE IF EXISTS salespersons;
DROP TABLE IF EXISTS invoices;