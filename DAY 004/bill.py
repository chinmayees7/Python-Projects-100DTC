import random
friends= ["alice", "bob", "charlie", "david", "emanuel"]

# print(len(friends)-1) = 5-1 = 4 since indexes starts from 0 
random_friend_index= random.randint(0,len(friends)-1)  
print(friends[random_friend_index])

#OR

print(random.choice(friends))