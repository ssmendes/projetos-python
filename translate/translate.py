pip install translate

from translate import Translator
translator = Translator(to_lang='pt-br')
translator.translate("This is a pen")