# Python Banking System

A Python-based banking system that manages user accounts with functionalities like adding new accounts, depositing, withdrawing funds, and checking balances. This system utilizes Object-Oriented Programming (OOP) principles and stores account data using `.txt` and `.pkl` files for persistence.

## Features

- **Add Account**: Create new accounts with a unique ID, name, and initial balance.
- **Deposit**: Add funds to an account.
- **Withdraw**: Remove funds from an account, ensuring sufficient balance.
- **Check Balance**: View the current balance of an account.
- **Data Persistence**: Supports both `.txt` and `.pkl` formats for saving account information.

## Prerequisites

- Python 3.x
- Basic understanding of file handling

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Aqeel-110/Python-Banking-System.git
   
2. Navigate to the project directory:
   cd Python-Banking-System

3. Ensure Python is installed on your system. You can check by running: python --version

## Usage

Run the program:
python Mini\ Project.py

## Example

--- Banking System ---

1. Add Account:

   Enter Account ID: 101

   Enter Account Name: Alice

   Enter Initial Balance: 5000

   Account added successfully!

2. Deposit:

   Enter Account ID: 101

   Enter amount to deposit: 2000

   Deposit successful! New balance: 7000

3. Withdraw:

   Enter Account ID: 101

   Enter amount to withdraw: 3000

   Withdrawal successful! New balance: 4000

4. Check Balance:

   Enter Account ID: 101

   Current balance: 4000

## Data Files

   bank_data.txt: Text file used to store account information.

   accounts_data.pkl: Pickle file used for binary data storage.

## License
This project is licensed under the MIT License. See the LICENSE file for details.
