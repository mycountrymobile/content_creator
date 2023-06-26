# Bring in deps
import os 
from apikey import apikey
import streamlit as st 
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain 
from langchain.memory import ConversationBufferMemory
from langchain.utilities import WikipediaAPIWrapper 

os.environ['OPENAI_API_KEY'] = apikey

# App framework
st.title('🔗 Content Creator')
prompt = st.text_input('Plug in the Keyword for the content you want to create') 

# Get a response
import openai

title_template = PromptTemplate(
    input_variables = ['topic'], 
    template='write me a content title about {topic} related to VOIP consisting of atleast 1 positive, 1 power and must be of 60 characters'
)

outline_template= PromptTemplate(
    input_variables=['title'],
    template='AZ Wholesale {title}” Based ON provided Information, Please Create an outline for the blog, the blog will be 2000 words. need to write a Title, with 60 characters and use power and positive word with a number, Meta should be a maximum of 160 characters, and the content should have a detailed outline. include H1,h2,h3,h4'
)

script_template = PromptTemplate(
    input_variables= ['title','outline'], 
    template='I like to start creating an article but want to start with the First section. I only. please write only the I section first and one by one we will write the rest the sections once I send submit. we will write the next one'
)

# Memory 
title_memory = ConversationBufferMemory(input_key='topic', memory_key='chat_history')
script_memory = ConversationBufferMemory(input_key='title', memory_key='chat_history')
outline_memory = ConversationBufferMemory(input_key='topic',memory_key='chat_history')
# Llms
llm = OpenAI(temperature=0.9) 
title_chain = LLMChain(llm=llm, prompt=title_template, verbose=True, output_key='title', memory=title_memory)
script_chain = LLMChain(llm=llm, prompt=script_template, verbose=True, output_key='script', memory=script_memory)
wiki = WikipediaAPIWrapper()
outline_chain=LLMChain(llm=llm,prompt=outline_template, verbose=True, output_key='topic', memory=outline_memory)

# Show stuff to the screen if there's a prompt
if prompt: 
    title = title_chain.run(prompt)
    outline= outline_chain.run(prompt)
    wiki_research = wiki.run(prompt) 
    script = script_chain.run(title=title, wikipedia_research=wiki_research) 

    st.write(title) 
    st.write(script)
    st.write(outline)

    with st.expander('Title History'): 
        st.info(title_memory.buffer)

    with st.expander('Script History'): 
        st.info(script_memory.buffer)

    with st.expander('Outline Points'):
        st.info(outline_memory.buffer)