
import re
#import sys
#print(sys.argv[1])
file = open(r"C:\Users\Rohith R\Documents\UiPath\DocumentUnderstandingFinal\extracted_txt.txt")
text = file.read().strip()
def make_trie(*words):
    root = {}
    for word in words:
        current = root
        for letter in word:
            current = current.setdefault(letter, {})
            # insert sentinel at the end
            current[None] = None
    return root

def word_boundary(s, trie):
    seq = []
    for i in range(len(s)):
        pos, current, found = i, trie, []
        while pos < len(s) and s[pos] in current:
            found.append(s[pos])
            current = current[s[pos]]
            if None in current:  # whole substring detected
                seq.append(''.join(found))
                pos += 1
    return seq

def title(text):
    s1 = "Title number(s) of the property:"
    s2 = "Insert address including postcode"
    s3 = "2\nProperty:"
    s4 = "Property:"
    return word_boundary(text, make_trie(s1, s2, s3, s4))

def property(text):
    s1 = "Property:"
    s2 = "Remember to date this deed"
    s3 = "3\nDate:"
    s4 = "Date:"
    return word_boundary(text, make_trie(s1, s2, s3, s4))

def transferor(text):
    s1 = "Transferor:"
    s2 = "4\nFor UK incorporated companies/LLPS"
    s3 = "Complete as appropriate"
    return word_boundary(text, make_trie(s1, s2, s3))

def date_func(text):
    s1 = "Date:"
    s2 = "Give full name(s)"
    s3 = "4\nTransferor:"
    return word_boundary(text, make_trie(s1, s2, s3))

if not text:
    print("Invalid text")
else:
    title_text = ((text.split(title(text)[0]))[1].split(title(text)[1])[0]).strip()
    property_text = ((text.split(property(text)[0]))[1].split(property(text)[1])[0]).strip().replace("\n", " ")
    transferor_text = ((text.split(transferor(text)[0]))[1].split(transferor(text)[1])[0]).strip().replace("\n", " ")
    date_text = ((text.split(date_func(text)[0]))[1].split(date_func(text)[1])[0]).strip().replace("\n", " ")
    print(title_text)
    print(property_text)
    print(transferor_text)
    print(date_text)
