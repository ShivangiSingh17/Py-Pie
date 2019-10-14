#Write a program (using functions!) that asks the user for a long string containing multiple words. 
#Print back to the user the same string, except with the words in backwards order. For example, say I type the string:
#My name is Michele
#Then I would see the string:
#Michele is name My


def show_words_reverse():

    print("Please enter long string containing multiple words")
    text = input()
    
    words = text.split()
    words.reverse()

    for i in range(len(words)):
    	words[i] += " "
    words[len(words)-1] = words[len(words)-1][:-1]

    text_back = ""
    text_back = text_back.join(words)
    print(text_back)

show_words_reverse("Please enter long string containing multiple words")