from langchain.schema import SystemMessage, HumanMessage, AIMessage

def clearHistory():
    """Clear the memory file."""
    with open("src/ai_models/data/history.txt", "w") as f:
        f.write("")
        # f.write('SystemMessage(content="Now be ready to start a new conversation with user. Use your learning from previous conversation examples")\n')

def saveHistory(query, answer):
    """Save the user query and assistant answer to the memory file."""
    with open("src/ai_models/data/history.txt", "a") as file:
        file.write(f'HumanMessage(content="{query}")\nAIMessage(content="{answer}")\n')

def readHistory():
    """Read and return the conversation history from the memory file."""
    with open("src/ai_models/data/history.txt", "r") as file:
        return [eval(line) for line in file]
