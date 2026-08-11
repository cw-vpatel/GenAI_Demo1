from langchain_core.messages import SystemMessage,HumanMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate, PromptTemplate
from dotenv import load_dotenv
import os
load_dotenv()

groq_api = os.getenv('GROQ_API_KEY')
if groq_api:
    llm = ChatGroq(
        model='openai/gpt-oss-120b'
    )

prompt = ChatPromptTemplate(
    [
        SystemMessage(content='You are an expert in explaining every topic. So You Have to Explain Every topic excatly in 2 sentences.'),
        ('human','{input}')
    ]
)
output = StrOutputParser()

#  Task 8
chain = prompt | llm | output
print("================Task 8================")
response = chain.invoke("What is Artificial Intellegence?")
print(response)
print('------------------')
response = chain.invoke("What is Genrative AI?")
print(response)
print('======================================')
print()
#  Task 9

prompt_child = ChatPromptTemplate(
    [

        SystemMessage(content='You are an expert tutor explaining every topic to 10 year old child . explain the topic recived in excatly 1 line not more than that which is suitable for 10 year old child'),
        ('human','{input}')
    ]
)

chain_child = chain | prompt_child | llm | output
print("================Task 9================")
response = chain_child.invoke("What is Artificial Intellegence?")
print(response)
print('------------------')
response = chain_child.invoke("What is Genrative AI?")
print(response)
print('======================================')

#  Task 10
# In the above code first the llm model is created using groq and the prompt is created using the chatprompttemplate which explains the llm that to explain the topic in excatly 2 sentences and the output is defined as stroutputparse then the rag chain is created using llm , prompt, output and | , | connects all the components with each other in order that is the first input is given in the prompt then the output of prompt is given to llm and the output of llm is given to outputparse and that output of parser is printed. similarly next the one more prompt is added that is prompt child which tell the model that you are explaining to 10 year old child and inserted in between llm and prommpt in the chain suhc that the output of prompt goes in the prompt child and output of prompt vhild goes to llm. LCEL chains are deescribes as composable and streamble because we can easily compose the different things into one stream using | similar to plug and play while the using simple function can be complex in writing code if there are multiple components in the pipeline.
