# Variabelen
Punt = 0
Ronde = 1
Spel = True
Poging = 10
from random import randint, randrange
Getal = randint(1,1000)
# De game
while Spel == True:

    Raden = input('Wil je een getal raden? J/N ')
    if Raden == 'J' or Raden == 'j':
        print('Ronde '+ str(Ronde))
        for x in range(10):
            Gokken = int(input('Raad het geheime getal: '))
            if Gokken == Getal:
                print('Je hebt het geraden!')
                Ronde += 1
                Punt += 1
                print('Je zit nu in ronde '+ str(Ronde))
                print('Je hebt '+ str(Punt) +' punten')
                break
            if Gokken > Getal:
                print('Je zit hoger dan het geheime getal')
            if Gokken < Getal:
                print('Je zit lager dan het geheime getal')
            if Gokken > Getal and Gokken < Getal + 50:
                print('Je zit hoger dan het geheime getal, max. 50 getallen ernaast.')
            if Gokken < Getal and Gokken > Getal - 50:
                print('Je zit lager dan het geheime getal, max. 50 getallen eronder.')
            if Gokken >= Getal and Gokken <= Getal + 20:
                print('Je zit hoger dan het geheime getal en je bent heel warm, max. 20 getallen ernaast.')
            if Gokken <= Getal and Gokken >= Getal - 20:
                print('Je zit lager dan het geheime getal en je bent heel warm, max. 20 getallen ervoor.')
            if Gokken != Getal:
                Poging -= 1
                print('Je hebt nog '+ str(Poging) +' pogingen')
        if Poging == 0:
            print('Je hebt geen pogingen meer! Het juiste getal is '+ str(Getal))
            Spel = False
        if Ronde == 20:
            print('Je hebt alles goed geraden! Je kwam bij ronde '+ str(Ronde) +' en je hebt '+ str(Punt) +' punten gehaald.')
            Spel = False
    elif Raden == 'N' or Raden == 'n':
        print('Spel gestopt')
        Spel = False
    else:
        print('Type alleen \'J\j\' of \'N/n\' in!')
        Spel = False