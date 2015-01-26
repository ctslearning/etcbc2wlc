#!/usr/local/bin/python3

# ETCBC Documentation: http://shebanq-doc.readthedocs.org/en/latest/features/comments/0_overview.html
# WLV Documentation: http://openscriptures.github.io/morphhb/parsing/HebrewMorphologyCodes.html
# XML Documentation: https://docs.python.org/2/library/xml.dom.html#xml.dom.Node.childNodes

import sys
import re
import collections
from laf.fabric import LafFabric
from etcbc.preprocess import prepare
fabric = LafFabric(verbose='DETAIL')

fabric.load('etcbc4', '--', 'wlc',
{
    "primary": False,
    "xmlids": {"node": False, "edge": False},
    "features": ("otype gn nu ps st vs vt sp g_cons_utf8 chapter book verse vbe ls language", ""),
})
exec(fabric.localnames.format(var='fabric'))

from xml.dom import minidom

table = outfile('table.csv')
table.write("{},{},{},{},{},{},{},{},{},{}\n".format('ETCBC Location', 'WLC Word', 'ETCBC Word', 'Word Match', 'WLC Morph', 'ETCBC Morph', 'Morph Match', 'WLC Lemma', 'Note', 'ETCBC Word Data'))

# import json
# output = open('output.json', 'w')

# import pickle
# output = open('output.txt', 'ab+')

from tabulate import tabulate
import openscripturesmorph

cur_chapter = None
cur_book = None
cur_verse = None
cur_word = 0
data = {}

exclusions = {
    "Ruth" : ["3 17 12", "3 17 13"]
}

convert_books = {
    "Genesis" : "Gen",
    "Exodus" : "Exod",
    "Leviticus" : "Lev",
    "Numeri" : "Num",
    "Deuteronomium" : "Deut",
    "Josua" : "Josh",
    "Judices" : "Judg",
    "Samuel_I" : "1Sam",
    "Samuel_II" : "2Sam",
    "Reges_I" : "1Kgs",
    "Reges_II" : "2Kgs",
    "Jesaia" : "Isa",
    "Jeremia" : "Jer",
    "Ezechiel" : "Ezek",
    "Hosea" : "Hos",
    "Joel" : "Joel",
    "Amos" : "Amos",
    "Obadia" : "Obad",
    "Jona" : "Jonah",
    "Micha" : "Mic",
    "Nahum" : "Nah",
    "Habakuk" : "Hab",
    "Zephania" : "Zeph",
    "Haggai" : "Hag",
    "Sacharia" : "Zech",
    "Maleachi" : "Mal",
    "Psalmi" : "Ps",
    "Iob" : "Job",
    "Proverbia" : "Prov",
    "Ruth" : "Ruth",
    "Canticum" : "Song",
    "Ecclesiastes" : "Eccl",
    "Threni" : "Lam",
    "Esther" : "Esth",
    "Daniel" : "Dan",
    "Esra" : "Ezra",
    "Nehemia" : "Neh",
    "Chronica_I" : "1Chr",
    "Chronica_II" : "2Chr",
}

for node in NN():
    otype = F.otype.v(node)
    # print(otype)
    if otype == "book":
        cur_book = F.book.v(node)
        data[cur_book] = {}
        # print(cur_book)
    elif otype == "chapter":
        cur_chapter = F.chapter.v(node)
        data[cur_book][cur_chapter] = {}
    elif otype == "verse":
        cur_verse = F.verse.v(node)
        cur_word = 0
        data[cur_book][cur_chapter][cur_verse] = {}
    elif otype == "word":
        cur_word += 1
        # table.write("{},{},{},{},{},{},{},{},{},{},{},{}\n".format(cur_book, cur_chapter, cur_verse, cur_word, F.g_cons_utf8.v(node), F.sp.v(node), F.gn.v(node), F.nu.v(node), F.ps.v(node), F.st.v(node), F.vs.v(node), F.vt.v(node)))
        data[cur_book][cur_chapter][cur_verse][cur_word] = {
            "language" : F.language.v(node), 
            "word" : F.g_cons_utf8.v(node), 
            "part_of_speech" : F.sp.v(node), 
            "lexical_set" : F.ls.v(node), 
            "gender" : F.gn.v(node), 
            "number" : F.nu.v(node), 
            "person" : F.ps.v(node), 
            "state" : F.st.v(node), 
            "stem" : F.vs.v(node), 
            "tense" : F.vt.v(node),
        }

print("Words have been exported")

# print(data)

# for book, chapters in data.items():
    # print(convert_books[book])
    # xmldoc = minidom.parse('/Users/samueloltz/python/etcbc2wlc/openscripture/wlc/' + convert_books[book] + '.xml')
    
chapters = data['Ruth']
# print(chapters)
xmldoc = minidom.parse('/Users/samueloltz/python/etcbc2wlc/openscripture/wlc/Ruth.xml')
xml_chapters = xmldoc.getElementsByTagName('chapter')

for xml_chapter in xml_chapters:
    xml_verses = xml_chapter.getElementsByTagName('verse')
    for xml_verse in xml_verses:
        osis = xml_verse.getAttribute('osisID')
        osisParts = osis.split('.')
        cur_book = osisParts[0]
        cur_chapter = osisParts[1]
        cur_verse = osisParts[2]
        cur_word = 1
        xml_words = xml_verse.getElementsByTagName('w')
        for xml_word in xml_words:
            if xml_word.parentNode.tagName != 'verse':
                # This word isn't directly under a verse, which means it's probably a variant and we don't want it.
                continue

            location = "{} {} {}".format(cur_chapter, cur_verse, cur_word)
            if location in exclusions[cur_book]:
                continue

            print(location)

            data_words = []

            word = xml_word.firstChild.data

            clean_word = word.replace('\u05E9\u05C1', '\uFB2A').replace('\u05E9\u05C2', '\uFB2B') # SHIN and SIN into a single character
            clean_word = re.sub('[\u0591-\u05C7]', '', clean_word).replace('/', '')

            data_word = re.sub('[\u0591-\u05C7]', '', chapters[cur_chapter][cur_verse][cur_word]['word'])

            words_in_word = 1 if clean_word == data_word else (xml_word.getAttribute('lemma').count('/') + 1)
                
            for x in range(0, words_in_word):
                data_words.append(chapters[cur_chapter][cur_verse][cur_word])
                cur_word += 1

            # Check next word in data, if there is one. 
            if cur_word in chapters[cur_chapter][cur_verse]: 
                next_word = chapters[cur_chapter][cur_verse][cur_word]
                # If it's an article and is blank, it's a definite article for the previous word!
                if next_word['part_of_speech'] == 'art' and len(next_word['word']) == 0:
                    data_words.append(next_word)
                    cur_word += 1

            # There's a plus sign in the lemma, which means the next xml word is still part of this one.
            if xml_word.getAttribute('lemma').count('+'):
                cur_word -= 1

            new_morph = openscripturesmorph.Morph(data_words).output()
            existing_morph = xml_word.getAttribute('morph') if xml_word.hasAttribute('morph') else ''
            lemma = xml_word.getAttribute('lemma')
            note = xml_word.getAttribute('note') if xml_word.hasAttribute('note') else ''

            
            data_word_output = ''
            for index, data_word in enumerate(data_words):
                data_word_output += data_word['word']
            

            clean_data_word_output = re.sub('[\u0591-\u05C7]', '', data_word_output)

            word_match = 1 if clean_word == clean_data_word_output else 0
            morph_match = 1 if existing_morph == new_morph else 0

            # Debugging
            if word_match != 1:
                print(data_words)
                table_output = [[clean_data_word_output, clean_word], [existing_morph, new_morph]]
                print(tabulate(table_output, ['Original', 'New'], tablefmt="grid"))
                print('Lemma: ' + lemma)
                # input("Press Enter to continue...")
                print("\n\n")

            table.write("{},{},{},{},{},{},{},{},{},{}\n".format(location, clean_word, clean_data_word_output, word_match, existing_morph, new_morph, morph_match, lemma, note, str(data_words)))




print("Table has been exported")

close()

# json.dump(data, output)

# pickle.dump(data, output)
# output.close()