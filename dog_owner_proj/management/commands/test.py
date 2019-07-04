#TEST OF dog.py

import dog

#--------------- Test dog class
rex = dog.Dog(1,'Rex', 'Border Collie', 5, 1)
rex.describe_dog()

#================ Test owner class
amy = dog.Owner(1,'Amy', 'Jones')
amy.describe_owner() 

