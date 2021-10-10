Punt = 0
Ronde = 1
Spel = True
from random import randint, randrange


while Spel == True:
    for y in range(11):
        x = randrange(1,1000)
        print(x)
        Question = int(input('Raad een getal tussen de 1 en 1000: '))
        if Question == x:
            print('Je hebt het geraden!')
            Punt = Punt + 1
            Ronde = Ronde + 1
            print('Je hebt '+ str(Punt) +' punten.')
            print('Je zit nu in ronde ' + str(Ronde) +'.')
        else:
            print('Helaas, je mag maar maximaal 10 keer raden!')
    break