# Discord Bot for Server

Main.py is where the bot runs all the commands and listens to all events.

## main.py
### Testing the functionality of dicord.py
I started by testing the bot by sending messages to the server if it responds to the commands.
With the wesley function, it tests if it can get a quote from the list and send it to the server.
It uses the random function to choose one from the list.  I plan to add a database later on to add
on to the functionality.

### 8ball function
Next, I added an 8ball function to further test the functionality of sending out quotes.
I wanted to test that it mentions you by username when it sends you the fortune. It was also my first time using aliases for the commands.

### anime.py implementation
Now that I have tested how the discord bot works, I decided to use my anime.py functions that gets the information from myanimelist.net using their API.  I have added two functions so far.

**Search Anime**

It uses the searchAnime function from the anime.py file, and uses the arguments after the command to search for the anime.  It uses the discord.Embed attribute to send back the information searched.  It sends the message with the title of the anime, link to the myanimelist.net anime page, synopsis, and footer to say data is from myanimelist.net.

**myanimelist Top 10 Airing**

This one is similar to search anime that it uses the Embed feature.  I return the top 10 airing anime list to the server when command is run.  The embed file includes the rank, title, and link to the anime page. 

- [x] Test the discord.py funcitonality 
- [x] Further implement sending message with another function
- [x] Implement anime.py searchAnime() function
- [x] Implement anime.py getAnimeRankingsTop() function
- [ ] Implment the rest of the anime.py functions
- [ ] Add functionality to assign role by reaction
- [ ] Add more functions with the myanimelist.net API
- [ ] Implement a database(probably PostgreSQL)
- [ ] Add more features according to the server owner