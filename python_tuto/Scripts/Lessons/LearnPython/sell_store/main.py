from item import Item

#Item.instantiate_from_csv()
#print(Item.all)

#print('7.5 is intger = ', Item.is_integer(7.5)) 

#phone1 = Phone("jscPhonev10", 500, 5, 1)
#print(phone1.calculate_total_price())
#phone2 = Phone("jscPhonev20", 700, 5, 1)

item1 = Item("MyItem", 750)
item1.apply_increment(0.2)
item1.apply_discount()
print(item1.name, item1.price)
