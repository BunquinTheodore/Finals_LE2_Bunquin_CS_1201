#Bunquin, Theodore Von Joshua M.
#CS 1201

import pickle

class Score:
    def __init__(self):
        self.scores = []
        self.load_scores()

    def load_scores(self):
        try:
            with open("scores.pickle", "rb") as file:
                self.scores = pickle.load(file)
        except FileNotFoundError:
            self.scores = []
        self.scores.sort(key=lambda x: x['points'], reverse=True)
        return self.scores

    def save_scores(self, username, points):
        self.scores.append({"username": username, "points": points})
        self.scores.sort(key=lambda x: x['points'], reverse=True)
        with open("scores.pickle", "wb") as file:
            pickle.dump(self.scores, file)
