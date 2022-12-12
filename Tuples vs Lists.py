#Creating  items in tuples
person = ('Candace Hollinger', 37, "555-555-5555")
person2 = ('John Hollinger', 78, '')
person[0]
'Candace Hollinger'
person2[0]
'John Hollinger'
Putting a list in a tuple
my_list = [1, 2, 3]
my_tuple = (my_list, 1)
my_tuple
([1, 2, 3], 1)

#Modifying a tuple in a list
my_list.append(1)
my_tuple
([1, 2, 3, 1], 1)
