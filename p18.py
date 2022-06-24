all=0
use_in =input().split(" ")
for i in use_in:
    if i== "K" or i=="k":
        all=all+13
    elif i=="A"or i=="a":
        all=all+1
    elif i=="J" or i=="j":
        all=all+11
    elif i=="Q" or i=="q":
         all=all+10
    else:
        all=all+int(i)
print(all) 