Punt = 0
Ronde = 1
Spel = True
from random import randint, randrange
x = randrange(1,1000)

while Spel == True:
    
    for y in range(3):
        print(x)
        Question = int(input('Raad een getal tussen de 1 en 1000: '))
        if Question == x:
            print('Je hebt het geraden!')
            Punt = Punt + 1
            Ronde = Ronde + 1
            print('Je hebt '+ str(Punt) +' punten.')
            print('Je zit nu in ronde ' + str(Ronde) +'.')
            break
        elif Question >= + 50:
            print('Je zit hoger dan het getal en er zitten max. 50 getallen ernaast, je bent warm')
        elif Question <= - 50:
            print('Je zit lager dan het getal en er zitten max. 50 getallen ervoor, je bent warm')
        elif Question > x and Question < x + 20:
            print('Je zit hoger dan het getal en er zitten max. 20 getallen ernaast, je bent heel warm')
        elif Question < x and Question > x + 20:
            print('Je zit lager dan het getal en er zitten max. 20 getallen ervoor, je bent heel warm')
        elif Question > x:
            print('Je zit hoger dan het random getal, je bent koud')
        elif Question < x:
            print('Je zit onder het random getal, je bent koud')
    if Question != x:
        print('Het getal was ' + str(x) + '!')
        Hervatten1 = input('Wil je nog doorgaan? J/N ')

    if Hervatten1 == 'j' or 'J':
        print('Het spel wordt hervat')
    if Hervatten == 'n' or 'N':
        print('Je hebt gekozen om te stoppen. Je was bij ronde ' + str(Ronde) + ' en je had ' + str(Punt) + ' punten.')
        Spel = False
    else:
        print('Type alleen \'J\/j\' of \'N\/n\' in! Je was bij ronde '+ str(Ronde))
        Spel = False
    
    



