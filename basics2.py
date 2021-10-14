import datetime
mynow = datetime.datetime.now()
print(mynow)

mynumber = 10
mytext = "hello"

print(list(range(1,10)))


student_grades = [9.1, 8.8, 7.5]

mysum = sum(student_grades)

length = len(student_grades)

mean = mysum / length
print(mean)

student_grades = [9.1, 8.8, 10.0, 7.7, 6.8, 8.0, 10.0, 8.1, 10.0, 9.9]
print(student_grades.count(10.0))

username = "Python3"
print(username.lower())

student_grades = {"Marry": 9.1, "John":8.8}
print()
#list you can mutable (add stuff)
#tuple you cannot append( immutable)
monday_temp = (20.0,90.0,89.7) #tuple

monday_temp = [9.1,9.9]
monday_temp.append(8.10)
monday_temp.clear()
monday_temp.append(2.1)
monday_temp.index(2.1)

print(username)
#function
def mean(value):
    if type(value) == dict:
        the_mean = sum(value.values()) /len(value)
    else:
        the_mean = sum(value) / len(value)
    return the_mean


student_grades = {"Marry": 9.1, "John":8.8}


print(mean(student_grades))

print(mean)

print(student_grades)

print(mean)

print(mean)

print ("nothing")



