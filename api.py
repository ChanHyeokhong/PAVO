import os
import sys
#한국어 번역 api#
from googletrans import Translator

def use_api(z,outlan):
    t=Translator()
    #t.detect()
    return (t.translate(z,dest=outlan).text)


