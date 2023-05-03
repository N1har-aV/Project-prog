def calculator():
    while true:
        print('Enter + to add two numbers')
        print('Enter - to subtract two numbers')
        print('Enter * to multiply two numbers')
        print('Enter / to divide two numbers')
        user_input=input(': ')
        num1=int(input('Enter the first number: '))
        num2=int(input('Enter the second number: '))
        operation=input('Enter the wanted operation: ')
        if user_input== '+':
            result=num1+num2
            print(num1,'+',num2,'=',result)
        elif user_input=='-':
             result=num1-num2
             print(num1,'-',num2,'=',result)
        elif user_input=='*':
            result=num1*num2
            print(num1,'*',num2,'=',result)
        elif user_input=='/':
            result=num1/num2
            print(num1,'/',num2,'=',result)
            
        
    