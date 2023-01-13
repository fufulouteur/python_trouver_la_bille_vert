import random

maCollec = ['rouge', 'rose', 'orange', 'rouge',
            'rose', 'jaune', 'rose', 'jaune']

sac2bille = ['rose', 'bleu', 'vert', 'orange', 'rouge',
             'pourpre', 'vert', 'bleu', 'rouge',
             'vert', 'pourpre', 'jaune', 'rouge', 'rose',
             'rouge', 'vert', 'jaune']

billes_sorties = []

tirages_restauts = 5

for x in range(5):
    if tirages_restauts > 0:
        selection = random.choice(sac2bille)
        billes_sorties.append(selection)
        tirages_restauts -= 1
        if selection == 'vert':
            maCollec.append(selection)
            sac2bille.remove(selection)
            print('Excellent ! tu as tire ta bille verte !')
            print(F'il restait {tirages_restauts} tirage.')
            break

if not('vert' in maCollec):
    print('tous les tirage sont faits. aucune bille verte.')

print("\nbille sorties pour ce tirage : ")
print(F"{billes_sorties}")
print(F"\nla nouvelle collection contient : \n{maCollec}")