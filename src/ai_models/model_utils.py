
def clean_memory():
    with open("ai_models/memory.txt", "w") as f:
        f.write("")

def save_memory(query, answer):
    with open("ai_models/memory.txt", "a") as f:
        f.write('{"role": "user", "content": "' + query + '"}' + "\n")
        f.write('{"role": "assistant", "content": "' + answer + '"}' + "\n")

def read_memory():
    conversations = []
    with open("ai_models/memory.txt", "r") as f:
            for line in f:
                line_dict = eval(line)
                conversations.append(line_dict)
    return conversations

