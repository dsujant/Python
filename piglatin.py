# -*- coding: utf-8 -*-
"""
Created on Sat Jul  7 17:08:46 2018

@author: diana

Pig Latin Game

This program will ask the user to enter a word with characters only 
and convert it into lowercase. Then, it will move the first character of 
the word and append 'ay' at the end of the word. 
For example, the word 'python' will become 'ythonpay' 

"""
playgame = True
counter=0
while playgame ==True:
    print("Let's play Pig Latin!")
    pyg = 'ay'
    original =input('Enter a word (all letters, please):')
    if len(original) > 0 and original.isalpha():
        counter=0
        print("Your word is: " + original)
        word = original.lower()
        first = word[0]
        new_word = word + first + pyg
        new_word = new_word[1:len(new_word)]
        print("The new word is: " + new_word)
        print("Do you want to play again?")
        response =input("Enter 'Y' if you want to play again, 'N' if you decide to quit the game: ")
        if response.lower() == 'n':
            playgame =False
    else:
        counter+=1;
        print("You either did not enter a word or the word contains numbers")
        if (counter==3):
            print("Do you still want to play?")
            response =input("Enter 'Y' if you still want to play, 'N' if you decide to quit the game: ")
            if response.lower() == 'n':
                playgame =False
            else:
                counter=0
        #if len(original) = 0:
        #original =input('Enter a word (all letters, please):')
        #print("Your word is: " + original)
        #word = original.lower()
        #first = word[0]
        #new_word = word + first + pyg
        #new_word = new_word[1:len(new_word)]
        #print("The new word is: " + new_word)
        #print("Do you want to play again?")
        #response =input("Enter 'Y' if you want to play again, 'N' if you decide to quit the game: ")
        #if response.lower() == 'n':
        #    playgame =False
print("Thanks for playing!")