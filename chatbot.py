from rich import print as rprint
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.messages import SystemMessage,HumanMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableWithMessageHistory
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder, PromptTemplate
from dotenv import load_dotenv
import os
from rich import box, print as rprint
from rich.markdown import Markdown
from rich.panel import Panel

from rich.panel import Panel
load_dotenv()

groq_api = os.getenv('GROQ_API_KEY')

llm = ChatGroq(
    model='openai/gpt-oss-120b'
)

prompt = ChatPromptTemplate(
    [
        SystemMessage(content='You are an expert chatbot capable of all the question. You response to the user perfectly according to the question asked.'),
        MessagesPlaceholder(variable_name='history'),
        ('human','{input}')
    ]
)
store={}
def get_session_history(session_id:str):
    if session_id not in store:
        store[session_id]=ChatMessageHistory()
    return store[session_id]

chain = prompt | llm | StrOutputParser()
with_message_history = RunnableWithMessageHistory(chain,get_session_history=get_session_history,input_messages_key='input',history_messages_key='history')
input_val = input()
config = {'configurable':{'session_id':'user1'}}
turns = 0
while(input_val != 'exit'):
    turns+=1
    rprint(Panel(input_val,border_style='bold white',title='User Prompt',box=box.DOUBLE_EDGE))
    response = with_message_history.invoke({'input':[HumanMessage(content=input_val)]},config)
    rprint(Panel(Markdown(response.content),border_style='bold green',title='AI Response',box=box.DOUBLE_EDGE))
    rprint(f'[yellow]Total turns completed : {turns}')
    input_val = input()
print(store)

#  Task 15 
#  the one thing that was harder than expected is that providing the context of data and tell the llm to fetch the answet from it for the context providing ypu dont just have to pass the data insteaad you have to fetch the related documents and retrived using the the vector database and then pass it to llm as the context and then usr it for the answer fetching
#   i have stored whole history in store variable which is mapped using the session_id to fetch the pres=vious chat for the response. i will imporve the model response and the context passing s the trimming the chat up to limited token summarise previous repsone and then passig in the model to reducr the token usage
