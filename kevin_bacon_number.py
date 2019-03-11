import psycopg2
# Parameters for accessing movies db
params = {
  'dbname': 'movies',
  'user': 'dsujanto'
}

### Set up connection
conn = psycopg2.connect(**params) # Create a connection object
cur = conn.cursor() # Create cursor object

print("Let's find Kevin Beacon!")
guess = input("Enter an actor name: ")
print(guess)
sql = """SELECT m.title, a.name, b.name from movies m, actors a, movies_actors ma,actors b, movies_actors ma2
         where m.movie_id = ma.movie_id and a.actor_id = ma.actor_id and b.actor_id = ma2.actor_id and m.movie_id =
         ma2.movie_id and b.name like '%s'""" % guess

cur.execute(sql)

#record = cur.fetchall()

print("Executing SQL...")

### Gather results
movie_list = [] # Initialize a list with one count per movie title in db
found = False
first = True
for rec in cur: # Loop through records in cursor object
    print (rec[0],rec[1])
    if rec[1]=='Kevin Bacon':
        if first:
            print ("Kevin Bacon found return 1")         
        else:
             print("Kevin Bacon found return 2")
        found = True
        break
    first = False

if not found:
    print ("Not found Kevin Bacon")

#movie_list.append(rec[0]) # and append them to movie list.

cur.close()

