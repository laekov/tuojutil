import numpy as np


class PlayerInContest(object):
    def __init__(self):
        pass

    def from_line(self, ls):
        self.uid, self.dept, self.name, self.stot = ls[1:5]
        self.scores = ls[5:]
        return self

    def parse_score(self, count_pre_test=True):
        for i, v in enumerate(self.scores):
            v = v.strip()
            if v == '-':
                self.scores[i] = 0
            elif v.find(' ') != -1:
                self.scores[i] = sum(map(int, v.split()))
            else:
                self.scores[i] = int(v)
        self.rtot = sum(self.scores)


def read_contest(filename):
    players = dict()
    with open(filename, 'r') as f:
        for l in f:
            ls = l.split('\t')
            if ls[0] == '#' or len(ls) < 3:
                continue
            pic = PlayerInContest().from_line(ls) 
            players[pic.uid] = pic
    return players


def parse_score(players, count_pre_test=True):
    for p in players:
        players[p].parse_score(count_pre_test)
