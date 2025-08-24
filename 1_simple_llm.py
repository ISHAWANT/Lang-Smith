from dotenv import load_dotenv 
from langchain_groq import ChatGroq 
from langchain_core.prompts import PromptTemplate 
from langchain_core.output_parsers import StrOutputParser 

load_dotenv() 

prompt = PromptTemplate.from_template("What is the capital of {country}?") 

model = ChatGroq(model_name='llama-3.1-8b-instant') 
parser = StrOutputParser() 

chain = prompt | model | parser 

res = chain.invoke({'country': 'India'}) 
print(res)