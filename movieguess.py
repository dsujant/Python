# -*- coding: utf-8 -*-
"""
Created on Fri Sep 28 08:29:18 2018
@author: diana
"""
import psycopg2

# Parameters for accessing movies db

def findmoviegenre(movieguess): 
    """
    This function handles the logic and queries for the game. It begins by 
    making a single SQL query to the movies db and look for similar movies and genre requested
    by the user.
    """
    #This query returns a list of similar movies entered by the user
    SQL = """SELECT distinct m.title
             FROM movies m, genres g 
             WHERE cube_ur_coord(genre, position) > 0 and m.title %% '%s'
             ORDER BY m.title LIMIT 10 """ 
    
    cur.execute(SQL % movieguess) #Executes Query
    rowcount = cur.rowcount
    if rowcount == 0:
        print ('No similar movies found')
        return
    
    for rec in cur: #Loop through records in cursor object
        print ("We found similar movies: ", rec[0]) #Details  
        
   
    findgenre = input("Enter your choice: ")
    SQL2 = """SELECT title, cube_distance(genre, g) dist 
              FROM movies, 
              (SELECT genre g FROM movies WHERE title %% '%s') a ORDER BY dist LIMIT 10; """ 
    cur.execute(SQL2 % findgenre)         
    
    for rec in cur: #Loop through records in cursor object
        print (" Similar Movies: ", rec[0]) #Details  
        
    cur.close()
    
    return #End function


#Program starts here
#Setup param
params = {
  'dbname': 'movies',
  'user': 'dsujanto'
}

### Set up connection
conn = psycopg2.connect(**params) # Create a connection object
cur = conn.cursor() # Create cursor object

### Start the game and take user input
print("Please enter a movie!")
movieguess = input("Enter movie: ")
findmoviegenre(movieguess)