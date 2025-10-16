# if the alien is green, print a message that the player just earned 5 points for shooting the alien  
alien_color = 'green'
if alien_color == 'green':
    print("You just earned 5 points for shooting the alien!")
# if the alien is yellow, print a message that the player just earned 10 points
alien_color = 'yellow'
if alien_color == 'yellow':
    print("You just earned 10 points for shooting the alien!") 
# if the alien is red, print a message that the player just earned 15 points
alien_color = 'red'
if alien_color == 'red':
    print("You just earned 15 points for shooting the alien!") 
# if the alien is some other color, print a message that the player failed to earn points
alien_color = 'blue'
if alien_color != 'green' and alien_color != 'yellow' and alien_color != 'red':
    print("You failed to earn points!") 
# Write one version of this program that runs the if block and another that runs the else block
alien_color = 'blue'
if alien_color == 'green':
    print("You just earned 5 points for shooting the alien!")
else:
    print("You failed to earn points!")  
