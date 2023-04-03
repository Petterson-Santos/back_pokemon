from Pokemon import Pokemon
from Pokedex import Pokedex

pokedex = Pokedex()

geodude = Pokemon('geodude', 'rock', 'ground', 0.4, 20)
pikachu = Pokemon('pikachu', 'electric', 'electric', 0.4, 6)
blastoise = Pokemon('blastoise', 'water', 'water', 1.6, 85.5)

pokedex.lista_pokemon.append(geodude)
pokedex.lista_pokemon.append(pikachu)
pokedex.lista_pokemon.append(blastoise)

print(geodude.name+'\n'+pokedex.compare_pokemon(geodude, geodude))