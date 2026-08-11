from dotenv import load_dotenv
import os
load_dotenv()

os.environ['GROQ_API_KEY'] = os.getenv('GROQ_API_KEY')
if not os.environ['GROQ_API_KEY']:
    print('Groq API Missing !!!!!!!')
else:
    print('Groq API found.')
    
os.environ['LANGSMITH_TRACING'] = os.getenv('LANGSMITH_TRACING')
os.environ['LANGSMITH_API_KEY'] = os.getenv('LANGSMITH_API_KEY')
if not os.environ['LANGSMITH_API_KEY']:
    print('Langsmith API Missing !!!!!!!')
else:    
    print('Langsmith API Found.')
os.environ['LANGSMITH_PROJECT'] = os.getenv('LANGSMITH_PROJECT')
if not os.environ['LANGSMITH_PROJECT']:
    print('langsmith project Missing !!!!!!!')
else:    
    print('langsmith project Found')

# Hard-Coding the enviroment is not a good practice because our code might get leaked and if the enviroment varible are hard coded then our api keys get leaked and can be used by other.

# Task 7
#### In your own words, briefly explain what each of these LangChain building blocks does and give one situation where you'd use it: a Document Loader, a Text Splitter, and an Agent. (2–3 lines total per item is enough.) 
# - Document Loader
#     - Document loader loads the data from different files and convert it in the Document type to easiky work with the data.
#     - use : Whenever we have to loadd the data from different files such as txt,pdf,csv etc for using the data in our app we use document loader
# - Text Splitter
#     - Text Spliiter splits the documents into the smaller chunks to easily query it for the context using rag.
#     - use: when we want to pass the context to the llm models by getting it from the documents using context vector match we use the text splitter so that we can only pass the data which is realted to the question
# - Agent
#     - an agent is a object/function that help us to connect to the pretrained models and gets the response by using that external llm models.
#     -  use : when we want to connect the external llm model in out application we use the agents
