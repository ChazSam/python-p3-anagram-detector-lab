# your code goes here!
import ipdb

class Anagram:
    
    def __init__(self, word):
        self.word = word

    def match(self, match_list):
        returnList = []
        newWord = sorted([letter for letter in self.word])

        for n in match_list:
            matcher = sorted([letter for letter in n])

            if newWord == matcher:
                returnList.append(n)
                
        return returnList

            



