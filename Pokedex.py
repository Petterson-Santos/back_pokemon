import Pokemon

class Pokedex():
    def __init__(self):
        self.lista_pokemon = []

    # poke1 = pokemon input
    # poke2 = pokemon goal
    def compare_name(self, poke1, poke2):
        if poke1.name == poke2.name:
            return 'Acertou'
        
        return
    
    # type = type1 ou type2
    # type1 = type do pokemon input
    # type2 = type do pokemon goal
    def compare_type(self, type, type1, type2):
        if type1 == type2:
            return 'type'+type+ '== \t'
        
        return 'type'+type+ '!= \t'
    
    # type = height ou weight
    # num1 e num2 mesma logica do compare_type
    def compare_number(self, type, num1, num2):
        if type == 'h':
            if num1 == num2:
                return 'height == \t'
            elif num1 < num2:
                return 'height > \t'
            else:
                return 'height < \t'
        else:
            if num1 == num2:
                return 'weight == )'
            elif num1 < num2:
                return 'weight > )'
            else:
                return 'weight < )'

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
