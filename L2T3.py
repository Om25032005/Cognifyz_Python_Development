import re
def checker(password):
    minlength=8
    stronglength=12
    digit=bool(re.search(r'\d', password))
    uppercase=bool(re.search(r'[A-Z]', password))
    lowercase=bool(re.search(r'[a-z]', password))
    specialchar=bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))
    length = len(password)
    if length<minlength:
        return "Easy"
    criteria=sum([uppercase,lowercase,digit,specialchar])
    if length>=stronglength and criteria==4:
        return "Strong"
    elif length>=minlength and criteria>=3:
        return "Moderate"
    else:
        return "Easy"
password = input("Enter your password: ")
result=checker(password)
print(f"Password strength is :",result)



"""
Output:-

PS D:\cognifyz\L2> Python L2T3.py
Enter your password: omkar123
Password strength is : Easy
PS D:\cognifyz\L2> Python L2T3.py
Enter your password: omkar123@
Password strength is : Moderate
PS D:\cognifyz\L2> Python L2T3.py
Enter your password: Omkar123@ 
Password strength is : Moderate
PS D:\cognifyz\L2> Python L2T3.py
Enter your password: Omkar1234@#$
Password strength is : Strong
PS D:\cognifyz\L2>

 """