class HighScores(object):
    def __init__(self, scores):
        self.scores = scores

    def latest(self):
        return self.scores[-1]

    def personal_best(self):
        return max(self.scores)

    def personal_top(self):
        return sorted(self.scores, reverse=True)[:3]

    def report(self):
        best = self.personal_best()
        latest = self.latest()
        if best == latest:
            return "Your latest score was {}. That's your personal best!".format(best)
        else:
            return "Your latest score was {}. That's {} short of your personal best!".format(
                latest, best - latest
            )
