
number = 88
guess  = int(input('enter a integer number: '))

if guess == number:
    #block begin
    print('awesome, you guessed it.')
    print('not price yet.')
elif guess < number:
    #another block
    print('must be bigger')
else:
    print('must be smaller')


print('Done.')
