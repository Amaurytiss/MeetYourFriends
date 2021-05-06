# MeetYourFriends
Selenium based bot which takes as many cities as you want as arguments and locate on google maps the closest place for evryone to meet with your friends

## How does it work

Once you entered the number of cities and their names, the bot goes on wikipedia to gather the lat/lon coordinates of the city from its page

![Alt wiki](https://github.com/Amaurytiss/MeetYourFriends/blob/main/images/wiki.JPG)

After parsing the result and computing the barycentre of the coordinates, it goes on google maps to show the result

Example on the french cities Paris, Nantes and Toulouse :

![Alt bary](https://github.com/Amaurytiss/MeetYourFriends/blob/main/images/bary.JPG)

## Requirements 

- Python 3+
- Selenium
- The chrome browser
- chromedriver.exe corresponding to your chrome version (you can find them on https://chromedriver.chromium.org/downloads)
