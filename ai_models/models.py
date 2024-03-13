import g4f


class ask_gpt3_5:
    
    def __init__(self, query):
        response =  g4f.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": query}],
        )
        return response


class ask_gpt3_5:
    
    def __init__(self, query):
        response =  g4f.ChatCompletion.create(
            model="gpt-4-turbo",
            messages=[{"role": "user", "content": query}],
        )
        return response


class ask_gemini:
    
    def __init__(self, query):
        response =  g4f.ChatCompletion.create(
            model="gemini",
            messages=[{"role": "user", "content": query}],
        )
        return response

