# check if the book exists

CollectionOfBooks = ["book1", "book2", "book3" ]
Userbook = (input("enter the name of the book : "))
for book in CollectionOfBooks:
    if book == Userbook:
        print("Yes, i have that book")
        break
else:
    print("No, i do not have that book")
