from contrib.pyas.src.pyas_v3 import Leaf

from player import Player
from src.features.oppgoal.block import Block


class ProbBlockDefenders(Leaf):

    prototypes = [Block] + Block.prototypes

    @classmethod
    def onNew(cls, self):
        self.playerFilters = [Player.notTeammates,
                              Player.notActors, Player.notKeepers]