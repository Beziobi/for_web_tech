list_of_name =['alex','dave','aster']
list_of_nick_name=['al','d','ab']
#we can print the elements using the command below but the next one is more efficent
print(f'hello{list_of_name[0]}')
for single_element in list_of_name:
   print(single_element)
   for single_element in range (len(list_of_name)):
   print(list_of_name[single_element])
#the code will display all the list of names along with their nick names 
for single_element in range (len(list_of_name)):
       print(f'{list_of_name[single_element]} nickname is{list_of_nick_name[single_element]})