
def clean_memory():
    with open("ai_models/memory.txt", "w") as f:
        f.write("")

def save_memory(query, answer):
    with open("ai_models/memory.txt", "a") as f:
        f.write('{"role": "user", "content": ' + query + '}' + "\n")
        f.write('{"role": "assistant", "content": ' + answer + '}' + "\n")

def read_memory():
    with open("ai_models/memory.txt", "r") as f:
        return f.readlines()