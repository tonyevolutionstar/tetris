class ScoreBoard:
    #based on https://tetris.wiki/Scoring
    def __init__(self):
        self.score = 0
        self.level = 1
        self.lines = 0
        self.action = None
        self.lost = ""


