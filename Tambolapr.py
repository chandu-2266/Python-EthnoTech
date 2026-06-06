import random

class TambolaGame:
    def __init__(self):
        self.numbers = list(range(1, 91))
        self.drawn_numbers = []
        self.tickets = {}
        self.winners = {'top_line': None, 'middle_line': None, 'bottom_line': None, 'full_house': None}
    
    def create_ticket(self, player_name):
        """Create a random ticket for a player"""
        ticket = []
        for _ in range(3):
            row = sorted(random.sample(range(1, 91), 5))
            ticket.append(row)
        self.tickets[player_name] = ticket
        return ticket
    
    def display_ticket(self, player_name):
        """Display a player's ticket"""
        ticket = self.tickets[player_name]
        print(f"\n{player_name}'s Ticket:")
        for row in ticket:
            print(row)
    
    def draw_number(self):
        """Draw a random number"""
        if len(self.drawn_numbers) < 90:
            num = random.choice([n for n in self.numbers if n not in self.drawn_numbers])
            self.drawn_numbers.append(num)
            return num
        return None
    
    def check_line(self, player_name, line_num):
        """Check if a player has completed a line"""
        ticket = self.tickets[player_name]
        if line_num < 3:
            return all(num in self.drawn_numbers for num in ticket[line_num])
        return False
    
    def check_full_house(self, player_name):
        """Check if a player has completed full house (all 15 numbers)"""
        ticket = self.tickets[player_name]
        all_numbers = sum(ticket, [])
        return all(num in self.drawn_numbers for num in all_numbers)
    
    def play(self, num_players):
        """Start the game"""
        print("=== TAMBOLA GAME ===\n")
        
        # Create tickets for players
        for i in range(num_players):
            player_name = f"Player {i + 1}"
            self.create_ticket(player_name)
            self.display_ticket(player_name)
        
        # Draw numbers
        print("\n=== Drawing Numbers ===")
        while len(self.drawn_numbers) < 90:
            num = self.draw_number()
            print(f"Number drawn: {num}")
            
            # Check for winners
            for player_name in self.tickets:
                if self.winners['top_line'] is None and self.check_line(player_name, 0):
                    self.winners['top_line'] = player_name
                    print(f"🎉 {player_name} completed TOP LINE!")
                
                if self.winners['middle_line'] is None and self.check_line(player_name, 1):
                    self.winners['middle_line'] = player_name
                    print(f"🎉 {player_name} completed MIDDLE LINE!")
                
                if self.winners['bottom_line'] is None and self.check_line(player_name, 2):
                    self.winners['bottom_line'] = player_name
                    print(f"🎉 {player_name} completed BOTTOM LINE!")
                
                if self.winners['full_house'] is None and self.check_full_house(player_name):
                    self.winners['full_house'] = player_name
                    print(f"🎉🎉🎉 {player_name} got FULL HOUSE! 🎉🎉🎉")
                    return
            
            input("Press Enter to draw next number...")
        
        print("\n=== GAME OVER ===")
        print(f"Winners: {self.winners}")

if __name__ == "__main__":
    game = TambolaGame()
    num_players = int(input("Enter number of players: "))
    game.play(num_players)
