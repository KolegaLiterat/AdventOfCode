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

    def __init__(self, data) -> None:
        self.MatchData = data

    def run_tournament(self):
        opponent_move : str = "None"
        player_move : str = "None"
        sum_of_player_points : int = 0

        for match in self.MatchData:
            opponent_move = self._decode_moves(match[0], False)
            player_move = self._decode_moves(match[1], True)

            sum_of_player_points = sum_of_player_points + self._calculate_outcome(player_move, opponent_move)

        return sum_of_player_points 
    
    def _decode_moves(self, encrypted_move: str, is_player: bool):
        if is_player == True:
            move = self.PlayerMoves[encrypted_move]
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