import re
str="""
navinpoonia@gmail.com
xyz1@yahoo.com 95844
+9144 49569 abcddsd ampo@hotmail.com
abcdef@gmail.com
"""

pattern=re.compile(r'\S+@\S+')
matches=pattern.finditer(str)

count = 1
for match in matches:
    c=list(match.span())
    with open("exercise11.txt",'a') as f:
        f.write(f"Email {count} : {str[c[0]:c[1]]} \n")
        count=count+1

