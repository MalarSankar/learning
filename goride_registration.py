import re
class CarDetails:
    def __init__(self,car_category,car_number,color,company,model):
        self.car_category=car_category
        self.car_number=car_number
        self.color=color
        self.company=company
        self.model=model

class DriverDetails:
    def __init__(self,driver_name,driver_age,license_number,license_validity,car_category,car_number,color,company,model):
        self.driver_name=driver_name
        self.driver_age=driver_age
        self.license_number=license_number
        self.license_validity=license_validity
        self.car_obj=CarDetails(car_category,car_number,color,company,model)
    def confirmation(self):
        print("Succesfully Registered!!")
def registration():
    print("##############Welcome to Goride#########")
    name=input("Enter driver/owner name:")
    age=int(input("Enter age of owner/driver:"))
    while True:
        license_num=input("Enter license number:")
        if re.match("^(([A-Z){2}[0-9]{2})()|([A-Z]{2}-[0-9]{2}))((19|20)[0-9][0-9])[0-9]{7}$",license_num):
            break
        else:
            print("enter valid license number")
    license_validity=input("Enter license validity period:")
    print("micro accomodate maximum of upto 4 people")
    print("xl accomodate maximum of upto 10 people:")
    car_category=input("Enter car category micro/xl:")
    car_number=input("Enter car number:")
    color=input("Enter car color:")
    company=input("Enter car company:")
    model=input("Enter car model:")
    driver=DriverDetails(name,age,license_num,license_validity,car_category,car_number,color,company,model)
    driver.confirmation()
registration()