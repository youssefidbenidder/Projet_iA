from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# stop_words
mots_inutiles = stopwords.words("english")
print(len(mots_inutiles))

mots_inutiles_supplementaires = ["mon", "tue", "wed", "thu", "fri", "sat", "sun", "sunday", "monday", "tuesday",
                                 "thursday", "friday", "saturday", "sunday", "thurs", "thur", "tues",
                                 "january", "february", "march", "april", "may", "june", "july", "august",
                                 "september", "october", "november", "december", "jan", "feb", "mar", "apr",
                                 "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"]

# ajoute les mots inutiles supplementaires au mots_inutiles
for mot in mots_inutiles_supplementaires:
    mots_inutiles.append(mot)


def creation_listes_mots_positives(mots):
    mots_utiles = [mot for mot in mots if mot not in mots_inutiles]
    ma_list = [({mot: True}, 'positive') for mot in mots_utiles]
    return ma_list


def creation_listes_mots_negatives(mots):
    mots_utiles = [mot for mot in mots if mot not in mots_inutiles]
    ma_list = [({mot: True}, 'negative') for mot in mots_utiles]
    return ma_list

#tokénisation
def get_tokenized_file(fichier):
    return word_tokenize(open(fichier, 'r').read())


#rendre les mots miniscules
def process(data):
    return [word.lower() for word in word_tokenize(data)]


def creation_list_mots(mots):
    mots_utiles = [mot for mot in mots if mot not in stopwords.words("english")]

    pos_txt = get_tokenized_file(u"positive-words.txt")
    neg_txt = get_tokenized_file(u"negative-words.txt")

    ma_dict = dict([(mot, True) for mot in pos_txt if mot in mots_utiles])
    ma_dict1 = dict([(mot, False) for mot in neg_txt if mot in mots_utiles])

    ma_dict.update(ma_dict1)

    ma_dict = dict([mot for mot in ma_dict if not (mot.startswith('@'))])
    ma_dict = dict([mot for mot in ma_dict if not (mot.startswith('htpp'))])
    ma_dict = dict([mot for mot in ma_dict if not (mot.startswith('www'))])

    return ma_dict


def get_data():
    print("Collection des mots negatives")
    neg_txt = get_tokenized_file(u"negative-words.txt")
    neg_mots_utiles = creation_listes_mots_negatives(neg_txt)

    print("Collection des mots positives")
    pos_txt = get_tokenized_file(u"positive-words.txt")
    pos_mots_utiles = creation_listes_mots_positives(pos_txt)
    return pos_mots_utiles + neg_mots_utiles


