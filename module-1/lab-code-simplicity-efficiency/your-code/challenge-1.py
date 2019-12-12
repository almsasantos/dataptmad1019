"""
This is a dumb calculator that can add and subtract whole numbers from zero to five.
When you run the code, you are prompted to enter two numbers (in the form of English
word instead of number) and the operator sign (also in the form of English word).
The code will perform the calculation and give the result if your input is what it
expects.

The code is very long and messy. Refactor it according to what you have learned about
code simplicity and efficiency.
"""

print('Welcome to this calculator!')
print('It can add and subtract whole numbers from 0 to 5')
fst_num = int(input('Please choose your first number (0 to 5): '))
operator = input('What do you want to do? plus or minus: ').lower()
sec_num = int(input('Please choose your second number (0 to 5): '))

def calculator(fst_num, operator, sec_num):
    fst = sec = [0, 1, 2, 3, 4, 5]
    if fst_num in fst and sec_num in sec and operator == 'plus':
        result = fst_num + sec_num
        print(f'{fst_num} + {sec_num} = {result}')
    elif fst_num in fst and sec_num in sec and operator == 'minus':
        result = fst_num - sec_num
        print(f'{fst_num} - {sec_num} = {result}')
    else:
        print("I am not able to answer this question. Check your input.")

calculator(fst_num, operator, sec_num)

print("Thanks for using this calculator, goodbye :)")