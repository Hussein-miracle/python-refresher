from random import randint


ans = randint(1,10);
while True:
  try:
      guess = int(input('Enter your guess num 1-10:  '))
      if guess > 0 and guess < 11:
        if guess == ans:
          print('You got the answer')
          break
        else:
          print('You didn\'t get  the answer')
          continue
      else:
        print('please enter a number btw 1 and 10')
        # continue
        
  except ValueError:
    print('please enter a number')
    continue
      
print(True * 1)
print(False * 1)