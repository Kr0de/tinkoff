from train import Train
from generate import Generate

words = Train.spl('')
pairs = Train.learn('', words)
num_words = 100
text = Generate.makeText('', words, pairs, num_words)
print(text)
