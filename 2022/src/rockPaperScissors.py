from dataclasses import dataclass

@dataclass

class Tournament():
    OpponentMoves = {
        "A" : "Rock",
        "B" : "Paper",
        "C" : "Scissors"
    }

    PlayerMoves = {
        "X" : ["Rock", 1],
        "Y" : ["Paper", 2],
        "Z" : ["Scissors", 3]
    }

    MatchOutcomes = {
        "X" : ["Lose", 0],
        "Y" : ["Draw", 3],
        "Z" : ["Win", 6],
    }

    def __init__(self, data) -> None:
        self.MatchData = data

    def run_tournament(self):
        opponent_move : str = "None"
        player_move : str = "None"
        sum_of_player_points : int = 0

        for match in self.MatchData:
            opponent_move = self._decode_moves(match[0], False, False)
            player_move = self._decode_moves(match[1], True, False)

            sum_of_player_points = sum_of_player_points + self._calculate_outcome(player_move, opponent_move)

        return sum_of_player_points 
    
    def run_setupo_tournament(self):
        match_outcome : str = "None"
        opponent_move : str = "None"
        sum_of_player_points : int = 0

        for match in self.MatchData:
            match_outcome = self._decode_moves(match[1], False, True)
            opponent_move = self._decode_moves(match[0], False, False)

            sum_of_player_points = self._calculate_setup_outcome(match_outcome, opponent_move) + sum_of_player_points
        
        return sum_of_player_points
    
    def _decode_moves(self, encrypted_move: str, is_player: bool, is_setup_match: bool):
        if is_player == True and is_setup_match == False:
            move = self.PlayerMoves[encrypted_move]
        elif is_player == False and is_setup_match == True:
            move = self.MatchOutcomes[encrypted_move]
        else:
            move = self.OpponentMoves[encrypted_move]
        
        return move
    
    def _calculate_outcome(self, player_move: list, opponent_move: str):
        player_points: int = 0

        match opponent_move:
            case "Rock":
                if player_move[0] == "Rock":
                    player_points = 3 + player_move[1]
                elif player_move[0] == "Paper":
                    player_points = 6 + player_move[1]
                elif player_move[0] == "Scissors":
                    player_points = 0 + player_move[1]
            case "Paper":
                if player_move[0] == "Rock":
                    player_points = 0 + player_move[1]
                elif player_move[0] == "Paper":
                    player_points = 3 + player_move[1]
                elif player_move[0] == "Scissors":
                    player_points = 6 + player_move[1]
            case "Scissors":
                if player_move[0] == "Rock":
                    player_points = 6 + player_move[1]
                elif player_move[0] == "Paper":
                    player_points = 0 + player_move[1]
                elif player_move[0] == "Scissors":
                    player_points = 3 + player_move[1]
            case other:
                print("Missing move!")
            
        return player_points
    
    def _calculate_setup_outcome(self, match_outcome: list, opponent_move: str):
        player_points: int = 0

        match match_outcome[0]:
            case "Win":
                if opponent_move == "Rock":
                    player_points = match_outcome[1] + self.PlayerMoves["Y"][1]
                elif opponent_move == "Paper":
                    player_points = match_outcome[1] + self.PlayerMoves["Z"][1]
                elif opponent_move == "Scissors":
                    player_points = match_outcome[1] + self.PlayerMoves["X"][1]
            case "Draw":
                if opponent_move == "Rock":
                    player_points = match_outcome[1] + self.PlayerMoves["X"][1]
                elif opponent_move == "Paper":
                    player_points = match_outcome[1] + self.PlayerMoves["Y"][1]
                elif opponent_move == "Scissors":
                    player_points = match_outcome[1] + self.PlayerMoves["Z"][1]
            case "Lose":
                if opponent_move == "Rock":
                    player_points = match_outcome[1] + self.PlayerMoves["Z"][1]
                elif opponent_move == "Paper":
                    player_points = match_outcome[1] + self.PlayerMoves["X"][1]
                elif opponent_move == "Scissors":
                    player_points = match_outcome[1] + self.PlayerMoves["Y"][1]
            case other:
                print("Missin move!")

        return player_points