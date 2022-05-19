#import requests
import random
movies = {"Title":"Back to the Future","Year":"1985","Rated":"PG","Released":"03 Jul 1985","Runtime":"116 min","Genre":"Adventure, Comedy, Sci-Fi","Director":"Robert Zemeckis","Writer":"Robert Zemeckis, Bob Gale","Actors":"Michael J. Fox, Christopher Lloyd, Lea Thompson","Plot":"Marty McFly, a 17-year-old high school student, is accidentally sent thirty years into the past in a time-traveling DeLorean invented by his close friend, the eccentric scientist Doc Brown.","Language":"English","Country":"United States","Awards":"Won 1 Oscar. 22 wins & 25 nominations total","Poster":"https://m.media-amazon.com/images/M/MV5BZmU0M2Y1OGUtZjIxNi00ZjBkLTg1MjgtOWIyNThiZWIwYjRiXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_SX300.jpg","Ratings":[{"Source":"Internet Movie Database","Value":"8.6/10"},{"Source":"Rotten Tomatoes","Value":"96%"},{"Source":"Metacritic","Value":"87/100"}],"Metascore":"87","imdbRating":"8.6","imdbVotes":"1,157,214","imdbID":"tt0088763","Type":"movie","DVD":"17 Aug 2010","BoxOffice":"$212,836,762","Production":"N/A","Website":"N/A","Response":"True"}
#API_KEY = "66d33a33"
#movie_title = 'Back To The Future'
#data = f'httpd://www.ombapi.com/?apikey={API_KEY}&t={movie_title}'
#response = requests.get(data).json()

def whatIs(m, t):
  if t == 'Title':
    autoSentence(m, t, f"{m[t]}")
  if t == 'Released':
    autoSentence(m,t,f"This movie was released was released {m[t]}.")
  if t == 'Actors':
    temp = getRandom("acclaiemed", "popular", " ")
    autoSentence(m, t, f"This movie stars {temp} actors: {m[t]}.")
  if t == 'Plot':
    autoSentence(m, t, f"The {t} of the movie is: {m[t]}")
  if t == 'Director':
    temp = getRandom("brilliant", "dashing", "marvelous")
    autoSentence(m, t, f"This {temp} movie's {t} is {m[t]}.")
  if t == 'Rating':
    autoSentence(m, t, f"")
    
    
    
def autoSentence(m, t, sentence):
  print(t + ": " + sentence)

def blog(movies):
  headLine(movies)
  for thing in movies:
    whatIs(movies, thing)

def headLine(m):
  temp = getRandom(f"Here are some fact about {m['Title']}!", f"Let's look back on {m['Title']}!", f"{m['Title']} is a classic!")
  print(temp)
  print()

def getRandom(c1, c2, c3):
  if (c2 != " " and c3 != " "):
    ran = random.randint(0, 2)
    if ran == 0:
      return c1
    elif ran == 1:
      return c2
    else:
      return c3
  elif(c3 != ""):
    ran = random.randint(0, 1)
    if ran == 0:
      return c1
    elif ran == 1:
      return c2
      
blog(movies)

