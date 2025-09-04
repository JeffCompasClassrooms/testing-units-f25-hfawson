### brought to you by chat gpt (:

import random
from typing import List, Dict, Optional

class DiceGame:
    def __init__(self, 
                 num_players: int = 2, 
                 num_dice: int = 1, 
                 sides_per_die: int = 6,
                 game_mode: str = "highest_total",
                 target_score: int = 50,
                 random_seed: Optional[int] = None):
        
        if not (2 <= num_players <= 6):
            raise ValueError("Number of players must be between 2 and 6.")
        if not (1 <= num_dice <= 3):
            raise ValueError("Number of dice must be between 1 and 3.")
        if sides_per_die < 2:
            raise ValueError("Dice must have at least 2 sides.")
        if game_mode not in {"highest_total", "first_to_target", "all_doubles"}:
            raise ValueError(f"Invalid game mode: {game_mode}")

        self.num_players = num_players
        self.num_dice = num_dice
        self.sides_per_die = sides_per_die
        self.game_mode = game_mode
        self.target_score = target_score
        self.random_seed = random_seed

        self.rng = random.Random(self.random_seed)
        self.players = [f"Player {i+1}" for i in range(num_players)]
        self.scores = [0 for _ in range(num_players)]
        self.winner = None

    def roll_dice(self) -> List[int]:
        return [self.rng.randint(1, self.sides_per_die) for _ in range(self.num_dice)]

    def play(self) -> Dict:
        if self.game_mode == "highest_total":
            return self._play_highest_total()
        elif self.game_mode == "first_to_target":
            return self._play_first_to_target()
        elif self.game_mode == "all_doubles":
            return self._play_all_doubles()

    def _play_highest_total(self) -> Dict:
        rolls = []
        for i in range(self.num_players):
            dice = self.roll_dice()
            total = sum(dice)
            self.scores[i] = total
            rolls.append({'player': self.players[i], 'dice': dice, 'total': total})
        
        max_score = max(self.scores)
        winners = [i for i, s in enumerate(self.scores) if s == max_score]

        self.winner = self.players[winners[0]] if len(winners) == 1 else None

        return {
            "mode": "highest_total",
            "rolls": rolls,
            "scores": self.scores,
            "winner": self.winner,
            "tie": len(winners) > 1
        }

    def _play_first_to_target(self) -> Dict:
        round_num = 0
        history = []

        while True:
            round_data = []
            for i in range(self.num_players):
                dice = self.roll_dice()
                total = sum(dice)
                self.scores[i] += total
                round_data.append({'player': self.players[i], 'dice': dice, 'total': total, 'cumulative': self.scores[i]})
                if self.scores[i] >= self.target_score:
                    self.winner = self.players[i]
                    history.append(round_data)
                    return {
                        "mode": "first_to_target",
                        "rounds": history,
                        "scores": self.scores,
                        "winner": self.winner
                    }
            history.append(round_data)
            round_num += 1

    def _play_all_doubles(self) -> Dict:
        rolls = []
        winners = []
        for i in range(self.num_players):
            dice = self.roll_dice()
            if all(d == dice[0] for d in dice):
                winners.append((i, dice[0]))  # (index, value)
            rolls.append({'player': self.players[i], 'dice': dice, 'all_same': all(d == dice[0] for d in dice)})

        if not winners:
            self.winner = None
        else:
            # Player with highest identical value wins
            best = max(winners, key=lambda x: x[1])
            self.winner = self.players[best[0]]

        return {
            "mode": "all_doubles",
            "rolls": rolls,
            "winner": self.winner,
            "any_winner": bool(winners)
        }

