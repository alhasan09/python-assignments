users = {
    'i':'12',
    'ali_ahmed':'se4wgr',
    'hosam_adel':'asdfgh'
}

users_info = {
    'i': {
        'full name' : 'Amira Ali Ahmed',
        'balance' : 173,
        'last_transaction': 'No transactions yet'
    },
    'ali_ahmed' : {
        'full name' : 'Ali Ahmed Ali',
        'balance' : 134373,
        'last_transaction': 'No transactions yet'
    },
    'hosam_adel' : {
        'full name' : 'Hosam Adel Ali',
        'balance' : 53273,
        'last_transaction': 'No transactions yet'
    },
}

def register():
    while True:
        fullname = input('Enter your full name (or 0 to cancel):\n').title().strip()
        if fullname == '0':
            return
        elif fullname == '':
            print('Error: This field cannot be empty. Please try again.')
        else:
            break

    while True:
        username = input('Enter a unique username (or 0 to cancel):\n').strip()
        if username == '0':
            return
        elif username == '':
            print('Error: This field cannot be empty. Please try again.')
        elif username in users:
            print("Error: This username is already taken. Please try another.")
        else:
            break

    password_flag = True
    while password_flag: 
        password = input("Enter a secure password (or 0 to cancel):\n").strip() 
        if password == '0':
            return
            
        has_digits = False
        has_upper = False
        has_lower = False         
        for letter in password:
            if letter.isdigit():
                has_digits = True
            if letter.isupper():
                has_upper = True
            if letter.islower():
                has_lower = True
                
        if has_digits and has_upper and has_lower and len(password) >= 6:
            print('Password accepted!')
            password_flag = False                
        else:
            print('Error: Password must be at least 6 characters long and contain uppercase, lowercase, and numbers.')  
            
    print('Account registered successfully! You can now log in.')
    users.update({username: password})
    users_info.update({username: {'full name': fullname, 'balance': 0, 'last_transaction': 'No transactions yet'}})

def login():
    tries = 3
    while tries > 0:
        username = input('Enter your username (or 0 to cancel):\n').strip()
        if username == '0':
            return
            
        password = input('Enter your password (or 0 to cancel):\n').strip()
        if password == '0':
            return

        if username in users and users[username] == password:
            fullname = users_info[username]['full name']
            balance = users_info[username]['balance']
            
            print('=' * 80)
            print(f"Welcome back, {fullname}!".center(80))
            print(f"Your current balance is: {balance} EGP".center(80))
            print('=' * 80)
            bank_menu(username)
            return 
        else:
            tries -= 1
            if tries > 0:
                print(f"Error: Invalid username or password. You have {tries} attempt(s) left.")
            else:
                print("Error: All attempts used. Returning to main menu.")

def bank_menu(username):
    condition = True
    while condition:
        option = input('\n========== Bank Menu ==========\n'
                '1. Check Balance\n'
                '2. Deposit\n'
                '3. Withdraw\n'
                '4. Transfer\n'
                '5. Change Password\n'
                '6. Show Last Transaction\n'
                '7. Logout\n'
                '\nPlease choose an option: ').strip()
        
        if option == '1':
            check_balance(username)
        elif option == '2':
            deposit(username)
        elif option == '3':
            withdraw(username)
        elif option == '4':
            transfer(username)
        elif option == '5':
            change_password(username)
        elif option == '6':
            show_last_transaction(username)
        elif option == '7':
            return
        else:
            print("Error: Invalid choice! Please select a valid option from the menu.")
    
def check_balance(username):
    print(f"Your current balance is: {users_info[username]['balance']} EGP")

def deposit(username):
    amount = input("Enter the amount to deposit (or 0 to cancel):\n").strip()
    if amount == '0':
        return
    if amount.isdigit():
        amount_val = int(amount)
        if amount_val <= 0:
            print('Error: Invalid amount. Please enter a value greater than zero.')
        else:
            users_info[username]['balance'] += amount_val
            users_info[username]['last_transaction'] = f"Deposited {amount_val} EGP"
            print('\n--- Transaction Receipt ---')
            print('Type: Deposit')
            print(f'Amount: {amount_val} EGP')
            print(f"New Balance: {users_info[username]['balance']} EGP")
            print('---------------------------\n')
    else:
        print("Error: Invalid input! Please enter numbers only.")

def withdraw(username):
    amount = input("Enter the amount to withdraw (or 0 to cancel):\n").strip()
    if amount == '0':
        return
    if amount.isdigit():
        amount_val = int(amount)
        if amount_val <= 0 :
            print('Error: Invalid amount. Please enter a value greater than zero.')
        elif amount_val > users_info[username]['balance']:
            print('Error: Insufficient balance.')
        else:
            users_info[username]['balance'] -= amount_val
            users_info[username]['last_transaction'] = f"Withdrew {amount_val} EGP"
            print('\n--- Transaction Receipt ---')
            print('Type: Withdrawal')
            print(f'Amount: {amount_val} EGP')
            print(f"New Balance: {users_info[username]['balance']} EGP")
            print('---------------------------\n')
    else:
        print("Error: Invalid input! Please enter numbers only.")

def transfer(username):
    print('--- Transfer Funds ---')
    recipient_username = input("Enter the recipient's username (or 0 to cancel):\n").strip()
    if recipient_username == '0':
        return
    amount = input("Enter the amount to transfer (or 0 to cancel):\n").strip()
    if amount == '0':
        return
    
    if recipient_username in users and recipient_username != username:
        if amount.isdigit():
            amount_val = int(amount)
            if amount_val > 0 and amount_val <= users_info[username]['balance']:
                users_info[username]['balance'] -= amount_val
                users_info[recipient_username]['balance'] += amount_val
                users_info[username]['last_transaction'] = f"Transferred {amount_val} EGP to {recipient_username}"
                users_info[recipient_username]['last_transaction'] = f"Received {amount_val} EGP from {username}"
                print('\n--- Transaction Receipt ---')
                print('Type: Transfer')
                print(f'Amount: {amount_val} EGP')
                print(f'Recipient: {recipient_username}')
                print(f"New Balance: {users_info[username]['balance']} EGP")
                print('---------------------------\n')
            else:
                print('Error: Invalid amount or insufficient balance.')
        else:
            print("Error: Invalid input! Please enter numbers only.")
    else:
        print('Error: Invalid or unallowed username.')

def change_password(username):
    print('--- Change Password ---')
    current_pass = input('Enter your current password (or 0 to cancel):\n').strip()
    if current_pass == '0':
        return
        
    if current_pass == users[username]:
        password_flag = True
        while password_flag:  
            new_pass = input('Enter your new password (or 0 to cancel):\n').strip()
            if new_pass == '0':
                return
                
            has_digits = False
            has_upper = False
            has_lower = False         
            for letter in new_pass:
                if letter.isdigit():
                    has_digits = True
                if letter.isupper():
                    has_upper = True
                if letter.islower():
                    has_lower = True
                    
            if has_digits and has_upper and has_lower and len(new_pass) >= 6:
                print('Password successfully changed!')
                users[username] = new_pass
                password_flag = False                
            else:
                print('Error: Password must be at least 6 characters long and contain uppercase, lowercase, and numbers.') 
    else:
        print('Error: Incorrect current password.')

def show_last_transaction(username):
    print('\n--- Last Transaction ---')
    print(users_info[username]['last_transaction'])
    print('------------------------\n')


def main():
    print('=' * 80)
    print('========== Welcome To Python Bank =========='.center(80))
    print('=' * 80)
    print('\n')
    print(f" Total Registered Users: {len(users)} ".center(80))
    
    condition = True
    while condition:
        option = input('\n1. Register\n' 
                       '2. Login\n' 
                       '3. Exit\n'
                       '\nPlease choose an option: ').strip()
        if option == '1':
            register()
        elif option == '2':
            login()
        elif option == '3':
            print('Thank you for using Python Bank. Goodbye!')
            condition = False
        else:
            print("Error: Invalid choice! Please select a valid option from the menu.")

main()