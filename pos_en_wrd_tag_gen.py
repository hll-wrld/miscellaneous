from nltk import word_tokenize, pos_tag
from nltk.corpus import words

print("starting...")
lst = pos_tag(words.words())

file_ = open("POS_tags/en_words_pos.txt","w")

print("writing...")
for n in lst:

    out = str(n).replace("(","")
    out = out.replace(")","")
    out = out.replace("'","")
    out = out.replace(",","")
    file_.write(out+"\n")


file_.close()

print("DONE")

