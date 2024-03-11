import eel
from g4f.client import Client


eel.init('common/UI/web')

@eel.expose
def ask(query):
    client = Client()
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",  # gpt-4-turbo, gpt-3.5-turbo, gemini
        messages=[{"role": "user", "content": query}])
    
    # print(response.choices[0].message.content)
    return response.choices[0].message.content


eel.start('index.html')


# from g4f.gui import run_gui
# run_gui()
