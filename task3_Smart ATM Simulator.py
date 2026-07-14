# Smart ATM Simulator

print('*' * 80)
print('Welcome to the Smart ATM!'.center(80))
print('*' * 80)

pin = '1234'
balance = 5000

pin_input = input('Enter your PIN:\n').strip()
if pin == pin_input :
    option = input('Select an option:\n1. Withdraw Cash\n2. Check Balance\n').strip()
    if option == '1' :
        withdrawal_amount = int(input('Enter the Amount to Withdraw.'))
        if withdrawal_amount <= balance :
            print(f'Transaction Completed Successfully.\nYour remaining Balance is : {balance - withdrawal_amount:,} EGP.')
        else :
            print('Sorry, Insufficient Balance.')
    elif option == '2' :
        print(f'Your Current Balance is : {balance:,} EGP')
    else :
        print('Invalid Option, Try Again.')
else :
    print('Invalid PIN. Access Denied')
