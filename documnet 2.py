# Interview-Style Questions Based on Conditional Statements
# 1. Check Even or Odd %operation is commmon approach try & opertor 
# b=int(input("enter the number:"))
# if(b%2==0):
#     print("even Number",b)
# else:
#     print("odd number")


# # & operator
# a=int(input("enter the number"))
# if(a&1==0):
#     print("even",a)
# else:
#     print("odd",a)

# 2. Divisible by 5 but Not by 10
# c=int(input("enter the number:"))
# if(c%5==0 and c%10!=0):
#     print("satisfy")
# else:
#     print("not satisty")

# 3. Biggest Among Two Numbers
a=4
b=7
if(a>b and b>a):
    print("a is greater than b")
else:
    print("b is greater than a")

# 4. Smallest Among Two Numbers
a=4
b=7
if(a<b or b<a):
    print("a is smallest")
else:
    print("b is smallest")

# 5. Divisible by 2, 3, and 6
a=16
if(a%2==0 or a%3==0 or a%6==0):
    print("satisty")
else:
    print("not satisy")

# 6. Voting Eligibility
age=18
if(age>=18):
    print("you are eligible for  vote")
else:
    print("you rae not eligiible for vote")

# 7. Student Pass/Fail Based on All Subjects >= 35
maths=40
phy=36
chemistry=30
if(maths>=35 and phy>=35 and chemistry>=30):
    print("pass")
else:
    print("fail")

# 8. Student Pass if Passed Any One Subject (>= 35)
maths=20
phy=38
chem=25
if(maths>=20 or phy>=38 or chem>=25):
    print("pass")
else:
    print("fail")

# 12. Perfect Square or Not
a=7
s=a*a
print(s)

a=2025
if(a%100==0 and a%400!=0):
    print("leap year")
else:
    print("not leap year")



