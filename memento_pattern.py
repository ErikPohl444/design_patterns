import pickle


class Originator:
    """
    Use the memento pattern to create a memento 
    containing a snapshot of the video game's current internal
    state.
    Use the memento to restore its internal state.
    """

    def __init__(self):
        self._videogamehealth = 10
        self._videogametime = 100
        self._videogameplayerloc = 12

    def set_memento(self, memento):
        previous_state = pickle.loads(memento)
        vars(self).clear()
        vars(self).update(previous_state)

    def create_memento(self):
        return pickle.dumps(vars(self))

    def outputstate(self):
        print("the player has ", self._videogamehealth, " health")
        print("the game time is  ", self._videogametime, " ticks")
        print("the player is at location  ", self._videogameplayerloc)


def main():
    originator = Originator()
    originator.outputstate()
    memento = originator.create_memento()
    originator._videogamehealth = 2
    originator._videogametime = 200
    originator._videogameplayerloc = 25
    originator.outputstate()
    originator.set_memento(memento)
    originator.outputstate()


if __name__ == "__main__":
    main()
