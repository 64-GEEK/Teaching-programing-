
"""patient_Name="John Smith"
age=20
status="New Patient"
print(patient_Name,age,status)"""


#2
"""name=input("what is your name? ")
print("Hello " + name)


array = ["Ahmed", "Mohamed", "Hassan", "ahmed"]

'''array[1] = "Hussien"
print(array[0:3])

al = ['Khaled']

array.extend(al)

array.append("Mohsen")

array.insert(1, "mahmoud")

array.remove("Ahmed")
array.clear()
array.pop()
print(array.count("Ahmed"))

array.sort()'''

cat = array.copy()
print(cat)"""
#Converting data types
"""num1=(input("Enter the first number "))
num2=(input("Enter another number "))
sum=float(num1)+float(num2)
print("sum: "+str(sum))"""


# string formating
"""name=input("what's your name? ")
print("Hello %s " % name)"""

"""# change this code
number = 16
second_number = 0
first_array = [1,2,3]
second_array = [1,2]

if number > 15:
    print("1")

if first_array:
    print("2")

if len(second_array) == 2:
    print("3")

if len(first_array) + len(second_array) == 5:
    print("4")

if first_array and first_array[0] == 1:
    print("5")

if not second_number:
    print("6")
    
    # Define our 3 functions
def my_function():
    print("Hello From My Function!")

def my_function_with_args(username, greeting):
    print("Hello, %s, From My Function!, I wish you %s"%(username, greeting))

def sum_two_numbers(a, b):
    return a + b

# print(a simple greeting)
my_function()

#prints - "Hello, John Doe, From My Function!, I wish you a great year!"
my_function_with_args("John Doe", "a great year!")

# after this line x will hold the value 3!
x = sum_two_numbers(1,2)"""
"""num1=int(input("enter the first num"))
num2=int(input("enter the num2"))
print(str(num1+num2))
def sum(num1, num2):
    return num1+num2

print(str(sum(num1,num2)))"""
#Next
"""# Modify this function to return a list of strings as defined above
def list_benefits():
    return ["More organized code", "More readable code", "Easier code reuse", "Allowing programmers to share and connect code together"]

# Modify this function to concatenate to each benefit - " is a benefit of functions!"
def build_sentence(benefit):
    return "%s  is a benefit of functions!"%benefit

def name_the_benefits_of_functions():
    list_of_benefits = list_benefits()
    for benefit in list_of_benefits:
        print(build_sentence(benefit))

name_the_benefits_of_functions()"""
#Numbers الأرقام

"""from math import * #to import from a library and(*)means all
mynum=5
print( round(sqrt(mynum))) #جذر ثم تقريب
print(floor(mynum))#تخفيض
print(ceil(mynum))#رفع
print(pow(mynum,2))#رفع لأس 2
print(max(mynum,6))#اختيار الأكبر من بين مجموعة
print(min(mynum,6))#اختيار الأصغر من بين مجموعة """
#Calculator 1 آلة حاسبة
"""num1=input("First: ")
num2=input("Second: ")
result= float(num1) + float(num2)
print("The sum is: "+str(result))"""
#Mad libs
"""color=input("Enter the color ")
plural_noun=input("Enter the character ")
adjective=input("Enter the adjective ")
print("Trees are %s"%(color))
print("%s are mean"%(plural_noun))
print("Please keep it %s"%(adjective))"""
#Lists القوائم
"""My_list=["mohamed","saif","malak",[1,"Mentor"]]
print(My_list[0])
print(My_list[1])
print(My_list[2])
print(My_list[3][0])#prints 0 from 3
print(My_list[3][1])#Prints 1 from 3
print(My_list[-1])#العد يبدأ بالعكس مع السالب
print(My_list[1:3])#1,2
print(My_list[:3])#0,1,2
print(My_list[2:])#2,3
My_list[0]="Hatem"#Changeing "mohamed" with "Hatem"
print(My_list[0])#prints the new value in 0
your_list=["Tarek",122,"Hosam","Ali","Hamada"]
My_list.extend(your_list)#lists concatination
print(My_list)#prints the items in My_list followed by the items in your_list
My_list+=your_list#another method
My_list=My_list+your_list#third method
My_list.append("Talal")#Add items after the last item
My_list.insert(0,"3la2")#Add items any where you want
print(My_list)
My_list.remove("saif")#removes a certain item
print(My_list)
your_list.clear()#Remove all the items in the list
print(your_list)#It's wipped out!
print(My_list)#My_list is still have the items in your_list
what_was_poped=My_list.pop()#Removes the last item and stores it in the variable what_was _poped
print(My_list.index(122))#prints the place of the item in the list
police_num=My_list.index(122)# stores the previous place in this variable(5)
print(My_list.count(122))#prints the number of 122s in the list
their_list=["bannanas","apples","chocolates"]
their_list.sort()#Alphabetically sort the array of the same data type(string)
print(their_list)
our_list=[36,100,1]
our_list.sort()# ترتيب تصاعدي للأرقام
print(our_list)
print(My_list)
print(My_list.copy())#this is a shallow copy 
The_copy=My_list #Any impact we apply happens to The_copy not My_list"""
#Tuples الصفوف
"""coordinates=(-5,3)#Tuples are fixed(can't be changed after being written)
print(coordinates[0])#prints -5
list_of_tuples=[(1,2),("Cream","Milk","Sugar"),(1,"bananas")]
print(list_of_tuples[2][1])#prints bananas"""
#Functions الدوال
"""def say_hi(name,age):
    print("Hi "+name+" your age is "+str(age))
say_hi("Mohamed",19)

def Cube(num):
    print(pow(num,3))
    
Cube(6)

def cube(num):
    return(num*num*num)
print(cube(3))
result=cube(4)#to save the result that the function cube returned"""
#CONDITIONALS الأدوات الشرطية
"""am_hungry=True
wants_to_eat=False
if(am_hungry and wants_to_eat):
    print("you're hungry and you wanna eat.")
elif(not am_hungry or wants_to_eat):
    print("You're either hungery or you wanna eat.")
else:
    print("You're neither hungery nor wanna eat.")"""
# Comparisons المقارنات
"""num1=1
num2=2
num3=3
if(num1>num2 and num2>num3):
    print("%x is the highest number")
elif(num2>num1 and num1>num3):
    print(str(num2)+" is the highest number.")
else:
    print("%s is the highest number."%num3)"""
#Calculator 2
"""num1=float(input("Please enter the first number: "))
operator=input("Please enter the operator: ")
num2=float(input("Please enter the second number: "))
if(operator=='+'):
    print(num1+num2)
elif(operator=='-'):
    print(num1-num2)
elif(operator=='*'):
    print(num1*num2)
elif(operator=='/'):
    print(num1/num2)
else:
    print("Invalid operator!")"""
# Dictionaries القواميس
"""convert_month={
    #key : value
    "Jan":"January",
    "Feb":"Febraury",
    "Mar":"March",
    "list":["bananas",4],
    1:1917,
    2:"Hope is the key!"
}
print(convert_month["Mar"])
print(convert_month.get("Jan","enta bthazar yabo sala7!"))
print(convert_month.get("list"))
print(convert_month[1])
print(convert_month.get(2))"""

#Inheritance
"""class parent:
    def __init__(self):
        print("This is the parent class")
    def parentFunc(self):
        print("This is is the parent func")
p= parent()
p.parentFunc()

class Child(parent):
    def __init__(self):
        print("this is the child class")
    def childFunc(self):
        print("this is the child function")
c=Child()
print(c)
c.parentFunc()"""

