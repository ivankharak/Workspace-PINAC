
def clean_memory():
    """Clear the memory file."""
    with open("src/ai_models/data/memory.txt", "w") as f:
        f.write("")

def save_memory(query, answer):
    """Save the user query and assistant answer to the memory file."""
    with open("src/ai_models/data/memory.txt", "a") as f:
        f.write(f'{{"role": "user", "content": "{query}"}}\n')
        f.write(f'{{"role": "assistant", "content": "{answer}"}}\n')

def read_memory():
    """Read and return the conversation history from the memory file."""
    with open("src/ai_models/data/memory.txt", "r") as f:
        return [eval(line) for line in f]
