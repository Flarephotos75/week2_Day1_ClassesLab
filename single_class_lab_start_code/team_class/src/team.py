from unicodedata import name


class Team:
    def __init__(self, name, players,coach):
        self.name = name
        self.players = players
        self.coach = coach

    def add_player(self,new_player):
        self.players.append(new_player)
    
    def has_player(self, player):
        for players in self.players:
            if players == player:
                return True
        return False


    points = 0

    def play_game(self, result):
        if result == True:
            self.points += 3
        
