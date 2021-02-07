import random
def gamewin(comp,you):
    if comp == you:
        return None
    elif comp == 'snake':
        if you == 'water':
            return False
        elif you == 'gun':
            return True
    elif comp == 'water':
        if you == 'gun':
            return False
        elif you == 'snake':
            return True
    elif comp == 'gun':
        if you == 'snake':
            return False
        elif you == 'water':
            return True

print('comp turn:Snake(s),water(w),gun(g)?')
randNo = random.randint(1,3)
if randNo == 1:
    comp = 'snake'
elif randNo == 2:
    comp = 'water'
elif randNo == 3:
    comp = 'gun'

you = input('yours turn : Snake(s),water(w),gun(g)?')
a = gamewin(comp,you)
print(f'comp choose:{comp}')
print(f'you choose:{you}')

if a == None:
    print("The game is tie")
elif a:
    print("You win")
else:
    print("You loose")