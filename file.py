num1 = 42 # variable declaration, number
num2 = 2.3 # variable declaration, floating-point number
boolean = True #Boolean
string = 'Hello World' #string 
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #variable declaration, list
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #variable declaration, dictionary, key value pair
fruit = ('blueberry', 'strawberry', 'banana') #variable declaration, tuple
print(type(fruit)) #print statement, tuple 
print(pizza_toppings[1]) #print statement, access value
pizza_toppings.append('Mushrooms') #list, add value
print(person['name']) #print statement, dictionary key 'name'
person['name'] = 'George' #initialize dictionary, add value (key value pair)
person['eye_color'] = 'blue' #initialize dictionary, add value (key value pair)
print(fruit[2]) #log statement, tuple at index 2

if num1 > 45: #conditional, if variable is greater than number
    print("It's greater") #log statement, string
else:                    #conditional, else
    print("It's lower") #log statement, string

if len(string) < 5: #conditional, if, length of string is greater than number
    print("It's a short word!") #log statement, string
elif len(string) > 15:# conditional, else if length of string is greater than number
    print("It's a long word!") #log statement, string 
else: #conditional, else
    print("Just right!") #log statement, string

for x in range(5): #for loop, variable 
    print(x) #logstatement, 
for x in range(2,5): #forloop, x=2; x<5 x++
    print(x) #logstatement
for x in range(2,10,3): #forloop, x=2; x<10; 3++
    print(x)#logstatement
x = 0 #
while(x < 5): #while x is less than 5
    print(x) #logstatement 
    x += 1 # x = x+1

pizza_toppings.pop() #remove pizza topping in last position 
pizza_toppings.pop(1)#remove pizza topping in index of 1

print(person) #logstatement variable 
person.pop('eye_color') #remove "eye_color"
print(person) #logstatement, eye color will not be shown

for topping in pizza_toppings: #for variable topping in variable pizza topping
    if topping == 'Pepperoni': #ifstatement topping  is equal to string
        continue # Continue 
    print('After 1st if statement') #logstatement  string
    if topping == 'Olives': #ifstatement variable equel to string  start sequence 
        break   #stop 

def print_hello_ten_times():#Function argument 
    for num in range(10): #forloop variable start sequence 
        print('Hello')      #print string x 10

print_hello_ten_times() #Unless given a parameter, it will just print hello 10 times 

def print_hello_x_times(x):#function, argument, parameter 
    for num in range(x): #start sequence
        print('Hello') #it will print hello by the number within x

print_hello_x_times(4)  #will print hello 4 times

def print_hello_x_or_ten_times(x = 10): #function argument oarameter (variable statement)
    for num in range(x): #for variable start sequence
        print('Hello') #logstatement x10

print_hello_x_or_ten_times() #argument, parameter () will not pass without a parameter
print_hello_x_or_ten_times(4) #argument, parameter () print 4 times. 


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)



fruits = ['apple', 'banana', 'orange', 'strawberry']
vegetables = ['lettuce', 'cucumber', 'carrots']
fruits_and_vegetables = fruits + vegetables
print(fruits_and_vegetables)
salad = 3 * vegetables
print(salad)






