
from typing import Literal,List
from urllib import response
from langchain_core.output_parsers import StrOutputParser
from langchain.messages import HumanMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

from pydantic import BaseModel, Field
load_dotenv()

#  Task 11
prompt = ChatPromptTemplate(
    [
        (
            'human','The product name is {product_name} and our target audience is {target_audience}. You have the generate the tagline for our product and the tone of the tagline must be {tone}'
        )
    ]
)
groq_api = os.getenv('GROQ_API_KEY')
llm = ChatGroq(
    model='openai/gpt-oss-120b',
)

chain = prompt | llm | StrOutputParser
res=chain.invoke(input={
    'product_name':'Dove',
    'target_audience':'teens',
    'tone':'sweet'
})


#  Task 12
print()
print()


prompt2 = ChatPromptTemplate(
    [
        ('system','you are given an paragraph of the product review you have to convert that review into the particular format with field such as key_topic,sentiment,summary'),
        ('human','{input}')
    ]
)

class Review(BaseModel):
    sentiment:Literal['positive','negative','neutral'] = Field(description='how was the review positive negative neutral')
    summary : str = Field(description='Summary of review in one line')
    key_topics : List[str] = Field(description='2-3 keword topics in the review')

llm_with_output_structure = llm.with_structured_output(Review)

chain = prompt2 | llm_with_output_structure

response = chain.invoke(' I bought the Apex Wireless Headphones two weeks ago, and they have completely transformed my daily commute. The sound quality is remarkably crisp with deep bass, and the active noise cancellation easily blocks out the loud city traffic. While the touch controls take a little time to learn and the case is slightly bulky, the impressive 30-hour battery life more than makes up for it. Overall, these headphones offer fantastic value for the price, and I gladly recommend them to anyone who loves high-quality sound on the go')
print(response)
response = chain.invoke('hello wshdencm ,.')
print(response)


# Task 13
# whenever we are working with the llms and using the output parser it fails when the the response from the llm is unexpected or that can be not formated according to the requirements then it causes problem in our example if the review is not given or some other string is passed it will not able to give the answet in proper format.
