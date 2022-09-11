import numpy as np
from train import Train

class Generate:
    def makeText(self, words, pairs, num_words):
        word_dict = {}

        for firstWord, secondWord in pairs:
            if firstWord in word_dict.keys():
                word_dict[firstWord].append(secondWord)
            else:
                word_dict[firstWord] = [secondWord]

        first_word = np.random.choice(words)
        chain = [first_word]
        for i in range(num_words):
            chain.append(np.random.choice(word_dict[chain[-1]]))
        out = ' '.join(chain)
        return out
