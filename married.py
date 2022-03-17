import random
girls=["sahar", "shirin", "atefe", "mahsa", "mahla", "zahra", "mina", "sara"]
boys=["hamed", "amir", "mohammad", "sajjad", "hojjat", "ali", "masood", "mehrdad"]
zoj=[]
for i in range(len(boys)):
    boy=random.choice(boys)
    girl=random.choice(girls)
    boys.remove(boy)
    girls.remove(girl)
    zoj.append((boy,girl))
print(zoj)