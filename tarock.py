import random

# --- DATA MODEL ---
FULL_CARD_POOL = [
    {"id": 1, "name": "TRAINING DUMMY", "attack": 1, "defense": 6, "special": [], "ability": "Defence +1"},
    {"id": 2, "name": "ENGINEER", "attack": 4, "defense": 3, "special": [], "ability": "Defence +1"},
    {"id": 3, "name": "TETRAODD", "attack": 3, "defense": 4, "special": [], "ability": "Lucky Attack"},
    {"id": 4, "name": "ITICA", "attack": 2, "defense": 4, "special": ["Left"], "ability": "Attack +1"},
    {"id": 5, "name": "SCARABARA", "attack": 5, "defense": 3, "special": [], "ability": "Defence +1"},
    {"id": 6, "name": "MYSTERIOUS DAGGER", "attack": 5, "defense": 5, "special": [], "ability": "Special Up"},
    {"id": 7, "name": "IRONTALON", "attack": 4, "defense": 6, "special": [], "ability": "Lucky Attack"},
    {"id": 8, "name": "DARK TROOPERS", "attack": 5, "defense": 4, "special": ["Right"], "ability": "Piercing Attack"},
    {"id": 9, "name": "SPIDERBOT", "attack": 3, "defense": 7, "special": [], "ability": "Last Attack +1"},
    {"id": 10, "name": "KAKTOS", "attack": 5, "defense": 4, "special": ["Up"], "ability": "First Defence +1"},
    {"id": 11, "name": "GILLMAN WARRIORS", "attack": 4, "defense": 7, "special": [], "ability": "Attack +1"},
    {"id": 12, "name": "GALACTOSS", "attack": 6, "defense": 4, "special": ["Down"], "ability": "Defence +1"},
    {"id": 13, "name": "ARCADIAN SOLDIER", "attack": 5, "defense": 6, "special": [], "ability": "Attack +1"},
    {"id": 14, "name": "OWRU BANDITS", "attack": 6, "defense": 5, "special": [], "ability": "First Defence +1"},
    {"id": 15, "name": "SECURITY DRONE", "attack": 7, "defense": 4, "special": [], "ability": "Last Attack +1"},
    {"id": 16, "name": "FLUTE", "attack": 4, "defense": 8, "special": [], "ability": "Attack +1"},
    {"id": 17, "name": "DROPSHIP", "attack": 7, "defense": 4, "special": ["Down"], "ability": "Defence +1"},
    {"id": 18, "name": "KNIGHT", "attack": 5, "defense": 7, "special": [], "ability": "Last Attack +1"},
    {"id": 19, "name": "BOT WARRIORS", "attack": 7, "defense": 5, "special": [], "ability": "Lucky Attack"},
    {"id": 20, "name": "CEPEDE", "attack": 6, "defense": 6, "special": [], "ability": "Defence +1"},
    {"id": 21, "name": "GHOST", "attack": 6, "defense": 7, "special": [], "ability": "Last Attack +1"},
    {"id": 22, "name": "CHIEF", "attack": 9, "defense": 4, "special": [], "ability": "Defence +1"},
    {"id": 23, "name": "PROTOTYPE SPIDERBOT", "attack": 5, "defense": 7, "special": ["Right"], "ability": "Attack +1"},
    {"id": 24, "name": "CASTER GUN", "attack": 8, "defense": 4, "special": ["Up"], "ability": "Piercing Attack"},
    {"id": 25, "name": "COMMANDER", "attack": 7, "defense": 6, "special": [], "ability": "Attack +1"},
    {"id": 26, "name": "PARADIGM HOURGLASS", "attack": 5, "defense": 9, "special": [], "ability": "Last Attack +1"},
    {"id": 27, "name": "SHIELD OF CHRONOS", "attack": 3, "defense": 9, "special": ["Up", "Down"], "ability": "First Defence +1"},
    {"id": 28, "name": "STEELSCALE", "attack": 8, "defense": 6, "special": [], "ability": "Defence +1"},
    {"id": 29, "name": "GUARDIAN", "attack": 7, "defense": 7, "special": [], "ability": "Attack +1"},
    {"id": 30, "name": "PRINCESS FIN", "attack": 6, "defense": 8, "special": [], "ability": "Special Left"},
    {"id": 31, "name": "YELLOW BIRD", "attack": 9, "defense": 6, "special": ["Right"], "ability": "First Defence +1"},
    {"id": 32, "name": "DARK APOSTLE", "attack": 8, "defense": 7, "special": ["Left"], "ability": "Last Attack +1"},
    {"id": 33, "name": "YURMALA TURTLE", "attack": 6, "defense": 10, "special": [], "ability": "Attack +1"},
    {"id": 34, "name": "THUNDERSTONE", "attack": 6, "defense": 9, "special": ["Right"], "ability": "Lucky Attack"},
    {"id": 35, "name": "FIREBIRD", "attack": 9, "defense": 6, "special": ["Down"], "ability": "Defence +1"},
    {"id": 36, "name": "GEN", "attack": 7, "defense": 9, "special": ["Left"], "ability": "First Defence +1"},
    {"id": 37, "name": "ASTROBLADE", "attack": 6, "defense": 9, "special": ["Up"], "ability": "Piercing Attack"},
    {"id": 38, "name": "THE SHADOW", "attack": 6, "defense": 9, "special": ["Down"], "ability": "Attack +1"},
    {"id": 39, "name": "MASTER MAYFAIR", "attack": 8, "defense": 7, "special": ["Up", "Right"], "ability": "First Defence +1"},
    {"id": 40, "name": "SEALURK", "attack": 9, "defense": 5, "special": ["Left", "Down"], "ability": "Attack +1"},
    {"id": 41, "name": "DARK CHARIOT", "attack": 9, "defense": 5, "special": ["Up", "Down"], "ability": "Defence +1"},
    {"id": 42, "name": "THE GREAT CHRONICLER", "attack": 7, "defense": 9, "special": ["Left", "Right"], "ability": "Lucky Attack"},
    {"id": 43, "name": "HERO", "attack": 9, "defense": 7, "special": ["Right", "Down"], "ability": "Last Attack +1"},
    {"id": 44, "name": "EVERTURSO", "attack": 9, "defense": 7, "special": ["Left", "Up"], "ability": "Defence +1"},
    {"id": 45, "name": "ARCHIMEDES", "attack": 7, "defense": 9, "special": ["Left", "Up", "Right"], "ability": "Lucky Attack"},
    {"id": 46, "name": "MESMEROTH", "attack": 9, "defense": 7, "special": ["Up", "Right", "Down"], "ability": "Lucky Attack"},
    {"id": 47, "name": "TRIN", "attack": 8, "defense": 8, "special": ["Down", "Left", "Up"], "ability": "Lucky Attack"},
    {"id": 48, "name": "OCEANHORN", "attack": 10, "defense": 6, "special": ["Right", "Down", "Left"], "ability": "First Defence +1"},
    {"id": 49, "name": "TRILOTH", "attack": 10, "defense": 5, "special": ["Up", "Right", "Down", "Left"], "ability": "Defence +1"},
    {"id": 50, "name": "SACRED EMBLEMS", "attack": 5, "defense": 10, "special": ["Up", "Right", "Down", "Left"], "ability": "Piercing Attack"}
]

# --- GAME ENGINE ---
class TarockCard:
    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.base_attack = data["attack"]
        self.base_defense = data["defense"]
        self.special = set(data["special"])
        self.ability = data["ability"]
        
        self.owner = None
        self.first_defense_active = (self.ability == "First Defence +1")
        
        # Apply Board Control abilities immediately
        if self.ability == "Special Left":
            self.special.add("Left")
        elif self.ability == "Special Up":
            self.special.add("Up")

    def get_attack(self, is_last_round):
        atk = self.base_attack
        if self.ability == "Attack +1":
            atk += 1
        if self.ability == "Last Attack +1" and is_last_round:
            atk += 1
        return atk

    def get_defense(self):
        dfn = self.base_defense
        if self.ability == "Defence +1":
            dfn += 1
        if self.first_defense_active:
            dfn += 1
        return dfn

    def receive_attack(self):
        """Consumes the First Defence shield if it was active."""
        if self.first_defense_active:
            self.first_defense_active = False

class TarockGame:
    def __init__(self, p1_name, p2_name, card_pool):
        # Deal 5 random cards to each player
        deck = random.sample([TarockCard(c) for c in card_pool], 10)
        self.players = {
            1: {"name": p1_name, "hand": deck[0:5]},
            2: {"name": p2_name, "hand": deck[5:10]}
        }
        self.board = [[None for _ in range(3)] for _ in range(3)]
        self.turn = 1
        self.current_player = 1 # P1 starts

    def play_card(self, player_id, card_index, x, y):
        if self.board[y][x] is not None:
            raise ValueError("Board space is already occupied.")
        
        card = self.players[player_id]["hand"].pop(card_index)
        card.owner = player_id
        self.board[y][x] = card
        
        is_last_round = (self.turn >= 8)
        self._resolve_adjacent_combat(x, y, card, is_last_round)
        
        self.turn += 1
        self.current_player = 2 if self.current_player == 1 else 1

    def _resolve_adjacent_combat(self, x, y, attacker, is_last_round):
        directions = {
            "Up": (0, -1, "Down"),
            "Down": (0, 1, "Up"),
            "Left": (-1, 0, "Right"),
            "Right": (1, 0, "Left")
        }
        
        for attack_dir, (dx, dy, defend_dir) in directions.items():
            nx, ny = x + dx, y + dy
            if 0 <= nx < 3 and 0 <= ny < 3:
                defender = self.board[ny][nx]
                if defender and defender.owner != attacker.owner:
                    self._execute_combat(attacker, defender, attack_dir, defend_dir, is_last_round)

    def _execute_combat(self, attacker, defender, atk_dir, def_dir, is_last_round):
        atk_special = atk_dir in attacker.special
        def_special = def_dir in defender.special
        
        piercing = (attacker.ability == "Piercing Attack")
        lucky = (attacker.ability == "Lucky Attack")
        
        if piercing:
            def_special = False # Ignore defender's arrow
            
        capture = False
        
        if atk_special and def_special:
            capture = True if lucky else False # Defender wins special ties unless Lucky
        elif atk_special and not def_special:
            capture = True # Unopposed special attack
        elif not atk_special and def_special:
            capture = False # Unopposed special block
        else:
            # Standard Combat
            atk_val = attacker.get_attack(is_last_round)
            def_val = defender.get_defense()
            
            if atk_val > def_val:
                capture = True
            elif atk_val == def_val:
                capture = True if lucky else False # Defender wins stat ties unless Lucky
                
        defender.receive_attack()
        
        if capture:
            defender.owner = attacker.owner

    def get_score(self):
        p1_score = p2_score = 0
        for row in self.board:
            for card in row:
                if card:
                    if card.owner == 1: p1_score += 1
                    elif card.owner == 2: p2_score += 1
        return {self.players[1]["name"]: p1_score, self.players[2]["name"]: p2_score}

    def check_win_condition(self):
        if self.turn > 9:
            return True
        return False

# --- CLI PLAYABLE LOOP ---
if __name__ == "__main__":
    game = TarockGame("Player 1", "Player 2", FULL_CARD_POOL)
    
    def print_board():
        print("\n--- BOARD ---")
        for y in range(3):
            row_str = []
            for x in range(3):
                card = game.board[y][x]
                if card:
                    row_str.append(f"[P{card.owner}:{card.name[:6]}]")
                else:
                    row_str.append(f"[ {x},{y}  ]")
            print(" ".join(row_str))
        print("-------------")

    print("Welcome to Arcadian Tarock CLI!")
    
    while not game.check_win_condition():
        print_board()
        cp = game.current_player
        player_name = game.players[cp]["name"]
        print(f"\n{player_name}'s Turn (Turn {game.turn})")
        
        # Show hand
        hand = game.players[cp]["hand"]
        for i, card in enumerate(hand):
            print(f"  {i}: {card.name} (Atk:{card.base_attack} Def:{card.base_defense} Ability:{card.ability})")
        
        try:
            choice = input(f"Choose card index (0-{len(hand)-1}) and x, y coordinates (e.g., '0 1 1'): ")
            c_idx, x, y = map(int, choice.split())
            game.play_card(cp, c_idx, x, y)
        except Exception as e:
            print(f"Invalid move: {e}. Try again.")

    print_board()
    scores = game.get_score()
    print("\nGAME OVER!")
    print(f"Final Scores: {scores}")
    if scores["Player 1"] > scores["Player 2"]:
        print("Player 1 Wins!")
    elif scores["Player 2"] > scores["Player 1"]:
        print("Player 2 Wins!")
    else:
        print("It's a Tie!")
