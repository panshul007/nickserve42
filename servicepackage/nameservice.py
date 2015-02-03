import servicepackage.adjectiveservice as adjectives
import servicepackage.ixnounservice as ixnouns
import servicepackage.nounservice as nouns


class NameService:
    adjservice = adjectives.AdjectiveService()
    ixnservice = ixnouns.NounService()
    nservice = nouns.NounService()

    def generaterandomname(self):
        left = self.adjservice.getrandomadjective()
        right = self.nservice.getrandomnoun()
        return self.__concatname(left, right)

    def generaterandomixname(self):
        left = self.adjservice.getrandomadjective()
        right = self.ixnservice.getrandomnoun()
        return self.__concatname(left, right)

    def generate_random_adjective_for_name(self, name):
        left = self.adjservice.getrandomadjective()
        return self.__concatname(left, name)

    def __concatname(self, left, right):
        return left + "-" + right
