
print(r"""
 _____________________
|  _________________  |
| | +0 D M          | |      ██████╗  █████╗ ██╗      ██████╗
| |_______________0.| |     ██╔════╝ ██╔══██╗██║     ██╔════╝
|  ___ ___ ___   ___  |     ██║      ███████║██║     ██║     
| | 7 | 8 | 9 | | + | |     ██║      ██╔══██║██║     ██║     
| |___|___|___| |___| |     ╚██████╗ ██║  ██║███████╗╚██████╗ ██╗
| | 4 | 5 | 6 | | - | |      ╚═════╝ ╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═╝
| |___|___|___| |___| |                                 
| | 1 | 2 | 3 | | x | |                     The fancy calculator ..
| |___|___|___| |___| |
| | . | 0 | = | | / | |     Because counting on your fingers doesn't scale ..
| |___|___|___| |___| |                 
|_____________________|     
      
      """)

def calc (num1,num2, op):
    if op == '+':
        return num1+num2
    elif op == '-':
        return num1-num2
    elif op == '*':
        return num1*num2
    elif op == '/':
        return num1/num2
    else:
        return 0.0
        

print("Welcome to the MATH arena .. lets duel in Numbers.. 😜")
keep_calcing=False
result = 0
while (True):
    
    if keep_calcing:
        num1 = result
    else:
        result = 0
        print("\ncalculator warming up ... OK! lets do some MATH!!\n")
        num1 = float(input("gimme a Number then:\n>>> "))
    
    op = input("what's the Operation tho?? .. (+,-,*,/)\n>>> ")
    
    while op not in "+-*/":
        op = input("com'on mate gimme a real operation ... pleaase 🙏🙏🙏:\n>>> ")
    
    num2 = float(input("the Other Number is:\n>>> "))
    
    result = round(float(calc(num1,num2,op)),2)
    print(f"{num1} {op} {num2} = {result}")
    
    keep_calcing = input(f"wanna use {result} in the next operation? (y/N): ").lower() == 'y' and True or False
