# Kyle Zarzana KJZ190000
# CS 4395.001
# Professor Karen Mazidi
# 9/25/22


from nltk import *
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from random import seed
from random import randint

seed(1234)


# This method reads in the file at specified filepath
def method1(filepath):
    with open(os.path.join(os.getcwd(), filepath), 'r') as f:
        f.readline()
        text_in = f.read()

    return text_in

# Calculates lexical diversity
def lexical_diversity(text):
    print('Lexical Diversity: ')
    print(len(set(text)) / len(text))

# tokenizes and extracts list of nouns from given text
def process_text(text):
    tokens = word_tokenize(text)
    tokens = (t.lower() for t in tokens)

    tokens = [t for t in tokens if t.isalpha() and t not in stopwords.words('english') and len(t) > 5]
    wnl = WordNetLemmatizer()
    lemmas = [wnl.lemmatize(t) for t in tokens]
    tags = pos_tag(lemmas)
    print(tags[:20])
    nouns = [n[0] for n in tags if n[1] == 'NN']
    print('Number of tokens: ')
    print(len(tokens))

    print('Number of nouns: ')
    print(len(nouns))

    return nouns, tokens


def guessing_game(words):
    user_points = 5
    ans = words[randint(0, 50)]
    guesses = []

    while user_points >= 0:

        num_underscores = 0

        # Prints known letters and blanks
        for char in ans:
            if char in guesses:
                print(char, end=" ")
            else:
                print('_', end=" ")
                num_underscores += 1

        # Win condition, no more underscores are printed
        if num_underscores == 0:
            print('\nYou Win!')
            again = input('Play again? (y/n)')
            if again == 'y':
                guessing_game(words)
            else:
                exit()

        # Input guess
        user_guess = input("\nInput a letter:").lower()
        guesses.append(user_guess)

        # Exit game
        if user_guess == '!':
            exit()

        # Correct guess
        elif user_guess in ans:
            print('Right!')
            user_points += 1
        # Wrong guess
        else:
            print('Wrong!')
            user_points -= 1
        print('You have', user_points, 'points.')

        # If user runs out of guesses
        if user_points < 0:
            print('You lose!')
            again = input('Play again? (y/n)')

            if again == 'y':
                guessing_game(words)
            else:
                exit()


if __name__ == '__main__':
    # Reads argument as filename
    if len(sys.argv) < 2:
        print('Please enter a filename as a system arg')
    else:
        fp = sys.argv[1]
        text_in = method1(fp)
        lexical_diversity(text_in)
        nouns, tokens = process_text(text_in)

        # creates dict of nouns:number of times in text
        noun_count = {}
        for noun in nouns:
            if noun not in noun_count:
                noun_count[noun] = 1
            else:
                noun_count[noun] += 1

        most_common = []
        i = 0
        # Print the 50 most common words and their counts
        for word in sorted(noun_count, key=noun_count.get, reverse=True):
            if i == 50:
                break
            print(word, ':', noun_count[word])
            most_common.append(word)
            i += 1

        guessing_game(most_common)
