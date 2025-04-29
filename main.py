from fastapi import FastAPI
from pydantic import BaseModel,Field
from langchain_community.chat_models import ChatOpenAI
import os
from dotenv import load_dotenv,find_dotenv
from mangum import Mangum
import uvicorn
load_dotenv(find_dotenv())
app=FastAPI(tittle='LLM APi')
class response(BaseModel):
    user:str=Field('input user')
@app.post('/')
def invoke(res: response):
    llm=ChatOpenAI(model_name="mistralai/mistral-7b-instruct", temperature=0.7)
    answer=llm.invoke(res.user).content
    return {"user":res.user,'ai':answer}

handler = Mangum(app)
