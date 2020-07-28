class Vechicle:
    def __init__(self, category, km_range, price_with_ac, price_with_nonac):
        self.catgory = category
        self.km_range = km_range
        self.price_with_ac = price_with_ac
        self.price_with_nonac = price_with_nonac
    def vechicle_details_with_ac(self):
        print(self.catgory,"          ",self.km_range,"         ",self.price_with_ac)
    def vechicle_detais_with_nonac(self):
        print(self.catgory,"           ",self.km_range,"          ",self.price_with_nonac)

class Auto(Vechicle):
    def __init__(self,category,km_range,price_with_ac,price_with_nonac):
        self.catgory=category
        self.km_range=km_range
        self.price_with_ac=price_with_ac
        self.price_with_nonac=price_with_nonac
        self.seat=3
    def price_calculation_ac(self,km):
        if(km<=15):
            return km*10
        elif(km>15 and km<=30):
            return km*8
        else:
            return km*15

class Micro(Vechicle):
    def __init__(self, category, km_range, price_with_ac, price_with_nonac):
        self.catgory = category
        self.km_range = km_range
        self.price_with_ac = price_with_ac
        self.price_with_nonac = price_with_nonac
        self.seat=4
    def price_calculation_ac(self,km):
        if(km<=15):
            return km*12
        else:
            return km*10
    def price_calculation_nonac(self,km):
        if(km<=15):
            return km*14
        else:
            return km*12

class Xl(Vechicle):
    def __init__(self, category, km_range, price_with_ac, price_with_nonac):
        self.catgory = category
        self.km_range = km_range
        self.price_with_ac = price_with_ac
        self.price_with_nonac = price_with_nonac
        self.seat=10
    def price_calculation_ac(self,km):
        if(km<=15):
            return km*14
        else:
            return km*14
    def price_clculation_nonac(self,km):
        if(km>15):
            return km*15
        else:
            return km*15

a1=Auto("auto","upto 15km","10/km","na")
a2=Auto("auto","15-30km","8/km","na")
a3=Auto("auto","30 and above","15/km","na")

m1=Micro("micro","upto 15km","12/km","14/km")
m2=Micro("micro","15 and above","10/km","12/km")

x1=Xl("xl","upto 15km","14/km","15/km")
x2=Xl("xl","15 and above","14/km","15/km")

vech_obj=[a1,a2,a3,m1,m2,x1,x2]
def get_user_preference():
        selected_category = input("enter your category [micro/auto/xl]: ").lower()
        selected_ac_or_nonac=input("enter do you want ac/non ac:").lower()
        return selected_category,selected_ac_or_nonac

def price_menu(selcted_category,selected_ac_or_nonac,vech_obj):
    print("Category        KM Range            Price")
    for obj in range(len(vech_obj)):
        if(selcted_category==vech_obj[obj].catgory):
            if(selected_ac_or_nonac=="ac"):
                vech_obj[obj].vechicle_details_with_ac()
            else:
                vech_obj[obj].vechicle_detais_with_nonac()

def total(selected_category,selected_ac_or_nonac,km,vech_obj):
    print("Total amount for ride:",end="")
    if(selected_ac_or_nonac=="ac"):
        for obj in range(len(vech_obj)):
            if(vech_obj[obj].catgory==selected_category):
                print(vech_obj[obj].price_calculation_ac(km))
                break
    else:
        for obj in range(len(vech_obj)):
            if(vech_obj[obj].catgory==selected_category):
                print(vech_obj[obj].price_calculation_nonac(km))
                break

(selected_category,selected_ac_or_nonac)=get_user_preference()
price_menu(selected_category,selected_ac_or_nonac,vech_obj)
km=int(input("enter km range:"))
total(selected_category,selected_ac_or_nonac,km,vech_obj)
print("Successully Booked!!")




