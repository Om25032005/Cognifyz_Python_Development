def valid(email):
    if email.count('@') != 1:
        return 1
    local_part, domain_part = email.split('@')
    if '.' not in domain_part:
        return 1
    if not local_part or not domain_part:
        return 1
    return 0
email=str(input("enter a email  "))
if((valid(email))==0):
    print("email is valid")
else:
    print("email is invalid")

"""
Output:-

PS D:\cognifyz\L1> Python L1T3.py
enter a email  omkarchechare2005@gmail.com
email is valid
PS D:\cognifyz\L1> Python L1T3.py
enter a email  omchechare223gmail.com
email is invalid
PS D:\cognifyz\L1> Python L1T3.py
enter a email  omchechare223gmailcom
email is invalid
PS D:\cognifyz\L1>

"""