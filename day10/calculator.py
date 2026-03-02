def add(n1,n2):
    return n1+n2
def sub(n1,n2):
    return n1-n2
def product(n1,n2):
    return n1*n2
def quotient(n1,n2):
    return n1/n2
def remainder(n1,n2):
    return n1%n2

arithmetic_operators={
    '+':add,
    '-':sub,
    '*':product,
    '/':quotient,
    '%':remainder
}

# def calculation():
first_num=float(input('enter the first number: '))
again=True
while again:
        ask_operator=input('+\n''-\n''*\n''/\n''%\n''Which operation you want to perform? ')
        next_number=float(input('enter the next number: '))
        print(f'{first_num} {ask_operator} {next_number} =',arithmetic_operators[ask_operator](first_num,next_number))
        
        ask_again=input('Type "y" to continue calculating with 100.0, or type "n" to start a new calculation:')
        if ask_again=='y':
            first_num=arithmetic_operators[ask_operator](first_num,next_number)
        else:
            again=False
            print('\n'* 20)
#             calculation()
# calculation()
        
