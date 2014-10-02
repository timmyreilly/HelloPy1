'''Demonstrate raiding a refridgerator.'''

from contextlib import closing # for context manager  

class RefridgeratorRaider:
    '''Raid a refridgerator'''

    def open(self):
        print("Open fridge door.")

    def take(self, food):
        print("Finding {}...".format(food))
        if food == 'deep fried pizza':
            raise RuntimeError("Health Warning!")
        print("Taking {}".format(food))

    def close(self):
        print("Close fridge door")
        # Generic code that needs to be called for cleanup

def raid(food):
    with closing(RefridgeratorRaider()) as r:
        r.open()
        r.take(food)
    