import string
import random

if __name__=="__main__":
    while True:
        print("-----------------------------------")
        print("Welcome to Password Generator app ")
        print("-----------------------------------")
        length = int(input("Enter password length: "))
        print("Enter the complexity of password ")
        al=int(input("count of Alphabets: "))
        no=int(input("count of Numbers: "))
        spl=int(input("count of special charaters: "))
        if (al+no+spl)>length:
            print(f"Invalid input count of characters {al+no+spl} must be eqaul to length of password {length}")
        else :
            temp=0
            if (al+no+spl)<length:
                temp=length-(al+no+spl)
            numbers = []
            alphabets=[]
            others=[]
            password=''
            numbers= string.digits
            letters= string.ascii_letters
            others=string.punctuation
            for i in range(al+temp):
                char=random.choice(letters)
                password+=char
            for i in range(no):
                char=random.choice(numbers)
                password+=char
            for i in range(spl):
                char=random.choice(others)
                password+=char
            print(f"the generated strong password  is {password}")
        ch=input("Do you want to contiue (yes/no):")
        if ch=='no':
            print("Exited sucessfully ")
            break