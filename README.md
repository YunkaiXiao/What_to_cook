# What to cook #
## Project background ##
This is a side project to save me some time in grocery store. Often, I would stand in front a shelf of different product inside of a grocery story thinking about what to have for dinner and how to put it together. This is extremely annoying especially when I'm in a rush.

Inspired by Kaggle project "[What's cooking](https://www.kaggle.com/c/whats-cooking)" I decide to make a app which I could just put in ingredients that I want to have for a meal and come up with a few recipes from the app. *E.g. If I really want to have tomato and garlic tonight I wouldn't mind cooking it with other ingredients as long as there's a good recipe.* From there, selecting styles of cooking, whether it's Asian, French, or Italian shouldn't be much of a trouble.

## Break down ##
In order to have this working, a few components need to be constructed first.
#### Data science
The data science component for this project is pretty simple. Adapted from the Kaggle project, there would be a classifier constructed, not necessarily determining the style of cooking to apply, but a range of dishes with similar ingredients as in the input. This would make it easier to just take a recipe and pick up what's missing apart from what's already in your shopping cart.
#### Image identification
Instead of punching in what's already picked/in the basket, we could incorporate some image recognition techniques so that a snap of picture would generate that list of items for you.
#### Mobile app / Web site
To make the application portable, it has to be ported on to some mobile platform, or a website that people (I) could access on my cellphone. Not sure how this is going to work out though.
