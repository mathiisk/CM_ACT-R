import ccm
from ccm.lib.actr import *

log = ccm.log(html=True)

class HanoiModel(ccm.Model):
    pegA = [1, 2, 3]
    pegB = []
    pegC = []

    def print_state(self):
        print("State: {}, {}, {}".format (self.pegA, self.pegB, self.pegC))


class HanoiAgent(ACTR):
    goal = Buffer()
    retrieve = Buffer()
    subgoal_disk = Buffer()
    memory = Memory(retrieve, threshold=-3)
    history = Buffer()
    moves = 0

    # DMNoise(memory, noise=0.3)

    def init():

        memory.add('move pegA pegB')
        memory.add('move pegA pegC')
        memory.add('move pegB pegA')
        memory.add('move pegB pegC')
        memory.add('move pegC pegA')
        memory.add('move pegC pegB')

        goal.set('spread_disks')
        subgoal_disk.set('None')
        history.set('from_peg:None to_peg:None')

    def genaralMove(goal='?goal'):  # selects a random move to take every step
        memory.request('move ?fromPeg ?toPeg')

    def move_spread(goal='spread_disks', retrieve='move ?fromPeg ?toPeg', history='from_peg:?hist1 to_peg:?hist2'):
        from_peg_list = getattr(self.parent, fromPeg)  # what is on from peg
        to_peg_list = getattr(self.parent, toPeg)  # what is on to peg
        if from_peg_list and (not to_peg_list) and (not(fromPeg==hist2 and toPeg==hist1)):  # only to empty pegs
            # move disk
            disk_number = from_peg_list[0]
            to_peg_list.insert(0, from_peg_list.pop(0))
            print("Moved {} from {} to {}".format(disk_number, fromPeg, toPeg))
            self.moves += 1
            # update history of last move
            history.modify(from_peg=fromPeg)
            history.modify(to_peg=toPeg)
            self.parent.print_state()

        if len(self.parent.pegC) == 1 and len(self.parent.pegA)==1 and len(self.parent.pegB)==1:
            print("Goal achieved: All disks are spread")
            goal.set('biggest disk on pegC')
            subgoal_disk.set('3')

    def move_biggest_disk(goal='biggest disk on pegC',subgoal_disk='?biggest', retrieve='move ?fromPeg ?toPeg', history='from_peg:?hist1 to_peg:?hist2'):
        from_peg_list = getattr(self.parent, fromPeg)  # what is on from peg
        to_peg_list = getattr(self.parent, toPeg)  # what is on to peg
        game_rules_met = from_peg_list and (not to_peg_list or from_peg_list[0] < to_peg_list[0])
        previous_move_not_reversed = (not(fromPeg==hist2 and toPeg==hist1))
        if game_rules_met and previous_move_not_reversed and from_peg_list[0]<=int(biggest):  # only move disks that are not in the correct position yet
            if (from_peg_list[0]==int(biggest) and toPeg=='pegC') or (from_peg_list[0]!=int(biggest)): # only move biggest peg to final position
                disk_number = from_peg_list[0]
                to_peg_list.insert(0, from_peg_list.pop(0))
                print("Moved {} from {} to {}".format(disk_number, fromPeg, toPeg))
                self.moves += 1
                history.modify(from_peg=fromPeg)
                history.modify(to_peg=toPeg)
                self.parent.print_state()

        if self.parent.pegC and self.parent.pegC[0] == int(biggest) and biggest=='3':
            goal.set('biggest disk on pegC')
            subgoal_disk.set('2')
            print('subgoal achieved disk 3 is on pegC')
            #goal.set('achieve_final_state')
        elif self.parent.pegC and self.parent.pegC[0] == int(biggest) and biggest=='2':
            goal.set('biggest disk on pegC')
            print('subgoal achieved disk 2 is on pegC')
            subgoal_disk.set('1')
        if self.parent.pegC and self.parent.pegC[0] == int(biggest) and biggest=='1' and self.parent.pegC == [1, 2, 3]:
            goal.set('final_goal_achieved')
            print('subgoal achieved disk 1 is on pegC')
            subgoal_disk.set('None')

    def terminate(goal='final_goal_achieved'):
        print("Goal achieved: All disks are on pegC in the correct order!")
        print("{} moves".format(self.moves))
        self.stop()



# Set up the environment and agent
env = HanoiModel()
# agent = HanoiAgent()
agent = HanoiAgent()
env.agent = agent
# ccm.log_everything(agent)
agent.run()
