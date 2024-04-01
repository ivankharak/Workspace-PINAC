import json

def clear_history():
    """Clear the memory file."""
    with open("src/ai_models/data/memory.txt", "w") as f:
        f.write("")

def save_history(query, answer):
    """Save the user query and assistant answer to the memory file."""
    with open("src/ai_models/data/memory.txt", "a") as file:
        json.dump({"role": "user", "content": query}, file)
        file.write("\n")
        json.dump({"role": "assistant", "content": answer}, file)
        file.write("\n")


def read_history():
    """Read and return the conversation history from the memory file."""
    with open("src/ai_models/data/memory.txt", "r") as file:
        return [eval(line) for line in file]
