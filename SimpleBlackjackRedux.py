import random
import sys
import pygame
import os

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Fonts
font = pygame.font.Font(None, 36)
small_font = pygame.font.Font(None, 24)

# Load background image
try:
    background = pygame.image.load('image.jpg')
    background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))
except pygame.error:
    print("Could not load image.jpg. Using solid color background instead.")
    background = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
    background.fill((34, 139, 34))  # Forest green background

# Move a card from deck to hand
def draw_card(hand: list[str], deck: list[str]) -> None:
    hand.append(deck.pop())  # take last card from deck

# calculate the score of the hand
def calculate_score(hand: list[str]) -> int:
    score = 0
    has_ace = False

    for card in hand:
        try:
            ival = int(card)
            score += ival
        except ValueError:
            # not a number card
            if card == "A":  # ace
                has_ace = True
            else:  # face card
                score += 10

    if has_ace:
        # treat ace as 11 if it doesn't bust, otherwise 1
        if (score + 11) > 21:
            score += 1
        else:
            score += 11

    return score

def draw_text(screen, text, font, color, x, y):
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))

def main():
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Blackjack")

    clock = pygame.time.Clock()

    deck: list[str] = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"] * 4  # 4 decks
    player_cards: list[str] = []
    dealer_cards: list[str] = []

    # shuffle the deck
    random.shuffle(deck)

    # Initial deal
    draw_card(dealer_cards, deck)
    draw_card(player_cards, deck)
    draw_card(player_cards, deck)

    game_state = "playing"  # playing, dealer_turn, game_over
    message = ""

    running = True
    while running:
        screen.blit(background, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if game_state == "playing":
                    if event.key == pygame.K_h:  # Hit
                        draw_card(player_cards, deck)
                        if calculate_score(player_cards) > 21:
                            message = "You busted! You lose!"
                            game_state = "game_over"
                    elif event.key == pygame.K_s:  # Stay
                        game_state = "dealer_turn"
                    elif event.key == pygame.K_q:  # Quit
                        running = False
                elif game_state == "dealer_turn":
                    # Dealer draws
                    while calculate_score(dealer_cards) < 17:
                        draw_card(dealer_cards, deck)
                    game_state = "game_over"
                    player_score = calculate_score(player_cards)
                    dealer_score = calculate_score(dealer_cards)
                    if dealer_score > 21:
                        message = "Dealer busts! You win!"
                    elif dealer_score > player_score:
                        message = "Dealer wins!"
                    elif dealer_score < player_score:
                        message = "You win!"
                    else:
                        message = "It's a tie!"
                elif game_state == "game_over":
                    if event.key == pygame.K_r:  # Restart
                        # Reset game
                        deck = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"] * 4
                        random.shuffle(deck)
                        player_cards = []
                        dealer_cards = []
                        draw_card(dealer_cards, deck)
                        draw_card(player_cards, deck)
                        draw_card(player_cards, deck)
                        game_state = "playing"
                        message = ""
                    elif event.key == pygame.K_q:  # Quit
                        running = False

        # Draw text
        draw_text(screen, f"Player's total: {calculate_score(player_cards)}", font, WHITE, 50, 50)
        draw_text(screen, f"Player's cards: {', '.join(player_cards)}", small_font, WHITE, 50, 90)

        draw_text(screen, f"Dealer's total: {calculate_score(dealer_cards)}", font, WHITE, 50, 150)
        draw_text(screen, f"Dealer's cards: {', '.join(dealer_cards)}", small_font, WHITE, 50, 190)

        if game_state == "playing":
            draw_text(screen, "Press H to Hit, S to Stay, Q to Quit", small_font, BLUE, 50, 250)
        elif game_state == "dealer_turn":
            draw_text(screen, "Dealer is drawing...", small_font, BLUE, 50, 250)
        elif game_state == "game_over":
            draw_text(screen, message, font, GREEN if "win" in message else RED, 50, 250)
            draw_text(screen, "Press R to Restart, Q to Quit", small_font, BLUE, 50, 300)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit(0)

if __name__ == "__main__":
    main()
