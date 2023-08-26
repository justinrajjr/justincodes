class Calculator:
    def add(self, a, b):
        return a+b
    
    def subtract(self, a, b):
        return a-b
        
    def multiply(self, a, b):
        return a*b

    def divide(self, a, b):
        return a/b

my_cl = Calculator()

while True:

    print("1: Add")
    print("2: Subtract")
    print("3: Multiply")
    print("4: Divide")
   
    
    ch = int(input("Select operation in(1/2/3/4): "))
    
    if ch in (1, 2, 3, 4):
        
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        
        if(ch == 1):
            print('result->',a, "+", b, "=", my_cl.add(a, b))
        elif(ch == 2):
            print('result->',a, "-", b, "=", my_cl.subtract(a, b))
        elif(ch == 3):
            print('result->',a, "*", b, "=", my_cl.multiply(a, b))
        elif(ch == 4):
            print('result->',a, "/", b, "=", my_cl.divide(a, b))
    
    else:
        print("Invalid Input")
