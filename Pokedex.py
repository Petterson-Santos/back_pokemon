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
            return 'Acertou'
        
        return
    
    # type = type1 ou type2
    # type1 = type do pokemon input
    # type2 = type do pokemon goal
    def compare_type(self, type1, type2):
        if type1 == type2:
            return GREEN+type1+RESET
        
        return RED+type1+RESET
    
    # type = height ou weight
    # num1 e num2 mesma logica do compare_type
    def compare_number(self, num1, num2):
            if num1 == num2:
                return GREEN+str(num1)+RESET
            elif num1 < num2:
                return RED+str(num1)+RESET
            else:
                return RED+str(num1)+RESET

    # poke1 = pokemon input
    # poke2 = pokemon goal
    def compare_pokemon(self, poke1, poke2):
        if self.compare_name(poke1, poke2) == 'Acertou':
            print(
                '( '+GREEN+poke1.type1+'\t'+poke1.type2+'\t'+str(poke1.height)+'\t'+str(poke1.weight)+RESET+' )'
            )
            return 'Acertou'
        
        message = '( '

        message += self.compare_type(poke1.type1, poke2.type1)
        message += '\t'
        message += self.compare_type(poke1.type2, poke2.type2)
        message += '\t'
        message += self.compare_number(poke1.height, poke2.height)
        message += '\t'
        message += self.compare_number(poke1.weight, poke2.weight)

        message += ' )'

        return message
