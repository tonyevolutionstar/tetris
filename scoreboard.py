class ScoreBoard:
    #based on https://tetris.wiki/Scoring
    def __init__(self):
        self.score = 0
        self.level = 1
        self.lines = 0
        self.action = None

    #state - soft, hard drop
    def handle_score(self, action, state):
        if state == "soft":
            self.score += 1
        elif state == "hard":
            self.score += 2
            
        if action == "Single":
            self.score += 100 * self.level
        elif action == "Double":
            self.score += 300 * self.level
        elif action == "Triple":
            self.score += 500 * self.level 
        elif action == "Tetris":
            self.score += 800 * self.level 

        

