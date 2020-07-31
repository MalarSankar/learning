import re
class Car:
    def __init__(self,car_category,car_number,color,company,model):
        self.car_category=car_category
        self.car_number=car_number
        self.color=color
        self.company=company
        self.model=model

class Driver:
    def __init__(self,driver_name,driver_age,license_number,license_validity,car_category,car_number,color,company,model):
        self.driver_name=driver_name
        self.driver_age=driver_age
        self.license_number=license_number
        self.license_validity=license_validity
        self.car_obj=Car(car_category,car_number,color,company,model)
    def confirmation(self):
        print("Succesfully Registered!!")
def registration():
    print("##############Welcome to Goride#########")
    name=input("Enter driver/owner name:")
    age=int(input("Enter age of owner/driver:"))
    while True:
        license_num=input("Enter license number:")
        if re.match(r"([A-Z]{2}[0-9]{2})((19|20)[0-9][0-9])([0-9]{7})",license_num):
            break
        else:
            print("enter valid license number")
    while True:
        license_validity=input("Enter license validity period:")
        if re.match(r"(0[1-9]|[12][0-9]|3[01])[-](0[1-9]|1[012])[-](202[1-9])",license_validity):
            break
        else:
            print("enter valid period")
    print("micro accomodate maximum of upto 4 people")
    print("xl accomodate maximum of upto 10 people:")
    car_category=input("Enter car category micro/xl:")
    car_number=input("Enter car number:")
    color=input("Enter car color:")
    company=input("Enter car company:")
    model=input("Enter car model:")
    driver=Driver(name,age,license_num,license_validity,car_category,car_number,color,company,model)
    driver.confirmation()
registration()
