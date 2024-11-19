import random

def get_computer_choice():
    """Generate a random choice for the computer."""
    return random.choice(['rock', 'paper', 'scissors'])

def determine_winner(user_choice, computer_choice):
    """Determine the winner based on user and computer choices."""
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "user"
    else:
        return "computer"

def display_result(user_choice, computer_choice, winner):
    """Display the result of the round."""
    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    if winner == "tie":
        print("It's a tie!")
    elif winner == "user":
        print("You win this round!")
    else:
        print("Computer wins this round!")

def play_game():
    """Main game function."""
    print("Welcome to Rock, Paper, Scissors!")
    print("Instructions: Enter 'rock', 'paper', or 'scissors' to play. Type 'quit' to end the game.")
    
    user_score = 0
    computer_score = 0

    while True:
        # Prompt user for their choice
        user_choice = input("\nEnter your choice (rock/paper/scissors): ").lower()
        if user_choice == 'quit':
            print("\nThanks for playing! Final Scores:")
            print(f"You: {user_score}")
            print(f"Computer: {computer_score}")
            break

        if user_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid choice. Please choose 'rock', 'paper', or 'scissors'.")
            continue

        # Generate computer choice
        computer_choice = get_computer_choice()

        # Determine the winner
        winner = determine_winner(user_choice, computer_choice)

        # Update scores
        if winner == "user":
            user_score += 1
        elif winner == "computer":
            computer_score += 1

        # Display the result
        display_result(user_choice, computer_choice, winner)

        # Display current scores
        print(f"Scores: You - {user_score}, Computer - {computer_score}")

        # Ask if the user wants to play another round
        play_again = input("\nDo you want to play another round? (yes/no): ").lower()
        if play_again != 'yes':
            print("\nThanks for playing! Final Scores:")
            print(f"You: {user_score}")
            print(f"Computer: {computer_score}")
            break

# Run the game
play_game()
