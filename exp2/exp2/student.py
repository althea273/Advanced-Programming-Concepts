mark1=int(input("Enter your marks: "))
mark2=int(input("Enter your marks: "))
mark3=int(input("Enter your marks: "))
mark4=int(input("Enter your marks: "))
marks=(mark1+mark2+mark3+mark4)/4
if(marks>=90):
    print("Excellant performance!")
elif(marks>=80):
    print("very good performance")
elif(marks>=70):
    print("good performance")
elif(marks>=60):
    print("Average performance")
else:
    print("Poor performance")