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
    def __init__(self,author_name,author_age,nationality):
        self.author_name=author_name
        self.author_age=author_age
        self.nationality=nationality

def particular_author_written_book(author_obj,author_name):
        count=0
        for author in range(len(author_obj)):
            if(author_obj[author].author_name==author_name.lower()):
                count=count+1
        print("The number of books written by",author_name,"-",count)

def print_total_cost_of_all_book(book_obj):
    price=0
    for object in range(len(book_obj)):
        price=price+book_obj[object].book_price
    print("The total cost of all the books in the store :",price)

def print_author_book_name(book_obj,author_obj):
    book_list=[]
    author_list=[]
    book_and_author_dict = {}
    print("The book name and author name of all affordable books: ")
    for book in range(len(book_obj)):
        book_list.append(book_obj[book].book_name)
    for author in range(len(author_obj)):
        author_list.append(author_obj[author].author_name)
    book_and_author_dict=dict(zip(book_list,author_list))
    for book in range(len(book_obj)):
        affordable_book=book_obj[book].is_affordable()
        for key in book_and_author_dict:
            if(affordable_book==key):
                print(key,"-",book_and_author_dict[key])


b1=Book("python",999)
b2=Book("scala",1500)
b3=Book("java",800)
b4=Book("c",1999)
b5=Book("c++",1499)
b6=Book("Generic java",599)

a1=Author("guido van rossum",64,"dutch")
a2=Author("martin odersky",61,"german")
a3=Author("james gosling",65,"canadian")
a4=Author("dennis ritchie",79,"american")
a5=Author("bjarne stroustrup","69","danish")
a6=Author("martin odersky",61,"german")


author_obj=[a1,a2,a3,a4,a5,a6]
book_obj=[b1,b2,b3,b4,b5,b6]
print_total_cost_of_all_book(book_obj)
particular_author_written_book(author_obj,"guido van rossum") #just pass author name
print_author_book_name(book_obj,author_obj)
