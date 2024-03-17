import g4f
from ai_models.training_data import tr_data


def ask_me(query):
    messages = tr_data + [{"role": "user", "content": query}]

    response =  g4f.ChatCompletion.create(
        # model="gpt-4-turbo",
        model=None,
        provider=g4f.Provider.Llama2,  # Model: Llama2, HuggingFace
        messages=messages,
    )
    return response

