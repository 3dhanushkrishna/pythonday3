count_of_books = int(input("Enter the num of books? "))
book_name = []
author_name = []
book_price = []
publisher_name = []
Book_details = {"Book name":book_name,"Author name":author_name,"Book Price":book_price,"Publisher name":publisher_name}
for i in range (0, count_of_books):
    bk_name = input("Enter the name of the book? ")
    aut_name = input("Enter the author name of the book? ")
    bk_price = int(input("Enter the price of the book? "))
    pb_name = input("Enter the publishers name? ")
    book_name.append(bk_name)
    author_name.append(aut_name)
    book_price.append(bk_price)
    publisher_name.append(pb_name)
print(Book_details)

