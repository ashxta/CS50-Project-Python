import random
def main():
     while True:
        print('GAME!')
        game = goGame()
        if game == 1 :
            RockPaperScissors()
        elif game == 2 :
            play_world_atlas()
        else:
            continue
        request = input('Do you want to carry on playing y/n? ').upper()
        if request in ['NO','N']:
            break
def goGame():
    try :
        n = int(input('Welcome to games, If you want to exit press CTRL + C\nSelect a game :\n- 1 for RockPaperScissors\n- 2 for World Atlas\nAnswer: '))
        if n not in [1,2]:
            raise Exception()
    except (ValueError,Exception):
        print('please Enter a Value 1 or 2')

    else :
        return n

def RockPaperScissors():
    print('Welcome to Rock Paper scissors')
    user = input("Please choose 'r' for rock, 's' for scissors, 'p' for paper\n")
    computer = random.choice(['r','p','s'])


    if user == computer:
        print('You tied!')
    elif is_win(user, computer):
        print('You won!')
    else:
        print('You lost!')

def is_win(player, player2):
    if (player == 'r' and player2 == 's') or (player == 's' and player2 == 'p') or (player == 'p' and player2 == 'r'):
        return True

world_atlas = {
    "France": "Paris",
    "Germany": "Berlin",
    "Italy": "Rome",
    "Spain": "Madrid",
    "United States": "Washington, D.C.",
    "India": "New Delhi",
    "Russia": "Moscow",
    "United Kingdom": "London",
    "Australia": "Canberra",
    "Maldives": "Male",
   "Egypt": "Cairo",
    "Netherlands": "Amsterdam",
    "Brazil": "Brasilia",
    "South Korea": "Seoul",
    "Qatar": "Doha",
    "Thailand": "Bangkok",
    "Malaysia": "Kuala Lumpur",
    "Norway": "Oslo",
    "Canada": "Ottawa",
    "Poland": "Warsaw",
    "Sweden": "Stockholm",
    "Taiwan": "Taipei",
    "Saudi Arabia": "Riyadh",
    "Argentina": "Buenos Aires",
    "China":"Beijing",
    "Indonesia":"Jakarta",
    "Greece":"Atehns",
    "Japan":"Tokyo",
}

# Function to choose a random country
def choose_country(atlas):
    country = random.choice(list(atlas.keys()))
    return country, atlas[country]

# Function to play the World Atlas game
def play_world_atlas():
    score = 0
    total_questions = 5

    print("Welcome to the World Atlas Game!")
    print(f"You will be asked to guess the capital of a country. You have {total_questions} questions.")

    for _ in range(total_questions):
        country, correct_answer = choose_country(world_atlas)
        print(f"What is the capital of {country}?")
        user_answer = input("Your answer: ")

        if user_answer.lower() == correct_answer.lower():
            print("Correct!")
            score += 1
        else:
            print(f"Sorry, the correct answer is {correct_answer}.")

    print(f"Game over! Your score is {score}/{total_questions}.")


if __name__ == "__main__":
    main()
