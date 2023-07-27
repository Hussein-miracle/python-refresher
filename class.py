# oop

from functools import reduce

class PlayerCharacter:
  # Class Object attribute
  membership = True
  def __init__(self,name:str,age:int = 23) -> None:
    self.name = name
    self.age = age
    
  def run(self):
    print('running')
    return self
  
  def toggle_membership(self):
    self.membership = not(self.membership)
    return self.membership
  
  @classmethod
  def adding_things(cls,n2,n1):
    return  n1 + n2
  
  @staticmethod
  def add_up_things(n1,n2):
    return n1 + n2
  
    
  
  
  

  
player1 =  PlayerCharacter('Abdullahi');
print(player1.adding_things(2,3),'p1 adding');
print(player1.add_up_things(2,3),'p1 add up');


# print(player1.name,'p1 name');
print(player1.run(),'p1 run');
# print(player1.age,'p1 age');
print(player1.toggle_membership(),'p1 age');
print(player1.toggle_membership(),'p1 age');
print(player1.toggle_membership(),'p1 age');
print(player1.toggle_membership(),'p1 age');


class Node:
  def __init__(self,value):
    self.next = None
    self.value = value
    
class LinkedList:
  def __init__(self) -> None:
    self.head = None
    self.tail = None
    self.length = 0
    
    
  def append(self,value):
    new_node = Node(value)
    if(not(self.head)):
      self.head = new_node
      self.tail = self.head
    else:
      self.tail.next = new_node
      self.tail = new_node
    self.length = self.length + 1
    return self
  
  
  # def pop(self):
  #   if(not self.head): return None
    
    # if()
    
  
  

      
      
linked_list = LinkedList()

print(linked_list.append(2))


class User():
  def sign_up():
    print('Signed up')
    
    
  
user = User.sign_up()

# user.sign_up()


# lambda param:  



# MAP ,FILTER ,ZIP,REDUCE


def mult_by_2(li:list):
  new_list = []
  
  for item in li:
    mapped_item = item * 2
    new_list.append(mapped_item)
  print(new_list,'new list')
  return new_list


mult_by_2([1,2,3])

my_list = [1,2,3]; 
def iter1(item):
  if item % 2 != 0:
    return item ** 2

mapped_list = list(map(lambda item:  item * 2,my_list))

print(mapped_list,'mapped_list')


print()

def div(num:int):
  if  num % 2 != 0:
    return num


filtered_list = list(filter(div,my_list))

print(filtered_list,'fl')

your_list = (10,20,30)

print(list(zip(my_list,your_list)))
print(list(zip(your_list,my_list)))


a = [(4,3),(0,2),(10,-1),(9,9)]

a.sort(key = lambda x:x[1])

print(a)




# list,set,dictionary comprehensinon


m_list = [param for param in 'hello']


for char  in 'hello':
  m_list.append(char)


print(m_list)  




n_l = [n ** 2 for n in range(1,101) if n % 2 == 0 ]

print(n_l)


s_s =  {param for param in 'hello'}

print(s_s,'ss');

simple_dict = {
  'a':2,
  'b':4
}


new_d = {k:value ** 2 for k,value in simple_dict.items() }

print(new_d)


from time import time

def performance(fn):
  def wrapper(*args,**kwargs):
    t1 = time()
    result = fn(*args,**kwargs)
    t2 = time()
    print(f'took {t2 - t1} s')
    return result
  return wrapper



@performance
def long_time():
  for i in range(100000000):
    i*5
    
long_time()