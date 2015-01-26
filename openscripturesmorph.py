#!/usr/local/bin/python3

class Morph:

    data = {
        "languages" : {
            "Hebrew" : "H",
            "Aramaic" : "A",
        },

        "partsofspeech" : {
            "art" : "T",    # article
            "verb" : "V",   # verb
            "subs" : "N",   # noun
            "nmpr" : "N",   # proper noun
            "advb" : "D",   # adverb
            "prep" : "R",   # preposition
            "conj" : "C",   # conjunction
            "prps" : "P",   # personal pronoun
            "prde" : "P",   # demonstrative pronoun
            "prin" : "P",   # interrogative pronoun
            "intj" : "T",   # interjection
            "nega" : "T",   # negative particle
            "inrg" : "T",   # interrogative particle
            "adjv" : "A",   # adjective
            # "" : "S"      # Suffix (WLC)
        },

        "lexical_set" : {
            "nmdi" : "",    # distributive noun
            "nmcp" : "",    # copulative noun
            "padv" : "",    # potential adverb
            "afad" : "",    # anaphoric adverb
            "ppre" : "",    # potential preposition
            "cjad" : "",    # conjunctive adverb
            "ordn" : "",    # ordinal
            "vbcp" : "",    # copulative verb
            "mult" : "",    # noun of multitude
            "focp" : "",    # focus particle
            "ques" : "",    # interrogative particle
            "gntl" : "",    # gentilic
            "quot" : "",    # quotation verb
            "card" : "",    # cardinal
            "none" : "",    # none
        },

        # From ETCBC lexical set
        "adjective_types" : { # WLC Values
            "ordn" : "a",   # adjective
            "card" : "c",   # cardinal number
            "gntl" : "g",   # gentilic
            # "" : "o",     # ordinal number
        },

        # From ETCBC lexical set
        "noun_types" : {  # WLC Values
            # "" : "c",     # common
            "gntl" : "g",   # gentilic
            # "" : "p",     # proper name
        },

        "pronoun_types" : { # WLC Values
            "prde" : "d",   # demonstrative
            # "" : "f",     # indefinite
            "prin" : "i",   # interrogative
            "prps" : "p",   # personal
            # "" : "r",     # relative
        },

        "participle_types" : { # WLC Values
            # "" : "a",     # affirmation
            "art" : "d",     # definite article
            # "" : "e",     # exhortation
            "inrg" : "i",   # interrogative
            "intj" : "j",   # interjection
            # "" : "m",     # demonstrative
            "nega" : "n",   # negative
            # "" : "o",     # direct object marker
            # "" : "r",     # relative
        },

        "verb_stems_H" : { # WLC Values
            "qal" : "q",   # qal
            "nif" : "N",   # niphal
            "piel" : "p",  # piel
            "pual" : "P",  # pual
            "hif" : "h",   # hiphil
            "hof" : "H",   # hophal
            "hit" : "t",   # hithpael
            # "" : "o",    # polel
            # "" : "O",    # polal
            # "" : "r",    # hithpolel
            # "" : "m",    # poel
            # "" : "M",    # poal
            # "" : "k",    # palel
            # "" : "K",    # pulal            
            # "" : "Q",    # qal passive
            # "" : "l",    # pilpel
            # "" : "L",    # polpal
            # "" : "f",    # hithpalpel
            # "" : "D",    # nithpael
            # "" : "j",    # pealal
            # "" : "i",    # pilel
            # "" : "u",    # hothpaal
            # "" : "c",    # tiphil
            # "" : "v",    # hishtaphel
            # "" : "w",    # nithpalel
            # "" : "y",    # nithpoel
            # "" : "z",    # hithpoel
        },

        "verb_stems_A" : {
            "afel" : "a",   # af'el
            "etpa" : "",    # etpa'"al
            "etpe" : "",    # etpe'el
            "haf" : "h",    # haf'el
            "hop" : "",     # hotpa'"al
            "hsht" : "",    # hishtaf'al
            "htpa" : "",    # hitpa'"al
            "htpe" : "",    # hitpe'el
            "nit" : "",     # nitpa'"el
            "pael" : "p",   # pa'"el
            "peal" : "q",   # pe'al
            "peil" : "Q",   # pe'il
            "shaf" : "e",   # shaf'el
            "tif" : "c",    # tif'al
            "pasq" : "",    # passiveqal

            # WLC Values
            # "peal" : "q", # peal
            # "peil" : "Q", # peil
            # # "" : "u",   # hithpeel
            # "pael" : "p", # pael
            # # "" : "P",   # ithpaal
            # # "" : "M",   # hithpaal
            # "afel" : "a", # aphel
            # "haf" : "h",  # haphel
            # # "" : "s",   # saphel
            # "shaf" : "e", # shaphel
            # # "" : "H",   # hophal
            # # "" : "i",   # ithpeel
            # # "" : "t",   # hishtaphel
            # # "" : "v",   # ishtaphel
            # # "" : "w",   # hithaphel
            # # "" : "o",   # polel
            # # "" : "z",   # ithpoel
            # # "" : "r",   # hithpolel
            # # "" : "f",   # hithpalpel
            # # "" : "b",   # hephal
            # "tif" : "c",  # tiphel
            # # "" : "m",   # poel
            # # "" : "l",   # palpel
            # # "" : "L",   # ithpalpel
            # # "" : "O",   # ithpolel
            # # "" : "G",   # ittaphal
        },

        "verse_tenses" : {
            "perf" : "p",    # perfect
            "impf" : "i",    # imperfect
            "wayq" : "w",    # wayyiqtol
            "impv" : "v",    # imperative
            "infa" : "a",    # infinitive (absolute)
            "infc" : "c",    # infinitive (construct)
            "ptca" : "r",    # participle
            "ptcp" : "s",    # participle (passive)

            # WLC Values
            # "perf" : "p",   # perfect (qatal)
            # # "" : "q",     # sequential perfect (weqatal)
            # "impf" : "i",   # imperfect (yiqtol)
            # "wayq" : "w",   # sequential imperfect (wayyiqtol)
            # # "" : "h",     # cohortative
            # # "" : "j",     # jussive
            # "impv" : "v",   # imperative
            # "ptca" : "r",   # participle active
            # "ptcp" : "s",   # participle passive
            # "infa" : "a",   # infinitive absolute
            # "infc" : "c",   # infinitive construct
        },

        "suffix" : { # WLC Values
            # "" : "d",   # directional he
            # "" : "h",   # paragogic he
            # "" : "n",   # paragogic nun
            # "" : "p",   # pronominal
        },

        "persons" : {
            "p1" : "1",
            "p2" : "2",
            "p3" : "3",
        },

        "genders" : {
            "m" : "m",
            "f" : "f",
        },

        "numbers" : {
            "sg" : "s",
            "du" : "d",
            "pl" : "p",
        },

        "states" : {
            "a" : "a",      # absolute
            "c" : "c",      # construct
            # "e" : "",     # emphatic
        },
    }

    def __init__(self, words):
        self.words = words
        return

    def output(self):
        morph = ''
        morph += self.data['languages'][self.words[0]['language']] # Language
        for index, word in enumerate(self.words):
            # This is the last word
            if (index+1) == len(self.words):
                if word['part_of_speech'] == 'art' and len(word['word']) == 0:
                    # This is an article and it's blank, so we need to modify the preposition
                    index = morph.find('/')
                    morph = morph[:index] + 'd' + morph[index:]
                    continue

            if index > 0:
                morph += '/'

            partofspeech = self.data['partsofspeech'][word['part_of_speech']]

            if partofspeech == 'N':
                type = word['lexical_set']
                if type == 'padv' or type == 'afad' or type == 'cjad':
                    # This is actually an adverb!
                    partofspeech = 'D'

            morph += partofspeech
            morph += self.assemble_partofspeech(partofspeech, word)

        return morph

    def assemble_partofspeech(self, partofspeech, word):
        output = ''
        try:
            func = getattr(self, 'assemble_' + partofspeech)
        except AttributeError:
            print('function not found "%s" (%s)' % ('assemble_' + partofspeech, word))
        else:
            output = func(word)
        return output


    # Adjective
    def assemble_A(self, word):
        type = self.val('adjective_types', word['lexical_set'])
        gender = self.val('genders', word['gender'])
        number = self.val('numbers', word['number'])
        state = self.val('states', word['state'])
        return type + gender + number + state

    # Conjunction
    def assemble_C(self, word):
        return '' 

    # Adverb
    def assemble_D(self, word):
        return '' 

    # Noun
    def assemble_N(self, word):
        type = self.val('noun_types', word['lexical_set'])
        gender = self.val('genders', word['gender'])
        number = self.val('numbers', word['number'])
        state = self.val('states', word['state'])

        if type == '?' and word['part_of_speech'] == 'nmpr':
            # Proper noun
            type = 'p'
            gender = ''
            number = ''
            state =  ''
        elif type == '?':
            # Common noun
            type = 'c'

        return type + gender + number + state

    # Pronoun
    def assemble_P(self, word):
        type = self.val('pronoun_types', word['part_of_speech'])
        person = self.val('persons', word['person'])
        gender = self.val('genders', word['gender'])
        number = self.val('numbers', word['number'])
        return type + person + gender + number

    # Preposition
    def assemble_R(self, word):
        return ''

    # Participle
    def assemble_T(self, word):
        type = self.val('participle_types', word['part_of_speech'])
        return type

    # Verb
    def assemble_V(self, word):
        stem = self.val('verb_stems_' + self.data['languages'][word['language']], word['stem'])
        tense = self.val('verse_tenses', word['tense'])
        person = self.val('persons', word['person'])
        gender = self.val('genders', word['gender'])
        number = self.val('numbers', word['number'])
        state = self.val('states', word['state'])

        if state == '?':
            state = '' # No state on this verb

        return stem + tense + person + gender + number + state

    def val(self, var, val):
        output = ''
        output += self.data[var][val] if val in self.data[var] and self.data[var][val] else '?'
        return output

