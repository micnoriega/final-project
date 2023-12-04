# final-project

# Title: Exploring Space :D

## URL of Video


## Link to Github
https://github.com/micnoriega/final-project.git

## Description
It is an interactive screen saver. You are a duck character that is in space and you can move around and see the different planets and stars while there are meteors falling behind you adding to the scene. You also seem to have a very colorful friend with you. Exploring space is always better with a companion! Can you figure out what each planet's theme is? 

## Overview and Thoughts
To start off I had a lot of fun but was also very stressed with this project. I have three png files I imported: exploring_space.png, duck sprite.png, and meteor.png. I was having a bit of trouble with importing the images because I tried to use pillows image import at first and it just didn't have the feel I was looking for and it got a bit complicated. So then I looked around online and I found two other methods within pygame (pygame.sprite.Sprite and pygame.image.load) and it was much easier to navigate. I used these to import the different pngs (which I made in photoshop and piskel) and just set the screen width and length and the background was good to go. 

The next part I ran into trouble with was making the duck sprite move with user input. At first, I tried to put the user imput in the main function but it was not working at all. I got stuck on this for a pretty long time until I tried putting all of the duck sprite's features within a class which is what made it work. 

The final part that I think I stressed over the most was the meteors. I had a little bit of trouble trying to make it fall from the top of the screen but in the end I got it to work. Now came the part where I think I spent the most time on. I could not figure out how to make the meteors spawn in different areas and fall from the top of the screen. Since I already had the one that worked I thought it was going to be easy, I would just have it loop through that same code and it would be fine! It was not. I tried so many different things and in different placements but all that kept falling was the singular one I already had. I looked all over the place trying to see what I could do to make this work but nothing was working. In the end I combined a few different things I saw on the internet and hoped that it would work. It did although it was also a lot of trial and error.

Somewhere in between all of this I got frustrated and added a cat (from keyboard) that changes colors because why not, the duck needed a buddy anyways.

There are a lot of things I wish I could've done with this but in the end I just didn't know how :( I looked in so many places trying to see if what I wanted to do was possible but in the end it seemed like it couldn't have been done. Not with the code I had anyways. Maybe if I had more knowledge on what works with what, it could've been better. I wanted to make the duck have to avoid the meteors while trying to pick up the "stars" but I looked into colliders and it just seemed impossible for me (and the code I had).

I think I slept like an average of 5 hours each night trying to finish this. Overall, it was fun to create this and I'm really happy with the result. I wish I could've done more but with my knowledge plus the code, it just didn't seem possible. Maybe in the future I pick this back up and add everything I wanted :)
