student=[[44,'Prasad',75,87],[13,'Ganguly',82,79],
        [53,'Sasikala',72,80],[35,'Manohar',86,85]]
student.sort()
print(student)
student.sort(key=lambda temp:temp[2])
print(student)
student.sort(key=lambda temp:temp[3])
print(student)
