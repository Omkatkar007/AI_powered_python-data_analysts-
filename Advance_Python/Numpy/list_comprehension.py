''' list comprehension is a one line shortcut for creating a new list keeping over an exisitng one 

example'''

numbers = [ 1,2,3,4,5]
squared = []
for x in numbers:
    squared.append(x*x)    #traditional way

squared = [x*x for x in numbers]    
print(squared) # list comprehesnion



# filtering data 
numbers = [1,2,3,4,5]
even_no = [x for x in numbers if x%2==0]
print(even_no)




# transforming  text data
names = ["hArry","joHn","pAul","Reorge","Ringo"]
clean_names = [names.lower().strip() for names in names]
print(clean_names)


# dictionary comprehension
items = ['spam', 'eggs', 'bacon', 'spam', 'eggs', 'ham', 'bacon']
prices=[1.99, 2.99, 3.99, 4.99, 5.99, 6.99, 7.99]
price_dict = {items:prices for items,prices in zip(items,prices)}
print(price_dict)



# set comprehension
values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
unique_squares = {x*x for x in values }
print(unique_squares)


#nested list comprehension
pair = [(x,y) for x in [1,2] for y in [3,4]]
print(pair)