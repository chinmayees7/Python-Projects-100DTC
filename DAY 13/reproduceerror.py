from random import randint
dice_images=["1","2","3","4","5","6"]

# dice_num=randint(1,6)
# print(dice_images[dice_num])

""" 
Occasional Error:   
print(dice_images[dice_num])
          ~~~~~~~~~~~^^^^^^^^^^
IndexError: list index out of range
"""

"""
Explanation:
Since a list has indexes starting from 0, the last index of the list dice_images[] would be 5. 
Upon randomly generating an index from 1 to 6, 6 will never be able to retrieve an element from the list. So, the error is produced, "list index out of range"
"""

"""
To always produce this error, any index greater than 5 will be needed.
"""

# dice_num=6
# print(dice_images[dice_num])

"""
To solve this error we have to modify randint to produce integers from 0 to 5.
"""
dice_num=randint(0,5)
print(dice_images[dice_num])