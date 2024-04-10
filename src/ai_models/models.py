
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.prompts.chat import ChatPromptTemplate
from langchain.schema import BaseOutputParser

from src.ai_models.data.training_data import dataset, findNameDataset
from src.ai_models.model_utils import readHistory


load_dotenv(dotenv_path="src/configs/.env")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
# HUGGINGFACEHUB_API_TOKEN = os.getenv("HUGGINGFACEHUB_API_TOKEN")

class MyOutputParser(BaseOutputParser):
    def parse(self, text: str) -> str:
        return text

llm = ChatOpenAI(openai_api_key=OPENAI_API_KEY, temperature=0.7, model_name="gpt-3.5-turbo")

chat_prompt = ChatPromptTemplate.from_messages(dataset)
namePrompt = ChatPromptTemplate.from_messages(findNameDataset)
chain = chat_prompt|llm|MyOutputParser()
nameChain = namePrompt|llm|MyOutputParser()

print("chain created")

def askAI(query):
    response = chain.invoke({"text": query})
    return response

def findName(user_input):
    response = nameChain.invoke({"text": user_input})
    return response
