# Task 1

#### Explain the core difference between a traditional discriminative ML model and a generative model. Give one real-world example of each that is NOT from your training material. 
- The traditional disccriminative ml model will not generate the new content instead it uses the training dataset for prediction or classfication of any thing while the geneatiive model use the the training data then genrates the whole new response using the context of the data on which it is trained. 
- Example : Predicting the weather of the city using past data and model train can be done using the machine learning models
- Example : Creating the paragraph by giving the context of the paragraph or genrating image by giving the description of the image is done by the genai models

# Task2

#### In 3–5 sentences, explain how a large language model decides the next word/token when generating a response. Mention the role of probability in your answer. 
- The llm models are trained on the large dataset and generated the different vecotrs for each word. The vector represent the numerical form of the word and how it id influenced by other . Using this vectors llm finds out the vectors which are close the the previous vectors , the vectors which are most probable to come after using the context vector of previous vectors. The probability is that how much does the vector of the next depends on the previous vectors more the dependency more the probability anf most likely to be the next word in the sentence.

# Task 3
#### Briefly define the following terms in your own words (1–2 lines each): 

- Token 
    - it is single smallest unit of the sentence or documents (i.e word) which is converted into the vectors
- Context window 
    - Context window is the window which defines that how much word/vector to look behind to take the context of the sentence for the prediction of the next particular ouput
- Temperature (as an LLM parameter) 
    - Temperature in llm defines how much creative the model will behave that generating the new new otucome in different way for same question if the temperature is high adn genrating same outcome not much creative or put as it is from the data if temperature is too low or zero.
- Hallucination 
    - When we try to predict the next outcome without using thr previous context it genrates the unuseful and wrong output using the simple ml models which is known as the hallicuination

# Task 4
####  A teammate says: "We don't need prompt engineering — a powerful enough model will always understand what I mean." Do you agree or disagree? Justify your answer in 3–4 sentences
- Yes I agree becauase if the model is powerful enough then it will easily get the context of tge prompt we are using to tell the llm models as it is trained on large number of params and we dont need the prompt engineer to explain the taks in the proper way.

# Task 7
#### In your own words, briefly explain what each of these LangChain building blocks does and give one situation where you'd use it: a Document Loader, a Text Splitter, and an Agent. (2–3 lines total per item is enough.) 
- Document Loader
    - Document loader loads the data from different files and convert it in the Document type to easiky work with the data.
    - use : Whenever we have to loadd the data from different files such as txt,pdf,csv etc for using the data in our app we use document loader
- Text Splitter
    - Text Spliiter splits the documents into the smaller chunks to easily query it for the context using rag.
    - use: when we want to pass the context to the llm models by getting it from the documents using context vector match we use the text splitter so that we can only pass the data which is realted to the question
- Agent
    - an agent is a object/function that help us to connect to the pretrained models and gets the response by using that external llm models.
    -  use : when we want to connect the external llm model in out application we use the agents