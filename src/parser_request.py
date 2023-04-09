import re
import string
class Parser:
    
    def __init__(self):
        pass

    def parseText(self,text):
        text=re.sub(r"[!#$%&\()*+,-./:;<=>?@[\\]^_`{|}~]",'',text)  #punctuations
        text = '' .join((z for z in text if not z.isdigit()))
        
        text=re.sub(r'"','',text)
        #special handling of the ' char
        text=re.sub(r"'",' ',text)
        text=re.sub(r'[[]]','',text)
        text=text.lower()
        text=text.strip()
        #second processing of the text
        text=text.translate(str.maketrans('','',string.punctuation))
        return text