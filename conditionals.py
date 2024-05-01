# write a python program that:
# 1.creates a list named 'bookshelf'
# 2. add the above book titlesto the 'bookshelf' list
# 3.print out the 'bookshelf' list to see the books you have added

# The book you want to place on your bookshelf are:
# "Harry Poter"
# "Lord of the rings"
# "the hobbit"

# bookshelf = ["Harry Poter", "Lord of the Rings", "The Hobbit"]
# bookshelf.append("My love")
# print(bookshelf)

# check if they are the same or different
bookshelf_A=["Harry Poter", "Lord of the Rings", "The Hobbit"]
# bookshelf_B=["Harry Poter", "Lord of the Rings", "The Hobbit"]
bookshelf_A.insert(1,"Pride and Prejudice")
bookshelf_A[bookshelf_A.index("The Hobbit")]="The Hobbit:Illustrated Edition"
bookshelf_A.remove("Lord of the Rings")
print(bookshelf_A)


# if bookshelf_A is bookshelf_B:
#     print("the are the same")
# else:
#     print("the bookshelf are different")

# main_shelf = ["Harry Poter", "Lord of the Rings", "The Hobbit"]