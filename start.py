from math import factorial,pi ;

import random

print(dir(random))

print("Hi what's your name?");


first_name = input('Tell me your firstname  name please!:  ');
last_name = input("Tell me your lastname:  ");

name = first_name + last_name;
print(name,'is your name');


const = factorial(5)

print(const,'const');

print(type(4.0))
print(type(('4.0')))
print(int(4.0))
print(int(float('34.6')))
print(bin(4))
print(pi)

# '''long_string = ''' 
#     -
#    ---
#    ---
#   -----
#   -----
#  -------
#  -------
#  -------
#  ---------
# ''';

# print(long_string,'long string');'''


name = 'Abdullahi';
age = 23;

print('My name is {},i am {} years old....{}'.format('22','bola','lll'));

quote = 'to be or not to be';

res = quote.find('to')

const = False;
print(const ,'c')

print(complex(2+6j) + complex(3,4))


basket = [1,23,34,21,5,8,99,122,45];
fruits = ['a','b','c','d','e']

result = basket.index(2,0,3)

sorted_basket = sorted(basket);

fruits.append('apple');
fruits.insert(0,'mango')
print(result,'result')
print(fruits,'fruits');

print(sorted_basket,'sorted_basket');

r = list(range(101));
print(r,'range 1 - 100')

s = '*'.join(fruits)
print(s,'s');


new_list = [*basket];

first_dict = {"a":'1','b':'2'};
print(first_dict,'fdict'); 

new_d = {*first_dict};
print(new_d,'new d')
# print(new_list,'new list')

user = {
  'bowl':[1,2,3],
  'age':20,
  'greet':'hellow',
}


print(user.copy().values(),'user copy')
print(user.pop('greet'))
print(user.values())


my_tuple = (2,4,6,8,10,12);
# my_tuple[2] = 22; immutable
print(6 in my_tuple);