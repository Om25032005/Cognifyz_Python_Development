from collections import Counter
import re
def countwords(file):
    try:
        with open(file, 'r') as f:
            text = f.read()
    except FileNotFoundError:
        print(f"Error: The file '{file}' was not found.")
        return
    except IOError:
        print(f"Error: Could not read the file '{file}'.")
        return
    text=text.lower()
    words=re.findall(r'\b\w+\b', text)
    wordcount=Counter(words)
    sortedwordcount=dict(sorted(wordcount.items()))
    for word,count in sortedwordcount.items():
        print(f'{word}: {count}')

file= "D:\cognifyz\L2\L2T5\om.txt" 
countwords(file)





"""
output:-


PS D:\cognifyz\L2\L2T5> Python L2T5.py
am: 2
from: 1
i: 2
is: 1
loni: 1
my: 1
name: 1
omkar: 1
onest: 1
person: 1
very: 1
PS D:\cognifyz\L2\L2T5>

"""