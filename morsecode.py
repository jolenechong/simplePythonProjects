'''
morse code generator
- each word separated with spaces worth 7 .
- each letter separated with spaces worth 3 .

time taken: 1h 30mins
date: 2nd october 2021
'''

morseCodeDictionary = { 'a':'.-', 'b':'-...','c':'-.-.','d':'-..','e':'.',
                        'f':'..-.', 'g':'--.','h':'....','i':'..','j':'.---','k':'-.-',
                        'l':'.-..','m':'--','n':'-.','o':'---','p':'.--.','q':'--.-', 'r':'.-.','s':'...','t':'-',
                        'u':'.._','v':'..._', 'w':'.__','x':'_.._','y':'_.__','z':'__..',
                        '1':'.----','2':'..---','3':'...--','4':'....-','5':'.....','6':'-....',
                        '7':'--...','8':'---..','9':'----.','0':'-----'
                        }

def main():
    while True:
        print('Morse code generator')
        print("Each word is separated with spaces worth 7 '.' and each letter is separated with spaces worth 3 '.'\n? ! and , are ignored\n---")
        start = input('Encode(E) or Decode(D): ')
        if start == 'e' or start == 'E':
            words = input('Enter text/sentence you would like to turn into morse code: ')
            encodeMorseCode(words)
            break
        elif start == 'd' or start == 'D':
            words = input('Enter morse code: ')
            decodeMorseCode(words)
            break
        else:
            print('Please enter a correct input.')


def encodeMorseCode(words):
    encodedSentence = []
    # change all characters to lowercase so that it can be searched in the dictionary
    words = words.lower()
    for word in words:
        if word == '?' or word =='!' or word == ',':
            # ignore these characters by turning them into blanks -> ""
            word = ""
        elif word != " ":
            word = morseCodeDictionary.get(word, 'error ')
        else:
            # leave 7 spaces between each word
            word = "       "
        encodedSentence.append(word)

    print('   '.join(map(str,encodedSentence)))

def decodeMorseCode(words):
    global answer

    answerList = []
    decoding = []
    space = []
    # add a space to end of string, this is so that the last character is not missed
    words = words + " " + " " + " "

    for char in words:
        if char == " ":
            space.append('')
        else:
            decoding.append(char)

        if len(space) == 3:
            # 3 spaces separates each character so each time spaces becomes 3 store everything in current list in finalWord and clear list again
            finalWord = decoding
            # finalWord is morsecode for 1 word but its in a list, join them tgt to a string
            finalWord = ''.join(map(str, finalWord))

            if finalWord != '':
                answer = list(morseCodeDictionary.keys())[list(morseCodeDictionary.values()).index(finalWord)]
                answerList.append(answer)
            else:
                answerList.append(' ')
            decoding = []
            space = []

    answerList = ''.join(map(str, answerList))
    print(answerList)

main()
