student = {
    "name": '张伟',
    "age": "20",
    "course":['数学','英语']
}
# student["course"]=['数学','英语',"物理"]

student["course"].append("物理")
student["course"].remove('英语')

print(student)

