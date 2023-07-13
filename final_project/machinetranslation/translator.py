
'''
this project implements translation function between english and frenc
'''
from deep_translator import MyMemoryTranslator

def english_to_french(english_text):
    '''
    this function translates english text into french
    '''
    french_text = MyMemoryTranslator(source='english', target='french').translate(english_text)
    return french_text

def french_to_english(french_text):
    '''
    this function translates french text into english
    '''
    english_text = MyMemoryTranslator(source='french', target='english').translate(french_text)
    return english_text
