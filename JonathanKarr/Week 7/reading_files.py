student_file = open("student_file.txt","r")
print(student_file.readable())
#print(student_file.read())
#print(student_file.readline())
#print(student_file.readline())
#print(student_file.readlines())
print(student_file.readlines()[1])
student_file.close()