# This file is for strategy

from util.objects import *
from util.routines import *
from util.tools import find_hits


class Bot(GoslingAgent):
    def run(self):
        if self.get_intent() is not None:
            return
        if self.kickoff_flag:
            self.set_intent(kickoff())
            return

        if self.is_in_front_of_ball():
            self.set_intent(goto(self.friend_goal.location))
            return

        if self.me.boost > 99:
            self.set_intent(short_shot(self.foe_goal.location))
            return

        closest_boost = self.get_closest_large_boost()

        if closest_boost is not None:
            self.set_intent(goto(closest_boost.location))
            return
