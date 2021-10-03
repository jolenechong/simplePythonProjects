from PIL import Image

'''
hangman
time taken: 30mins on base form (no hangman image, no game won no games left)
1h45min for whole project

todos:
- guess letter OR whole word
'''

hangman = {
    1:[
    "-------",
    "      ▓",
    "      ▓",
    "      ▓",
    "      ▓",
    "      ▓",
    "-------",
    ],
    2:[
    "-------",
    "  |    ▓",
    "       ▓",
    "       ▓",
    "       ▓",
    "       ▓",
    "-------",
    ],
    3:[
    "-------",
    "  |    ▓",
    "  ☺    ▓",
    "       ▓",
    "       ▓",
    "       ▓",
    "-------",
    ],
    4:[
    "-------",
    "  |    ▓",
    " \☺    ▓",
    "       ▓",
    "       ▓",
    "       ▓",
    "-------",
    ],
    5:[
    "-------",
    "  |    ▓",
    " \☺/   ▓",
    "       ▓",
    "       ▓",
    "       ▓",
    "-------",
    ],
    6:[
    "-------",
    "  |    ▓",
    " \☺/   ▓",
    "  |    ▓",
    "       ▓",
    "       ▓",
    "-------",
    ],
    7:[
    "-------",
    "  |    ▓",
    " \☺/   ▓",
    "  |    ▓",
    " /     ▓",
    "       ▓",
    "-------",
    ],
    8:[
    "-------",
    "  |    ▓",
    " \☺/   ▓",
    "  |    ▓",
    " / \   ▓",
    "       ▓",
    "-------",
    ],

}

def main():
    word = str(input('Enter the word to guess: '))
    word = word.lower()
    start = input('Enter (E) to start: ')

    if start == 'e' or start == 'E':
        guess_the_word(word)

def guess_the_word(word):
    letterList = []
    currentWord = []
    gameWon = False
    hangmanCount = 1

    # store word in a list by each letter
    # append _ to current word depending on how many letters are in the word
    for letter in word:
        letterList.append(letter)
        currentWord.append("_")

    while True:
        roundWon = False
        if gameWon == True:
            print('\nYAY! You won!')
            im = Image.open("YAY.jpg")
            im.show()
            break
        else:
            letterGuessed = str(input('Guess a letter:'))
            letterGuessed = letterGuessed.lower()

            # if guessed correctly append currentWord
            count = 0
            for letter in letterList:
                if letterGuessed == letter:
                    currentWord[count]=letterGuessed
                    roundWon = True
                count +=1

            if "_" not in currentWord:
                gameWon = True

            if roundWon == False:
                hangmanCount += 1

            print(hangman.get(hangmanCount, 'error')[0])
            print(hangman.get(hangmanCount, 'error')[1])
            print(hangman.get(hangmanCount, 'error')[2])
            print(hangman.get(hangmanCount, 'error')[3])
            print(hangman.get(hangmanCount, 'error')[4])
            print(hangman.get(hangmanCount, 'error')[5])
            print(hangman.get(hangmanCount, 'error')[6])
            print("CURRENT WORD:\n", "".join(map(str, currentWord)))
            turnsleft = 10 - hangmanCount
            print(f"You have {turnsleft} turns left\n")

main()