import eel
import g4f


eel.init('common/UI/web')

@eel.expose
def ask(query):
    response =  g4f.ChatCompletion.create(
        model=None,  # gpt-4-turbo, gpt-3.5-turbo, gemini
        messages=[{"role": "user", "content": query}],
        provider= g4f.Provider.DeepInfra
        )
    return response


eel.start('index.html')
