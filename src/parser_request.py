import re
class Parser:
    
    def __init__(self):
        pass

    def parseText(self,text):
        text=re.sub(r'[!@#$()—,\n"%^*?:;0-9)]','',text)
        text=re.sub(r'[[]]','',text)
        text=text.lower()
        text=text.strip()
        return text