def palindrome(str):
    rstr=str[::-1]
    if(str==rstr):
        print("string is palindrome")
    else:
        print('string is not palindrome')
str=str(input("enter string :"))
palindrome(str)



"""
Output:-

PS D:\cognifyz\L1> Python L1T5.py
enter string :OmKar
string is not palindrome
PS D:\cognifyz\L1> Python L1T5.py
enter string :madam
string is palindrome
PS D:\cognifyz\L1> Python L1T5.py
enter string :king
string is not palindrome
PS D:\cognifyz\L1> Python L1T5.py
enter string :abba
string is palindrome
PS D:\cognifyz\L1>


"""