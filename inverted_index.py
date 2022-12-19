import re
import os, glob

def splitter(keywords):

    splited_keywords = re.split(r"[-;,. ]\s*",keywords)

    print(splited_keywords)
    text_reader()


def text_reader():

    path = r'C:\Users\APA\Desktop'
    for filename in glob.glob(os.path.join(path, '*.txt')):
        with open(os.path.join(os.getcwd(), filename), 'r') as f: 
            print('1')

    

def clean_text(text):
    """
    takes the text and removes signs and some extra words
    """
    stopwords = {
        'A', 'About', 'Actually' ,'Almost','Also','Although','Always','Am','An','And','Any','Are','As','At','Be','Became','Become','But','By',
        'Can','Could','Did','Do','Each','Either','Else','For','From','Had','Has','Have','Hence','How','I','If','In','IS','IT','ITS','JUST','MAY','MAYBE','Me',
        'Might','Mine','Must','My','Mine','Must','My','Neither','Nor','Not','Of','Oh','Ok','When','Where','Whereas','Wherever','Whenever','Whether',
        'Which','While','Who','Whom','Whoever','Whose','Will' ,'With' ,'Within' ,'Without' ,'Would' ,'Yes' ,'Yet' ,'You' ,'Your',
    }
    result  = [word for word in re.split("\W+",text) if word.lower() not in stopwords]
    result = (' ').join(result)
    return result

    
search_for = input("What words are you looking for ? :")
splitter(search_for)