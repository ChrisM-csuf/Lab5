

"""
the program will translate a sentence that is given via user input
we need to read the data of the .txt file
from that data we create a laist of strings 
use that list of strings to create a dictionary
close the file

we make a translate function that works by splitting the user input into a list of strings.

once we have a list of strings, we loop through each word in the list and check it against the dictionary to see if it exists as a words that can be 
translated

replace the list items with the translated words and print the entire thing back to the user.
"""

"""
main():
    set dictionary = translate ()
    translate()

translate():
    print out the translated sentence

create_dictionary():
    read in textese.txt
    create list = each line in the file
    close the file
    create dict off the list
    return dict
"""

def main():
    sentence = input("enter a sentence: ")
    dictionary = create_dictionary('textese.txt')
    translate(sentence, dictionary)

def create_dictionary(txt_file):
    infile = open(txt_file, 'r')
    words = [word.rstrip() for word in infile]
    infile.close()
    return dict([word.split(',') for word in words])

def translate(sentence, dictionary):
    words = sentence.split()
    for word in words:
        print(dictionary.get(word, word), " ", end="")

main()
