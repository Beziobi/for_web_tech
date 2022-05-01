#takes an age input 
age= int(input('please insert your age:'))
#prints out the age you entered
print(age)
#if condition that checks if your age is greater and equal with 18 and prints out id and if it`s `
if age>=18:
    print(f'{age} is an appropirate age please wait until we prepare it for you')
elif (age<18 ):
     print(f'please come back after {18-age} years')