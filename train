import re

class Train:

    def spl(self):
        text = open('help/a.txt', encoding='utf8').read()
        tmp = re.sub("[$|@|&,.—+-=]", '', text)
        tmp = tmp.lower()
        words = tmp.split()
        return words

    def learn(self, words):
        def make_pairs(words):
            for i in range(len(words)-1):
                yield (words[i], words[i+1])
        pairs = make_pairs(words)
        return pairs
