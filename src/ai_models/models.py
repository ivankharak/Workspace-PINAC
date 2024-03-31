import g4f
from functools import cache
from src.ai_models.data.training_data import general_dataset, findName_dataset
from src.ai_models.model_utils import save_memory, read_memory

@cache
def ask_me(query):
    """Generate a response for a general query."""
    memory = read_memory()
    if memory:
        messages = general_dataset + memory + [{"role": "user", "content": query}]
    else:
        messages = general_dataset + [{"role": "user", "content": query}]
    response = g4f.ChatCompletion.create(
        model=None,
        provider=g4f.Provider.HuggingFace,  # Model: Llama2, HuggingFace, PerplexityLabs
        messages=messages,
        )
    save_memory(query, response)
    return response

@cache
def find_name(query):
    """Find a name in the dataset based on the query."""
    messages = findName_dataset + [{"role": "user", "content": query}]
    return g4f.ChatCompletion.create(
        model=None,
        provider=g4f.Provider.HuggingFace,
        messages=messages
        )
