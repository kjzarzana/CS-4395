# CS-4395

See Overview of NLP [here](Overview_of_NLP.pdf)



## Text Processing With Python
Code is located [here](https://github.com/kjzarzana/CS-4395/blob/main/Person_Dict/main.py)

This program takes in employee account information from a csv file and catches any errors that might be found in the formatting of user IDs and phone numbers. The resulting data is then stored in a dictionary and re-displayed cleanly.

This program is run with a filepath as the only argument.
The program assumes data is stored in a file in a comma seperated list.   
For example:   
Last,First,Middle Initial,ID,Office phone  
Smith,Smitty,S,WH1234,5557771212

In this assignment I learned how to search for and reformat data within a file using regex. Python is a powerful tool for text processing because of it's vast libraries and readability.

## Guessing Game
Code is located [here](https://github.com/kjzarzana/CS-4395/blob/main/Guessing_Game/main.py)

This program reads in a text file and extracts all the nouns. The fifty most common nouns are then used in a guessing game where the user inputs a character at a time to figure out the word.

This program is run with a filepath as the only argument.
The file does not need to be formatted. The example I used is a textbook.

##N-grams
Code is located [here](https://github.com/kjzarzana/CS-4395/blob/main/N-gram/main.py)

This program constructs a basic language model using n-grams of various source texts in different languages. Once the dicitonaries are created, it reads each line of the LangId.test and determines the language of the text. When the model was tested on the 300 lines in LangId.test, it correctly guessed the language 97% of the time.

The pickle program is necessary to create the dictionaries that the main program will use.
