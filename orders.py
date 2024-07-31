from ecommerce import product

class order:
    def __init__(self,order_id,product,quantity):
        self.order_id=order_id
        self.product=product 
        self.quantity=quantity
        self.flag="pending"

    def process_order(self):
        if self.product.stock >= self.quantity:
            self.product.update_stock(-self.quantity)
            self.flag="processing"
            print(f'order of {self.product.name} is placed...')
        else:
            print("Out of stock!!")

    def cancel_order(self):
        if self.flag=="processing":
            self.product.update_stock(self.quantity)
        self.flag="cancelled"

        print(f'product with {self.name} is cancelled..')
