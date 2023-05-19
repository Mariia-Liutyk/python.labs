class Shop:
    def __init__(self, shop_name, store_type ):
        self.shop_name = shop_name
        self.store_type = store_type
        self.number_of_units = 0
    def describe_shop(self):
        print(f'Shop name: {self.shop_name}')
        print(f'Store type: {self.store_type}')
    def open_shop(self):
        print(f'The online store is open: {self.shop_name}')

    def set_number_of_units(self, units):
        self.number_of_units = units

    def increment_number_of_units(self, units):
        self.number_of_units += units


store = Shop("My Store", "Clothes")
print(store.shop_name)
print(store.store_type)

store.open_shop()
store.describe_shop()

shop1 = Shop("My Store 1", "Cake")
shop2 = Shop("My Store 2", "Food")
shop3 = Shop("My Store 3", "Electronics")

shop1.describe_shop()
shop2.describe_shop()
shop3.describe_shop()

print(store.number_of_units)

store.number_of_units = 15
print(store.number_of_units)

store.set_number_of_units(15)
print(store.number_of_units)

store.increment_number_of_units(10)
print(store.number_of_units)

class  Discount(Shop):
    def __init__(self, shop_name, store_type, discount_products):
        super().__init__(shop_name, store_type)
        self.discount_products = discount_products
    def get_discounts_products(self):
        print(f"Товари зі знижкою в {self.shop_name}:")
        for product in self.discount_products:
            print(product)

store_discount = Discount("ABC", "Grocery", ["Product 1", "Product 2", "Product 3"])
store_discount.get_discounts_products()