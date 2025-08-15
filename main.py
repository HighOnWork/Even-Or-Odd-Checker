Reset = '\033[0m'
Red = '\033[31m'
Cyan = '\033[36m'

Num = int(input("Write the number you want to check: "))

Remainder = Num % 2

if Remainder == 0:
    print(f"{Num} is an {Cyan} even {Reset} number ")
else:
    print(f"{Num} is an {Red} odd {Reset} number")