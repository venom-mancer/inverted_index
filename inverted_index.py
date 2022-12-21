import re
import os, glob

keyword_used = {}

def splitter(keywords):

    splited_keywords = re.split(r"[-;,. ]\s*",keywords)

    print(splited_keywords)
    text_reader(splited_keywords)


def text_reader(keywords):

    path = r'C:\Users\Bavifard\Desktop\New folder'
    for filename in glob.glob(os.path.join(path, '*.txt')):
        with open(os.path.join(os.getcwd(), filename), 'r') as file:
            read_file = file.read()
            text_file = clean_text(read_file)
            head, tail = os.path.split(filename)
            keyword_counter(text_file,keywords,tail)


def clean_text(text):
    """
    takes the text and removes signs and some extra words
    """
    stopwords = {
        'A', 'About', 'Actually' ,'Almost','Also','Although','Always','Am','An','And','Any','Are','As','At','Be','Became','Become','But','By',
        'Can','Could','Did','Do','Each','Either','Else','The','That','For','From','Had','Has','Have','Hence','How','I','If','In','IS','IT','ITS','JUST','MAY','MAYBE','Me',
        'Might','Mine','Must','My','Mine','Must','My','Neither','Nor','Not','Of','Oh','Ok','When','Where','Whereas','Wherever','Whenever','Whether',
        'Which','While','Who','Whom','Whoever','Whose','Will' ,'With' ,'Within' ,'Without' ,'Would' ,'Yes' ,'Yet' ,'You' ,'Your',
    }
    remover = '|'.join(stopwords)
    result = re.compile(r'\b\W+('+remover+r')\b', flags=re.IGNORECASE)
    out = result.sub("", text)
    return out


def keyword_counter(text,keywords,filename):

    for word in keywords:
        match = re.findall(word, text)
        keyword_used['{}'.format(word) + ' ' + '{}'.format(len(match))] = filename


search_for = input("What words are you looking for ? :")
splitter(search_for)
print(keyword_used)