from direct.showbase.ShowBase import ShowBase
from fgb import Mapmanager

class Game(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
        self.land = Mapmanager()
        base.camlens.setFor(90)
game = Game()
game.run()