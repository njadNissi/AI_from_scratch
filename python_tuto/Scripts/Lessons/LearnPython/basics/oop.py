a = 5.4
b = int(a) + 1  # casting
c = a * b
print('5 * 2 = ' + str(c))
print('5 * 2 =', c)

c1 = complex(4+2j)
c2 = complex(-1-3j)
print(c1+c2)

hello = 'Hello'
bobby = 'Bobby'
welcome = 'Welcome'

print(hello, welcome, ' to ', bobby)

# print datatype of the passed var
print(type(hello), type(c))

##########################


class Item:
    def calculate_total_price(self, x, y):
        return x * y


item1 = Item()
item1.name = "Phone"
item1.price = 100
item1.quantity = 5
print(item1.calculate_total_price(item1.price, item1.quantity))

for item in Item.all:
    print(item.name)

    # instant method: run by instancen -receives self as param
    # class method: run by class -receives cls as param
    # static method: -receives normal var as param
    # magic method: __methodName__

    # pass : avoind having error for a not defined class body, function etc...
    # print(ClassName__dic__) display all class attributes

    # private attribute : read-only-property;

    # @property => getter method
    # def name(self):
     # return self._name

    # @name.setter => setter methodabstraction
    # def name(self, value):
     # self.__name = value

     # to make a method private or abstract or encapsulated
     # just add a double underscores before the name

     # list : multiple elements of different type||MUTABLE
     my_list = [1, [2, 3], 4.0, "hi", 2]
      # .append for adding and .pop for removing last and remove(element)
      # .count(element)
      my_list[0:2] = []
       # define list : multiple elements of same type
       # age = "my age"
       # my_list = ["name", age]
       # new_list = my_list.copy()
       if "hi" in my_list:
            print("there is hi!")

        # tuple : ||IMMUTABLE
        tup1 = ("xyz", 123, "abc")

        # set: ||UNORDERDED and NO REPETITION ALLOWED
        my_set = {'xyz', 123, "abc"}

        # in terminal: pip install thing_to_install

        # Function Binary to Decimal number
          # def binaryToDecimal(val):
          # return int(val, 2)

        # country = input('where are you from?: ') #read keyboard
