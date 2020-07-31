class Vehicle:
    def __init__(self, type, ac):
        self.__type = type
        self.__ac = ac

    def get_type(self):
        return self.__type

    def is_with_ac(self):
        return self.__ac


class Auto(Vehicle):
    def __init__(self, type, range, price, ac):
        self.__range = range
        self.__price = price
        super().__init__(type, ac)

    def get_range(self):
        return self.__range

    def get_price(self):
        return self.__price


class Micro(Vehicle):
    def __init__(self, type, range, price, ac):
        self.__range = range
        self.__price = price
        super().__init__(type, ac)

    def get_range(self):
        return self.__range

    def get_price(self):
        return self.__price


class XL(Vehicle):
    def __init__(self, type, range, price, ac):
        self.__range = range
        self.__price = price
        super().__init__(type, ac)

    def get_range(self):
        return self.__range

    def get_price(self):
        return self.__price


def is_valid_category(type):
    category_list = []
    filtered_categories = []
    for category in categories:
        category_list.append(category.get_type().lower())
        if type == category.get_type().lower():
            filtered_categories.append(category)
    if type in category_list:
        return True, filtered_categories
    else:
        return False, filtered_categories


def is_option_available(filtered_categories, with_ac_or_not):
    option_list = []
    for filtered_category in filtered_categories:
        option_list.append(filtered_category.is_with_ac().lower())
    if with_ac_or_not in option_list:
        return True
    else:
        return False


def display_price(filtered_categories, with_ac_or_not):
    print("Range(km)    price/km")
    if with_ac_or_not == "yes":
        for option in filtered_categories:
            if option.is_with_ac() == "yes":
                print(option.get_range(), ":    ", option.get_price())
    else:
        for option in filtered_categories:
            if option.is_with_ac() == "no":
                print(option.get_range(), ":      ", option.get_price())
    print("Thanks for riding with us!")


def book_ride():
    while True:
        type = input("select any one of the above category : ")
        (is_available, filtered_categories) = is_valid_category(type.lower())
        if is_available:
            break
        else:
            print("please enter a valid category")

    while True:
        with_ac_or_not = input("Do you want ac? (yes/no) : ")
        selection = is_option_available(filtered_categories, with_ac_or_not.lower())
        if selection:
            break
        else:
            print("Option not available,please select another option !")
    display_price(filtered_categories, with_ac_or_not.lower())


auto1 = Auto("auto", [0, 15], 10, "yes")
auto2 = Auto("auto", [16, 30], 8, "yes")
auto3 = Auto("auto", [31, 1000], 15, "yes")

micro1 = Micro("micro", [0, 15], 12, "yes")
micro2 = Micro("micro", [16, 1000], 10, "yes")
micro3 = Micro("micro", [0, 15], 14, "no")
micro4 = Micro("micro", [16, 1000], 12, "no")

xl1 = XL("xl", [0, 15], 14, "yes")
xl2 = XL("xl", [16, 1000], 14, "yes")
xl3 = XL("xl", [0, 15], 15, "no")
xl4 = XL("xl", [16, 1000], 15, "no")

categories = [auto1, auto2, auto3, micro1, micro2, micro3, micro4, xl1, xl2, xl3, xl4]
print(
    "Welcome to GoRide!\n Auto : can accomodate upto 3 peole\n Micro : can accomodate upto 4 people\n XL : can accomodate upto 10 people")

book_ride()



