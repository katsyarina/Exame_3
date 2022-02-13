class Tomato:
    states = {0: 'Flower', 1: 'Green', 2: 'Yellow', 3: 'Red'}
    def __init__(self, _index, _state):
        self._index = _index
        self._state = Tomato.states[0]
    def grow(self):
        self._next_state
    def is_ripe(self):
        if self._state == len(Tomato.states)+1:
            return True
        else:
            return False
    def _next_state(self):
        if self._state < len(Tomato.states)+1:
            self._state += 1
    def print_state(self):
        print()



class TomatoBush:
    def __init__(self, number_tomato):
        self.tomatoes = [Tomato(i) for i in range(0, number_tomato)]
    def grow_all(self, ):
        for t in self.tomatoes:
            t.grow()
    def all_are_ripe(self):
        if all(t.is_ripe for t in self.tomatoes):
            return True
    def give_away_all(self):
        self.tomatoes = []

class Gardner:
    def __init__(self, name, _plant):
        self.name = name
        self._plant = _plant
    def work(self):
        print('work')
        self._plant.grow_all()
        print('end')
    def harvest(self):
        if self._plants.all_are_ripe():
            self._plants.give_away_all()
            return 'Gardner take tomatos'
        return 'Attention'

    @staticmethod
    def knowledge_base():
        print('Info about Gardnerin')

tomatobush = TomatoBush(8)
gardner = Gardner('Victor', tomatobush)
print(gardner.knowledge_base())



