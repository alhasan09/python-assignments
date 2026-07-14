# Job Eligibility Portal
print('*' * 80)
print('Welcome to the Job Eligibility Portal!'.center(80))
print('*' * 80)

python_knowledge = input('Are you Proficient in Python? (yes / no) :\n').strip().lower()
experience = int(input('How many Years of Experience Or Projects do you have?\n'))
degree = input('Do you have a Computer Science Degree or a Bootcamp Certificate? (yes / no) :\n').strip().lower()

if python_knowledge == 'yes' and (experience >= 2 or degree == 'yes') :
    print('Congratulations! You have Qualified for the next Interview Stage.')
else :
    print("Unfortunately, Your Current Qualifications don't Meet the Job Requirements")
