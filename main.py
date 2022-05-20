#import requests
import random
movies = {"Title":"Back to the Future","Year":"1985","Rated":"PG","Released":"03 Jul 1985","Runtime":"116 min","Genre":"Adventure, Comedy, Sci-Fi","Director":"Robert Zemeckis","Writer":"Robert Zemeckis, Bob Gale","Actors":"Michael J. Fox, Christopher Lloyd, Lea Thompson","Plot":"Marty McFly, a 17-year-old high school student, is accidentally sent thirty years into the past in a time-traveling DeLorean invented by his close friend, the eccentric scientist Doc Brown.","Language":"English","Country":"United States","Awards":"Won 1 Oscar. 22 wins & 25 nominations total","Poster":"https://m.media-amazon.com/images/M/MV5BZmU0M2Y1OGUtZjIxNi00ZjBkLTg1MjgtOWIyNThiZWIwYjRiXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_SX300.jpg","Ratings":[{"Source":"Internet Movie Database","Value":"8.6/10"},{"Source":"Rotten Tomatoes","Value":"96%"},{"Source":"Metacritic","Value":"87/100"}],"Metascore":"87","imdbRating":"8.6","imdbVotes":"1,157,214","imdbID":"tt0088763","Type":"movie","DVD":"17 Aug 2010","BoxOffice":"$212,836,762","Production":"N/A","Website":"N/A","Response":"True"}
#API_KEY = "66d33a33"
#movie_title = 'Back To The Future'
#data = f'httpd://www.ombapi.com/?apikey={API_KEY}&t={movie_title}'
#response = requests.get(data).json()
#Could not make this working. However if it were intergrated into the code I would be able to make a 'blog'for any movie Even if it is missing something.


def whatIs(m, t):
  try:
    if t == 'Title':
      autoSentence(m, t, f"{m[t]}")
    elif t == 'Released':
      temp = movies['Released']
      temp = temp[7:11]
      if(temp == "2022"):
        autoSentence(t,f"{m['Title']} was released was released {m[t]} which was released this year.")
      else:
        autoSentence(t,f"{m['Title']} was released was released {m[t]}.")
    elif t == 'Actors':
      temp = getRandom("acclaiemed", "popular", " ")
      autoSentence(t, f"{m['Title']} stars {temp} actors: {m[t]}.")
    elif t == 'Plot':
      autoSentence(t, f"The {t} of the {m['Title']} is: {m[t]}")
    elif t == 'Director':
      temp = getRandom("brilliant", "dashing", "marvelous")
      autoSentence(t, f"The {temp} {t} {m[t]} directed {m['Title']}.")
    elif t == 'Metascore':
      temp = m[t]
      if int(temp) == 100:
        autoSentence(t, f"{m['Title']} has a perfect {t} score of {temp}%!")
      elif int(temp[0]) <= 6:
        autoSentence(t, f"{m['Title']} has a terrible {t} level is {temp}%. Spend your time on another film.")
      elif int(temp[0]) >= 7:
        autoSentence(t, f"The {t} of {m['Title']} is {temp}. I siggest that you watch this.")
    elif t == 'Awards':
      autoSentence(t, f"{m['Title']} has recived {m[t]} for {t}.")
    elif t =='Writer':
      temp = getRandom("talented", "fabulous", " ")
      autoSentence(t, f"The {t} of {m['Title']} is the {temp} {m[t]}.")
  except:
    # This code is useless. Just so that in case soemthing fails, which it souldn't anyways.
    b = 1
     
    
def autoSentence(t, sentence):
  print(t + ": " + sentence)


def blog(m):
  headLine(m)
  for thing in m:
    temp = whatIs(m, thing)
  print()
  temp = m['Metascore']
  if (temp) == 100:
    autoSentence("My review", f"{m['Title']} was a amazing movie. I would definetly recommend it. The amazing acting from {m} is amazing. The plot written by {m['Writer']} was greate and cinematography by {m['Director']} was superb.")
  elif int(temp[0]) <= 6:
    autoSentence("My review", f"{m['Title']} was a terrible movie. All personel that worked on this movie should be ashamed. The disgusting plot written by {m['Writer']} and directed by vile {m['Director']}. The actors performance was terrible, {m['Actors']}. Don't think about watching this movie unless you love wathcing dumpster fires.")
  elif int(temp[0]) >= 7:
    autoSentence("My review", f"{m['Title']} this movie is pretty acclaimed. The director {m['Director']} should be very happy with this movie. {m['Actors']} did a great job in this film and really support the writing of {m['Writer']}. If this movie sounds intresting I would highly suggest watching it.")

def headLine(m):
  temp = getRandom(f"HERE ARE SOEM FACTS ABOUT {m['Title']}!", f"LET'S LOOK BACK ON {m['Title']}!", f"{m['Title']} IS A CLASSIC!")
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


#This was very difficult. I wanted to make sentences that go automatically as long as the movie has a certain peramiter. I'm not sure if this is what you wanted. 
blog(movies)
