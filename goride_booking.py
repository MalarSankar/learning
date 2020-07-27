class Auto:
    def __init__(self,category,km_range,price_with_ac,price_with_nonac):
        self.catgory=category
        self.km_range=km_range
        self.price_with_ac=price_with_ac
        self.price_with_nonac=price_with_nonac
        self.seat=3

class Micro:
    def __init__(self, category, km_range, price_with_ac, price_with_nonac):
        self.catgory = category
        self.km_range = km_range
        self.price_with_ac = price_with_ac
        self.price_with_nonac = price_with_nonac
        self.seat=4

class Xl:
    def __init__(self, category, km_range, price_with_ac, price_with_nonac):
        self.catgory = category
        self.km_range = km_range
        self.price_with_ac = price_with_ac
        self.price_with_nonac = price_with_nonac
        self.seat=10

a1=Auto("auto","upto 15km","10/km","na")
a2=Auto("auto","15-30km","8/km","na")
a3=Auto("auto","30 and above","15/km","na")
auto_obj=[a1,a2,a3]

m1=Micro("micro","upto 15km","12/km","14/km")
m2=Micro("micro","15 and above","10/km","12/km")
micro_obj=[m1,m2]

x1=Xl("xl","upto 15km","14/km","15/km")
x2=Xl("xl","15 and above","14/km","15/km")
xl_obj=[x1,x2]

def get_user_preference():
        selected_category = input("enter your category [micro/auto/xl]: ").lower()
        selected_ac_or_nonac=input("enter do you want ac/non ac:").lower()
        return selected_category,selected_ac_or_nonac

def price_menu(selected_category,selected_ac_or_nonac,auto_obj,micro_obj,xl_obj):
    print("Category      Km Range           price")
    if(selected_category=="auto"):
        for obj in range(len(auto_obj)):
            if(selected_ac_or_nonac=="ac"):
                print(auto_obj[obj].catgory,"        ",auto_obj[obj].km_range,"         ",auto_obj[obj].price_with_ac)
                price_list.append(auto_obj[obj].price_with_ac.replace('/km',''))
            else:
                print(auto_obj[obj].catgory,"        ",auto_obj[obj].km_range, auto_obj[obj].price_with_nonac)
                price_list.append(auto_obj[obj].price_with_nonac.replace('/km', ''))
    elif(selected_category=="micro"):
        for obj in range(len(micro_obj)):
            if(selected_ac_or_nonac=="ac"):
                print(micro_obj[obj].catgory, "        ", micro_obj[obj].km_range, "         ",micro_obj[obj].price_with_ac)
                price_list.append(micro_obj[obj].price_with_ac.replace('/km', ''))
            else:
                print(micro_obj[obj].catgory, "        ", micro_obj[obj].km_range,"      ", micro_obj[obj].price_with_nonac)
                price_list.append(micro_obj[obj].price_with_nonac.replace('/km', ''))

    else:
        for obj in range(len(xl_obj)):
            if (selected_ac_or_nonac == "ac"):
                    print(xl_obj[obj].catgory, "        ", xl_obj[obj].km_range, "         ",xl_obj[obj].price_with_ac)
                    price_list.append(xl_obj[obj].price_with_ac.replace('/km', ''))
            else:
                print(xl_obj[obj].catgory, "        ", xl_obj[obj].km_range,"         " ,xl_obj[obj].price_with_nonac)
                price_list.append(xl_obj[obj].price_with_nonac.replace('/km', ''))

def total_cost(list2,category,km):
    print("Total cost for ride:",end="")
    if(category=="auto"):
        if(km<=15):
            print(km*int(list2[0]))
        elif(km>15 and km<=30):
            print(km*int(list2[1]))
        else:
            print(km*int(list2[2]))
    else:
        if(km<=15):
            print(km*int(list2[0]))
        else:
            print(km*int(list2[1]))

price_list=[]
(selected_category,selected_ac_or_nonac)=get_user_preference()
price_menu(selected_category,selected_ac_or_nonac,auto_obj,micro_obj,xl_obj)
print("Confirm your ride:")
category=input("select category from the above:")
km=int(input("enter distance in km:"))
total_cost(price_list,category,km)
print("successfully booked!!")



