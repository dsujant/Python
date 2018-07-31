# -*- coding: utf-8 -*-
"""
Created on Sun Jul  8 13:17:34 2018

@author: diana

This program will roll a pair of dice and add values of the roll.  
Then, it will ask the user to guess the number.  The program will compare
the user's guess to the total value and determine the winner (user or 
computer)

"""
from random import randint
from time import sleep

def get_user_guess():
  print ("Let's play Number Guess! If your guess is greater than the sum of "
         "both rolling dice numbers, you win!"
         )
  guess = int(input("Guess a number: "))
  return guess

def roll_dice(number_of_sides):
  first_roll = randint(1, number_of_sides)
  second_roll = randint(1, number_of_sides)
  max_val = number_of_sides * 2
  #print ("The maximum possible value is: %d" % max_val)
  guess = get_user_guess()
  if guess > max_val:
    print ("Your guess is invalid!")
  else:
    print ("Rolling ...")
    sleep(2)
    print ("The first roll is: %d" %first_roll)
    sleep(1)
    print ("The second roll is: %d" %second_roll)
    sleep(1)
    total_roll = first_roll + second_roll
    print ("Total Roll : %d" %total_roll)
    print ("Result ...")
    sleep(1)
    if guess > total_roll:
      print ("You won! Congratulations!")
    else:
      print ("You lost this time.  Better luck next time!")
    
roll_dice(6)
  