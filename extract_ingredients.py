import pandas as pd
import nltk
import msvcrt as ms
import gensim

# Load Google's pre-trained Word2Vec model.
# model = gensim.models.KeyedVectors.load_word2vec_format('GoogleNews-vectors-negative300.bin', binary=True)

fd = open('train.json', 'r', encoding = 'utf8')
df = pd.read_json(fd)
fd.close()
print(df.head(10))
ingredients = set()
for row in df.ingredients:
    ingredients.update(row)

with open('ingredients.txt', 'w', encoding='utf8') as f:
    for item in ingredients:
        f.write("%s\n" % item)
print("saving...")

# print(len(ingredients),ingredients)
# There are 6714 kinds of ingredients....
# could there be overlaps? or similar ingredients? some of it even have how it is processed
# How do we merge those? Merging would reduce complexity in cooking as well as the dimensionality problem.
valid_ingredients = []
count = 0
for item in ingredients:
    count += 1
    words = item.split()
    # print(nltk.pos_tag(item.split()))
    try:
        print("ingredient: ", item)
    except:
        pass

    skip_flag = 0
    for word in words:
        if word in valid_ingredients:
            skip_flag = 1
    if skip_flag == 1:
        continue

    for word in words:
        try:
            print(word)
            exam_flag = 1
            while exam_flag:
                if ms.kbhit():
                    if ms.getch() == b'z':
                        exam_flag = 0
                    elif ms.getch() ==b'/':
                        valid_ingredients.append()
                        exam_flag = 0

        except:
            pass
    if count % 100 == 0:
        with open('ingredients.txt', 'w') as f:
            for item in valid_ingredients:
                f.write("%s\n" % item)
        print("saving...")




'''

        
    try:
        print(model.distance(words[0], 'food'))
    except:
        print(words[0] + ' not in vocab')
'''

# we would definitely need to tag them somehow, maybe not POS though.
