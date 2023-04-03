import Pokemon

class Pokedex():
    def __init__(self):
        self.lista_pokemon = []

    def compare_name(self, poke1, poke2):
        if poke1.name == poke2.name:
            return 'Acertou'
        
        return 'Errou'
    
    def compare_type(self, type, type1, type2):
        if type1 == type2:
            return 'type'+type+ '== \t'
        
        return 'type'+type+ '!= \t'
    
    def compare_numbers(self, type, num1, num2):
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

    def compare_pokemon(self, poke1, poke2):
        if self.compare_name(poke1, poke2) == 'Acertou':
            return 'Acertou'
        
        message = '( '

        message += self.compare_type('1', poke1.type1, poke2.type1)
        message += self.compare_type('2', poke1.type2, poke2.type2)
        message += self.compare_numbers('h', poke1.height, poke2.height)
        message += self.compare_numbers('w', poke1.weight, poke2.weight)

        return message
