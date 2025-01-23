# Twój pomysł: 1.0 jammer 

# Wygenerowany kod
import random

def play_game():
    number_to_guess = random.randint(1, 100)
    attempts = 0
    print('Zgadnij liczbę od 1 do 100.')
    
    while True:
        try:
            guess = int(input('Twoja próba: '))
            attempts += 1
            if guess < number_to_guess:
                print('Za mało!')
            elif guess > number_to_guess:
                print('Za dużo!')
            else:
                print(f'Brawo! Zgadłeś liczbę {number_to_guess} w {attempts} próbach.')
                break
        except ValueError:
            print('Proszę wprowadzić liczbę.')

if __name__ == '__main__':
    play_game()