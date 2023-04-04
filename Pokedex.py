import Pokemon

RED = "\033[1;31m"
GREEN = "\033[0;32m"
RESET = "\033[0;0m"

class Pokedex():
    def __init__(self):
        self.lista_pokemon = []

    def get_pokemon(self, pokemon_name):
        for pokemon in self.lista_pokemon:
            if pokemon.name == pokemon_name:
                return pokemon

     # poke1 = pokemon input
     # poke2 = pokemon goal
    def compare_name(self, poke1, poke2):
        if poke1.name == poke2.name:
            return GREEN+'Acertou'+RESET
        
        return
    
    # type = type1 ou type2
    # type1 = type do pokemon input
    # type2 = type do pokemon goal
    def compare_type(self, type, type1, type2):
        if type1 == type2:
            return GREEN+'type'+type+ '== \t'+RESET
        
        return RED+'type'+type+ '!= \t'+RESET
    
    # type = height ou weight
    # num1 e num2 mesma logica do compare_type
    def compare_number(self, type, num1, num2):
        if type == 'h':
            if num1 == num2:
                return GREEN+'height== \t'+RESET
            elif num1 < num2:
                return RED+'height> \t'+RESET
            else:
                return RED+'height< \t'+RESET
        else:
            if num1 == num2:
                return GREEN+'weight== '+RESET+')'
            elif num1 < num2:
                return RED+'weight> '+RESET+')'
            else:
                return RED+'weight< '+RESET+')'

    # poke1 = pokemon input
    # poke2 = pokemon goal
    def compare_pokemon(self, poke1, poke2):
        if self.compare_name(poke1, poke2) == 'Acertou':
            return 'Acertou'
        
        message = '( '

        message += self.compare_type('1', poke1.type1, poke2.type1)
        message += self.compare_type('2', poke1.type2, poke2.type2)
        message += self.compare_number('h', poke1.height, poke2.height)
        message += self.compare_number('w', poke1.weight, poke2.weight)

        return message
