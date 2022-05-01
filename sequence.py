#list is an ordered sequence of items.
from multiprocessing import set_forkserver_preload


list_of_numbers=[1,2,3,4,5]
#the command below will print 2 since it`s found on index 1
print(list_of_numbers=[1])
#the command below will list elements from index 1 to 3 but doesn`t include the 4th element`

print ( list_of_numbers= [1:3])
#the cmd below assigns the value 4 for the 4th value
list_of_numbers[3]=4
#the cmd below will add the value 90 at the end
list_of_numbers.append(90)

#tuple is an ordered sequence of items like lists but it is immutable (difficult to change elements)
tuples_of_numbers=(1,2,3,4,5,6)
#set uses unique values and is an unordered collection
set_of_numbers= {1,2,3}
#we can also write it as:

set_of_numbers={1,2,3}
print(type (set_of_numbers))
#len shows us the length of the elements
print(len(set_of_numbers))
#a dictionary is unordered collection of unique items
number_dict = {'name':'abebe', 'age':30,'gender' :'male'}
#below shows as the name element of the dict
print(number_dict['name'])