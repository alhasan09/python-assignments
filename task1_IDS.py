# Instant Discount System

print('*' * 80)
print('Welcome to Our Store!'.center(80))
print('*' * 80)

purchase_amount = int(input('Enter your Purchase Amount.'))


if purchase_amount < 100 :
    discount = 0
elif purchase_amount < 500 :
    discount = 10
else :
    discount =20

discount_value = (discount/100) * purchase_amount
print(f'Your Available Discount is : {discount_value:,} EGP')
print(f'Total Amount after Discount is : {purchase_amount - discount_value} EGP')