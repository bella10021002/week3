all = set(['John','Mary','Tina','Fiona','Claire','Eva','Ben','Bill','Bert'])
e = set(['John','Mary','Fiona','Claire','Ben','Bill'])
m = set(['Mary','Fiona','Claire','Eva','Ben'])

print("英文和數學都及格",set(e) & set(m))
print("數學不及格",set(all) - set(m))
print("英文及格且數學不及格",set(e) & (set(all) - set(m)))