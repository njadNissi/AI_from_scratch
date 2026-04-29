from item import Item

class Phone(Item): #Phone inherits froom Item
    def __init__(self, name: str, price: float, quantity=0, broken_phones=0):
        #Call to super function for access to all attributes && /methods
        super().__init__(name, price, quantity)
 
        #Run validations to the received attributes
        assert broken_phones >= 0, f"broken_phones can't be < 0!"

        #Assign to self object
        self.broken_phones = broken_phones