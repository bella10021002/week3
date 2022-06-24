studentList = {
    "123":["Tom","DTGD"],
    "456":["Cat","CSIE"],
    "789":["Nana","ASIE"],
    "321":["Lim","DBA"],
    "654":["Won","FDD"]
}

inp = input("輸入查詢學號為:")

print(f"學生資料為:{inp} {studentList[inp][0]} {studentList[inp][1]}")