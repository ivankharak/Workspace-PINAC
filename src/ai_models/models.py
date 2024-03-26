import g4f
from functools import cache
from src.ai_models.data.training_data import general_dataset, findName_dataset

# @cache
def ask_me(query):
    """Generate a response for a general query."""
    messages = general_dataset + [{"role": "user", "content": query}]
    return g4f.ChatCompletion.create(
        # model="gpt-4-turbo",
        model=None,
        provider=g4f.Provider.Llama2,  # Model: Llama2, HuggingFace
        messages=messages,
    )

@cache
def find_name(query):
    """Find a name in the dataset based on the query."""
    messages = findName_dataset + [{"role": "user", "content": query}]
    return g4f.ChatCompletion.create(
        model=None,
        provider=g4f.Provider.HuggingFace,
        messages=messages
        )
