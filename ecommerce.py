class product:
    def __init__(self,id,name,price,stock):
        self.id=id
        self.name=name
        self.price=price
        self.stock=stock

    
    def update_stock(self,quantity):
        self.stock+=quantity
        print(f'Stock value is changed to {self.stock}')
        print("Successfully updated...")

    def apply_discount(self,discount):
        self.price-=self.price*(discount/100)
        print(f'After discounting the price will be {self.price}')

    


    
       