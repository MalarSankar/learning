class Ice_Cream:
    def __init__(self,type,flavour):
        self.ice_type=type
        self.ice_flavour=flavour
        self.ice = []
        self.rupee = []
        self.ice_dict={}
    def print_menu_card(self):
        print("***********MENU CARD************")
        for flavour in self.ice_flavour:
            for type in self.ice_type:
                ice_cream_name = flavour + " " + type
                self.ice.append(ice_cream_name)
                print("      ", flavour, type, "-", end=" ")
                ice_cream_cost = self.ice_flavour[flavour] + self.ice_type[type]
                self.rupee.append(ice_cream_cost)
                print(self.ice_flavour[flavour] + self.ice_type[type])
        print("************XXXXXXX************")
        self.ice_dict = (dict(zip(self.ice, self.rupee)))

class Topping:
    def __init__(self,topping_options):
        self.topping_options=topping_options
    def print_topping(self):
        print("************Toppings**********")
        for toppin in self.topping_options:
            print("        ",toppin," - ",self.topping_options[toppin])
    def toppin_total_cost(self,order,quantity):
        top = input("Do you want toppings, enter yes/no:")
        if (top == "yes"):
            top_in = input("select topping:")
            for keys in t1.topping_options:
                if (top_in == keys):
                    for key in s1.ice_dict:
                        if (order == key):
                            print("the cost of ", key, "-",
                                  quantity * s1.ice_dict[key] + t1.topping_options[keys] * quantity)
        else:
            print_and_display_total_cost(order, quantity)


def print_and_display_total_cost(order,quantity):
    for key in s1.ice_dict:
        if (key == order):
            print("The cost of",key,":",quantity*s1.ice_dict[key])


def toppin_calculation(order,quantity):
        t1.print_topping()
        t1.toppin_total_cost(order,quantity)

def takes_order(order,quantity):
    if(order[0:9]=="chocolate"):
        toppin_calculation(order,quantity)
    else:
        print_and_display_total_cost(order,quantity)


s1=Ice_Cream({"cup":10,"stick":15,"cone":20},{"chocolate":30,"vanila":25,"strawberry":35})
t1=Topping({"choco chips":20,"caramel":10,"nuts":20})
s1.print_menu_card()
takes_order(input("enter favorite ice cream:"),int(input("enter quantity:")))
