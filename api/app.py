from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langserve import add_routes
import uvicorn
import os
from langchain_community.llms import Ollama

from dotenv import load_dotenv

load_dotenv()

os.environ['GOOGLE_API_KEY']=os.getenv('GOOGLE_API_KEY')

app= FastAPI(
    title="Langchain Server",
    version="1.0",
    description="A simple API Server"
)

add_routes(
    app,
    ChatGoogleGenerativeAI(model="gemini-pro", convert_system_message_to_human=True),
    path='/gemini'
)

model = ChatGoogleGenerativeAI(model="gemini-pro", convert_system_message_to_human=True)

llm=Ollama(model = "llama2")

prompt1=ChatPromptTemplate.from_template("Write me an essay about {topic} with 100 words.")

prompt2=ChatPromptTemplate.from_template("Write me an poem about {topic} with 50 words.")

add_routes(
    app,
    prompt1|model,
    path="/essay"
)

add_routes(
    app,
    prompt2|llm,
    path="/poem"
)

if __name__=="__main__":
    uvicorn.run(app, host="localhost", port=8000)