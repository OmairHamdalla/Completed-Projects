import random
import time

class Card:
    ranks = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
    suits = ["Hearts", "Diamonds", "Clubs", "Spades"]

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f"{self.rank} of {self.suit}"


class Deck:
    def __init__(self):
        self.cards = [Card(rank, suit) for rank in Card.ranks for suit in Card.suits]
        random.shuffle(self.cards)

    def draw_card(self):
        if len(self.cards) > 0:
            return self.cards.pop()
        else:
            return None


class Game:
    def __init__(self):
        self.deck = Deck()

    def again(self):
        choice = input("Want to start again? (y/n)")
        if choice == 'y': self.play()
        else: exit()

    def play(self):
        print('''
        Welcome to the Card Game!\n
        1. Bidding: Compare the ranks of the drawn cards. Highest rank wins.\n
        2. Higher or Lower: Guess if the next card will be higher or lower than the current card.\n
        3. Blackjack: Try to get as close to 21 without going over. Face cards are worth 10.
              ''')
        choice = input("Choose a game -> ")
                

        if choice == "1":   game = Bidding(self.deck)
        elif choice == "2": game = HigherLower(self.deck)
        elif choice == "3": game = Blackjack(self.deck)            
        else:
            print("Invalid choice. Exiting the game.")
            time.sleep(3)
            exit()

        print("Game Started !")
        game.start()
        self.again()
        time.sleep(3)


class Bidding:
    def __init__(self, deck):
        self.deck = deck

    def start(self):

        player_card = self.deck.draw_card()
        computer_card = self.deck.draw_card()

        print("Player's card: ", player_card)
        print("Computer's card: ", computer_card)

        player_rank_index = Card.ranks.index(player_card.rank)
        computer_rank_index = Card.ranks.index(computer_card.rank)

        if player_rank_index > computer_rank_index:
            print("Player wins!")
        elif player_rank_index < computer_rank_index:
            print("Computer wins!")
        else:
            print("It's a tie!")

class HigherLower:
    def __init__(self, deck):
        self.deck = deck
        self.current_card = None
        self.score = 0

    def start(self):
        while True:
            if self.current_card is None:
                self.current_card = self.deck.draw_card()
                print("Current card: ", self.current_card)
            
            next_card = self.deck.draw_card()
            
            guess = input("\nWill the next card be higher (h) or lower (l)? ")

            if guess.lower() == "h":
                print("Next card:", next_card)
                if Card.ranks.index(next_card.rank) > Card.ranks.index(self.current_card.rank):
                    self.score += 1
                    print("Correct! Your score:", self.score)
                    self.current_card = next_card
                else:
                    print("Wrong! Game over, Your final score: ", self.score)
                    break

            elif guess.lower() == "l":
                print("Next card:", next_card)
                if Card.ranks.index(next_card.rank) < Card.ranks.index(self.current_card.rank):
                    self.score += 1
                    print("Correct! Your score:", self.score)
                    self.current_card = next_card
                else:
                    print("Wrong! Game over, Your final score:", self.score)
                    break

            else:
                print("Invalid choice. Please enter 'h' or 'l'.")
            
class Blackjack:
    def __init__(self, deck):
        self.deck = deck
        self.player_cards = []
        self.computer_cards = []

    def start(self):
        
        # Deal initial cards to player and computer
        self.player_cards = [self.deck.draw_card(), self.deck.draw_card()]
        self.computer_cards = [self.deck.draw_card(), self.deck.draw_card()]

        print("Player's cards: ", ", ".join(str(card) for card in self.player_cards))
        print("Computer's cards: ", ", ".join(str(card) for card in self.computer_cards[:1]), "and one hidden card.")

        # Player's turn
        while True:
            choice = input("Do you want to hit (h) or stand (s)? ")

            if choice.lower() == "h":
                new_card = self.deck.draw_card()
                self.player_cards.append(new_card)
                print("Player draws:", new_card)
            elif choice.lower() == "s":
                break
            else:
                print("Invalid choice. Please enter 'h' or 's'.")

            player_total = self.get_total_value(self.player_cards)
            print("Player's total:", player_total)

            if player_total > 21:
                print("Player busts! Computer wins!")
                return

        # Computer's turn
        while self.get_total_value(self.computer_cards) < 17:
            new_card = self.deck.draw_card()
            self.computer_cards.append(new_card)
            print("Computer draws:", new_card)

        computer_total = self.get_total_value(self.computer_cards)
        print("Computer's total:", computer_total)

        # Compare hands
        if computer_total > 21:
            print("Computer busts! Player wins!")
        elif player_total > computer_total:
            print("Player wins!")
        elif player_total < computer_total:
            print("Computer wins!")
        else:
            print("It's a tie!")

    def get_total_value(self, cards):
        total = 0
        num_aces = 0

        for card in cards:
            if card.rank == "Ace":
                total += 11
                num_aces += 1
            elif card.rank in ["Jack", "Queen", "King"]:
                total += 10
            else:
                total += int(card.rank)

        while total > 21 and num_aces > 0:
            total -= 10
            num_aces -= 1

        return total