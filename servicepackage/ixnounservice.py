import random


class NounService:
    def getrandomnoun(self):
        return random.choice(self.__fetch_noun_list())

    def __fetch_noun_list(self):
        nouns = ["Christian",
                 "Panshul",
                 "Lealem",
                 "Rene",
                 "Lars",
                 "Jochen",
                 "Johanna",
                 "Herbert",
                 "Manuel",
                 "Manuela",
                 "Stefan",
                 "Michael",
                 "Roland"]

        return nouns
