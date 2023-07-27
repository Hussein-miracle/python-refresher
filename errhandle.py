  
# while True:
#   try:
#     age = int(input('What is your age?'))
#     print(age)
#   except:
#     print('please enter a number')
#   else:
#     print('Fenks')
#     break
#   finally:
#     print('Done')
    
    
def gen_func():
  for i in range(1,101):
    yield i
    


# for item in gen_func():
#   print(item)

g = gen_func()
next(g)
print(next(g))