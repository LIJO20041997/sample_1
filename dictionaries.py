#dictionaries
'''symbol={
    "h":"hydrogen",
    "he":"helium",
    "li":"lithium",
    "c":"carbon",
    "o":"oxygen",
    "n":"nitrogen"

}
print(symbol)
print(symbol.keys())
print(symbol.values())
print(symbol.items())
print(symbol["h"])
symbol["p"]="phosphrous"
print(symbol)
symbol["c"]="carondioxide"
print(symbol)
symbol.update({"p":"sulphur"})
print(symbol)'''

'''student={
    1: "george",
    "class": 6,
    "mark":[22,34,89,81,67]
}

print(student.items())
print(student.get("class"))
print(student)
newlst=list(student.items())
print(newlst)
si=dict(newlst)
print(si)'''

#create a dictonary of students and get the user input of student name print their respective marks
students_marks={
    "akhil":[87,89,76,75,90,89],
    "amal":[67,78,56,79,88,90],
    "lijo":[89,90,99,83,78,77],
    "jidhu":[67,78,89,69,98,77]
}
name =input("the name of the student is: ")
def marklist(name):
    for i in students_marks:
        if i==name:
            print("the marks of",name,"is",students_marks.get(name))
marklist(name)
marklist("amal")

