class Payment:
    tax_repo = []

    def __init__(self, price, category, name):
        self.name = name
        self.price = price
        self.category = category

    def calculate_tax(self):
        if (self.category == "produce" and self.price >= 500) or (self.category == "homeneeds" and self.price >= 500):
            tax = self.price * (5 / 100)
            self.tax_repo.append(self.name)
            self.tax_repo.append(tax)
            return tax
        elif (self.category == "produce" and self.price < 500) or (self.category == "homeneeds" and self.price < 500):
            tax = (2 / 100) * (self.price)
            self.tax_repo.append(self.name)
            self.tax_repo.append(tax)
            return tax
        elif (self.category == "textile" and self.price >= 500):
            tax = (6 / 100) * (self.price)
            self.tax_repo.append(self.name)
            self.tax_repo.append(tax)
            return tax
        elif (self.category == "textile" and self.price < 500) or (self.category == "dairy" and self.price >= 1000):
            tax = (3 / 100) * (self.price)
            self.tax_repo.append(self.name)
            self.tax_repo.append(tax)
            return tax
        elif (self.category == "dairy" and self.price < 1000):
            self.tax_repo.append(self.name)
            self.tax_repo.append(0)
            return (0)
        else:
            pass

    def calculate_and_print_totalprice(self):
        total_price = self.price + self.calculate_tax()
        print("The price of", self.name, ":", total_price)


class Product(Payment):
    def __init__(self, price, category, name, id):
        self.id = id
        self.name = name.lower()
        self.price = price
        self.category = category.lower()
        Payment.__init__(self, price, category, name)


def object_access(object):
    object.calculate_and_print_totalprice()


number_of_proucts = int(input("enter number of products:"))
print("enter the product details one by one:")
object = []

for i in range(number_of_proucts):
    print("enter the detail of product:", i + 1, ":")
    id = input("enter the id of product:")
    name = input("enter the name of product:")
    price = float(input("enter the price of product:"))
    category = input("enter category of product:")
    object_id = Product(id=id, name=name, price=price, category=category)
    object.append(object_id)

for i in range(len(object)):
    object_access(object[i])

print("TAX REPOSITORY")
for i in range(len(Payment.tax_repo) - 1):
    if (i % 2 == 0):
        print(Payment.tax_repo[i], ":", Payment.tax_repo[i + 1])





