import pandas as pd
import nltk

df = pd.read_json('train.json',encoding = 'utf8')
print(df.head(10))
ingredients = set()
for row in df.ingredients:
    ingredients.update(row)

print(len(ingredients),ingredients)
# There are 6714 kinds of ingredients....
# could there be overlaps? or similar ingredients? some of it even have how it is processed
# How do we merge those? Merging would reduce complexity in cooking as well as the dimensionality problem.

for item in ingredients:
    print(nltk.pos_tag(item.split()))

# we would definitely need to tag them somehow, maybe not POS though.
