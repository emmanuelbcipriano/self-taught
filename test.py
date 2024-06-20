import random
 
rand_list=[]
n=99
for i in range(n):
    rand_list.append(random.randint(1,9))

for i in rand_list:
    inpt = input('Enter an integer: ')
    
    if inpt == 'q':
        print('Thank you for playing')
        quit()
    elif inpt == str(i):
        print('You have successfully guessed the number.')
        quit()
    else:
        print('Please try again.')
