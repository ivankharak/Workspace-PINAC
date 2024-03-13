import os
import sys
import eel

module_path = os.path.abspath("my_module.py")
sys.path.append(os.path.dirname("ai_models/models"))
import models

eel.init('common/UI/web')

@eel.expose
def ask(query):
    return models.ask_gemini(query)


eel.start('index.html')
