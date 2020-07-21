class Ice:

    def __init__(self):
        self.ice_types={"stick":50,"cone":70,"cup":40}
        self.ice_flavours={"chocolate ":55,"vanila ":30,"strawberry ":46}
        self.toppings={"choco chips":40,"caramel":30,"nuts":60}
        self.ice=[]
        self.rupee=[]
        self.ice_dict={}


    def print_and_display_menu(self):
        print("***********MENU CARD************")
        for flavour in self.ice_flavours:
            for type in self.ice_types:
                ice_cream_name=flavour+type
                self.ice.append(ice_cream_name)
                print("      ",flavour+type,"-",end="")
                ice_cream_cost=self.ice_flavours[flavour]+self.ice_types[type]
                self.rupee.append(ice_cream_cost)
                print(self.ice_flavours[flavour]+self.ice_types[type])
        print("************XXXXXXX************")
        self.ice_dict=(dict(zip(self.ice,self.rupee)))


    def print_and_display_total_cost(self,order,quantity):
            for key in self.ice_dict:
                if(key==order):
                    print("the cost of ",key,"-",quantity*self.ice_dict[key])

    def topping(self,order,quantity):
        print("***********TOPPINGS************")
        for key in self.toppings:
            print(key,"-",self.toppings[key])
        top=input("Do you want toppings, enter yes/no:")
        if(top=="yes"):
            top_in=input("select topping:")
            for keys in self.toppings:
                if(top_in==keys):
                    for key in self.ice_dict:
                        if (order==key):
                            print("the cost of ", key, "-", quantity * self.ice_dict[key] + self.toppings[keys] * quantity)
        else:
            self.print_and_display_total_cost(order,quantity)

    def take_order(self,order,quantity):
        if(order[0:9]=="chocolate"):
            self.topping(order,quantity)
        else:
           self.print_and_display_total_cost(order,quantity)


i1=Ice()
i1.print_and_display_menu()
i1.take_order(input("enter your favourite ice cream:"),int(input("enter quantity:")))