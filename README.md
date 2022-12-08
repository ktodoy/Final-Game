# DaBabyKart

Welcome to DaBabyKart! If you are expecting a game like MarioKart, extremely lower your expectations. It is kind of life 'Frogger' with DaBaby's face. Here is how the game/code works:

The 'DaBabyKart' itself is an image 'blitted' on to the road, which is a Surface. He can only move in the +/- y-direction by pressing the up/down arrows on your keyboard.

 There are four cop cars, each with a different speed. The slowest two appear on the screen at the very start of the game. The third slowest appears after ten seconds, and the final and fastest car appears at the 30 second mark. The way they constanly reapper on the screen is by resetting their rectangular x-value to a little bit more than the width of the screen just after it passes x = 0. Every time this occurs, a new y-value is chosen through the 'randint' function, which is bound by the top and bottom of the road. Essentially, the goal of the game is to avoid colliding with these cars for as long as possible. If you do collide with one of these cars, your health goes down. When your health reaches 0, the game is over and your time is shown to you on another page (this was originally supposed to be a leaderboard, but I got lazy and programmed it to only read one score at a time - so, everywhere you see 'leaderboard', think this screen.)

Also appearing at the 30 second mark is the 'DaBaby Potion' - if you have seen the YouTube video about this potion, you know its magical powers. It will instantaneously fill your healthbar upon collision, hopefully allowing you to stay alive for longer. Every 30 seconds after (1 minute, 90 seconds, etc.), the potion will reappear to give you an extra boost if you can 'collide' with it.

All the other code in this game essentially has to do with logic and calling certain methods/modules at the right time. The stopwatch is simple in functioning, for it increases milliseconds until 1000, adds 1 to the seconds value, then resets to 0. Once there is 60 seconds, it will essential function the same with minutes.

That is truly all the useful explanation I have to offer without going into boring detail. So, with this, I wish you all happy playing!!!

# Table of Contents:

- start.py - code for start screen (where running of game actually starts)
- game.py - code for functioning of main game
- leaderboard.py - code for screen which displays time
- dababy.py - code for the actual 'DaBabyKart'
- car1-4.py - code for police cars
- potion.py - code for potion
- road.py - code for road
- stopwatch.py - code for running clock
- healthbar.py - code for healthbar

# Sources:

- images: https://kenney.nl/assets/road-textures
