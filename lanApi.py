from googletrans import Translator

def tran_lan(z):
    t = Translator()
    langs= t.detect(z)
    return(langs.lang)
