#!/usr/bin/env python3

import random
import re
from nltk.corpus import words, wordnet


class randomDefinition:
    '''A class for providing 100% accurate definitions of any word'''
    def __init__(self, inword, showexample=False, subset=True):
        self.inword = inword
        self.showexample = showexample
        self.subset = subset
        self.base_list = [w.lower() for w in words.words()
                          if 3 <= len(w) <= 15]
        self.word_list = self.generate_list()
        self.syns = None
        self.example = None

    def generate_list(self):
        ''' Returns the base word list, or a smaller subset of words'''
        if self.subset is True:
            subset = random.sample(self.base_list, 1000)
        else:
            subset = self.base_list
        return subset

    def random_word(self):
        ''' Returns a random word from the word list'''
        try:
            rand_word = random.sample(self.word_list, 1)[0]
        except:
            raise SystemExit("Failed to generate random word")
        else:
            return rand_word

    def validate_def(self, synset_object):
        ''' Validate whether the synset object has a definition'''
        if synset_object and synset_object[0].definition() is not None:
            return True
        else:
            return False

    def validate_examples(self, synset_object):
        ''' Validate whether the synset object has at least one example'''
        if synset_object and len(synset_object[0].examples()) > 0:
            return True
        else:
            return False

    def validate_synset(self, synset_object):
        ''' Validate a synset object '''
        if self.validate_def(synset_object) is False:
            return False
        if (self.showexample is True and
                self.validate_examples(synset_object) is False):
            return False
        return True

    def get_synset(self):
        ''' Generate a synset object that meets certain requirements '''
        synset = wordnet.synsets(self.random_word())
        if self.validate_synset(synset) is True:
            self.syns = synset[0]
            if self.showexample is True:
                self.example = synset[0].examples()[0]
        else:
            self.get_synset()

    def print_output(self):
        ''' Prints a definition and - optionally - an example '''
        print("The definition of {0} is:".format(self.inword))
        print("{0}".format(self.syns.definition()))
        if self.example is not None:
            matchword = str(self.syns.lemmas()[0].name())
            newexample = re.subn(matchword, self.inword, self.example)
            if newexample[1] > 0:
                print("Example: {0}".format(newexample[0]))
            else:
                print("No examples available")
