class Book:
    def __init__(self,book_name,book_price):
        self.book_name=book_name
        self.book_price=book_price

    def is_affordable(self):
        if(self.book_price<1000):
            return self.book_name
    def is_expensive(self):
        if(self.book_price>1000):
            return (self.book_name)


class Author:
    def __init__(self,author_name,author_age,nationality,book_name,book_pice):
        self.author_name=author_name
        self.author_age=author_age
        self.nationality=nationality
        self.book_obj=Book(book_name,book_pice)

def particular_author_written_book(author_obj,author_name):
        count=0
        for author in range(len(author_obj)):
            if(author_obj[author].author_name==author_name.lower()):
                count=count+1
        print("The number of books written by",author_name,"-",count)

def print_total_cost_of_all_book(author_obj):
    price=0
    for object in range(len(author_obj)):
        price=price+author_obj[object].book_obj.book_price
    print("The total cost of all the books in the store :",price)

def print_author_book_name(author_obj):
    print("The book name and author name of all affordable books: ")
    for author in range(len(author_obj)):
        affordable_book=author_obj[author].book_obj.is_affordable()
        if(affordable_book==author_obj[author].book_obj.book_name):
            print(affordable_book,author_obj[author].author_name)



a1=Author("guido van rossum",64,"dutch","python",999)
a2=Author("martin odersky",61,"german","scala",1500)
a3=Author("james gosling",65,"canadian","java",800)
a4=Author("dennis ritchie",79,"american","c",1999)
a5=Author("bjarne stroustrup","69","danish","c++",1499)
a6=Author("martin odersky",61,"german","generic java",599)


author_obj=[a1,a2,a3,a4,a5,a6]
print_total_cost_of_all_book(author_obj)
particular_author_written_book(author_obj,"guido van rossum") #just pass author name
print_author_book_name(author_obj)
