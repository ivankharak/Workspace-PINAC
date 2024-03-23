import g4f
from src.ai_models.training_data import dataset


def ask_me(query):
    messages = dataset + [{"role": "user", "content": query}]

    response =  g4f.ChatCompletion.create(
        # model="gpt-4-turbo",
        model=None,
        provider=g4f.Provider.Llama2,  # Model: Llama2, HuggingFace
        messages=messages,
    )
    return response

