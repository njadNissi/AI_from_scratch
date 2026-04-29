#default value function
def print_sex(sex="unknown"):
    if sex == "M":
        sex = "Male"
    elif sex == "F":
        sex = "Female"
    print("sex is", sex)

#print_sex("M")
#print_sex("F")
#print_sex()

#keyword arguments function
def print_sentence(subject="AnJie", verb="ate", complement="mango"):
    print(subject, verb, complement)

#print_sentence()
#print_sentence(subject="Ben")
#print_sentence(verb="went", complement="to school")

#flexible arguments function
def adder(*args):
    sum = 0
    for a in args:
        sum += a
    print('sum of ', args, ' = ', sum)    

#adder(1, 2, 5, -9)


#argument unhacking
def search_with(name, age, height):
    print('name = ', name, ', age = ', age, ', height = ', height)

lixiang = ['LiXiang', 21, 1.67]
search_with(*lixiang)


groceries = ['milk', 'bread', 'meat']
def cart(item):
    if item in groceries:
        print('Milk already baught!')
    else:
        groceries.append(item)

cart('vegetable')
cart('meat')
print(groceries)