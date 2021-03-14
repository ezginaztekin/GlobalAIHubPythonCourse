#giving first student and grades
name=input("Please give the name of student:")
midterm=input("Please give the midterm grade:")
project=input("Please give the project grade:")
final=input("Please give the final grade:")

name={"midterm":int(midterm),"project": int(project),"final":int(final)}
namepassing= name["midterm"]*(0.3)+name["project"]*(0.3)+name["final"]*(0.4)
print(name)
print("passingGrade:",namepassing)

#giving second student and grades
name1=input("Please give the name of student:")
midterm1=input("Please give the midterm grade:")
project1=input("Please give the project grade:")
final1=input("Please give the final grade:")

name1={"midterm":int(midterm1),"project": int(project1),"final":int(final1)}
namepassing1= name1["midterm"]*(0.3)+name1["project"]*(0.3)+name1["final"]*(0.4)
print(name1)
print("passingGrade:",namepassing1)

#giving third student and grades
name2=input("Please give the name of student:")
midterm2=input("Please give the midterm grade:")
project2=input("Please give the project grade:")
final2=input("Please give the final grade:")

name2={"midterm":int(midterm2),"project": int(project2),"final":int(final2)}
namepassing2= name2["midterm"]*(0.3)+name2["project"]*(0.3)+name2["final"]*(0.4)
print(name2)
print("passingGrade:",namepassing2)

#giving fourth student and grades
name3=input("Please give the name of student:")
midterm3=input("Please give the midterm grade:")
project3=input("Please give the project grade:")
final3=input("Please give the final grade:")

name3={"midterm":int(midterm3),"project": int(project3),"final":int(final3)}
namepassing3= name3["midterm"]*(0.3)+name3["project"]*(0.3)+name3["final"]*(0.4)
print(name3)
print("passingGrade:",namepassing3)

#giving last student and grades
name4=input("Please give the name of student:")
midterm4=input("Please give the midterm grade:")
project4=input("Please give the project grade:")
final4=input("Please give the final grade:")

name4={"midterm":int(midterm4),"project": int(project4),"final":int(final4)}
namepassing4= name4["midterm"]*(0.3)+name4["project"]*(0.3)+name4["final"]*(0.4)
print(name4)
print("passingGrade:",namepassing4)

#list of all passinggrades
list=[namepassing,namepassing1,namepassing2,namepassing3,namepassing4]
list.sort(reverse=True)

print(list)
