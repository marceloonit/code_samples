
import getpass


secret_word = getpass.getpass('Enter the word to be played with: ')
length_word = len(secret_word)
tentativas = length_word

while True:
    guess = input('Enter a letter: ')
    
    if len(guess) != 1:
        continue

    if guess in secret_word:
        print('JA')
    else:
        tentativas -= 1
        print('Nope, you still have more ' + str(tentativas) + 'shots!')

    if tentativas == 0:
        print("you ran out of shots")
        break

print("game over")
