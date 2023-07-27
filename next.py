is_old = True;
is_licensed = True;


if is_old == True and is_licensed == False:
  print('You can\'t drive still')
elif is_old == True and is_licensed != False:
  print('You can drive still and race maddd')
else:
  print('You can\'t drive \ln hehe');
  
  
print(bool(None))
   
#  Ternary Operator

is_friend = '';

can_message  = 'msg allowed' if bool(is_friend) else 'msg not allowed'

print(can_message,'cm')


for item,i in 'Zero To Mastery':
  print(item,i)

obj = {'b':2,'bu': 0, 'p':'wwr'}
for item,i in obj:
  print(item,i)


my_list  = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16];

length = len(my_list);

for i in range(0,length+1 , 2):
  print(i,'i')

string = 'loksss'

for ch in enumerate(string):
  a,b = ch
  print(ch,'ch')
  print(a,'a')
  print(b,'b')



i = 0;

while i < 50:
  i += 1;
  print(i)
  # if i == 25:
  #   break;
else:
  print('Hi')


picture = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0],
]


for image in picture:
  for px in image:
    if not(px):
      print(' ',end='')
    elif px == 1:
      print('*',end='')
  print('')


some_list = ['a','b','c','b','d','m','n','n'];

some_list.sort()

duplicates = []
for item in some_list:
  if(some_list.count(item) > 1):
    
    print(f'There is a duplicate of {item}')
    if(item not in duplicates):
      duplicates.append(item)
      
    
print(duplicates)
    
  
def printName(first_name,last_name):
  print('YOur fullname is {} {}'.format(first_name,last_name))
  
printName('ade','boli')


def super_func(*args,**kwargs):
  # print(*args);
  total = 0;
  for item in kwargs.values():
    # print(item)
    total += item;
  return sum(args) + total;

print(super_func(1,2,3,4,5,name1 = 2,name2 = 99))



# def some_func():
  # nonlocal total = 100:



total = 0;

def count():
  # nonlocal total;
  global total;
  total += 1;
  return total;

print(count(),'total count')


def outer():
  x = 'local'
  def inner():
    nonlocal x;
    x = 'nonlocal';
    print('inner x:' , x);
  
  inner();
  
  print('outer',x);
  
outer()