pip install langchain
# Import dependencies
import os 
from apikey import apikey 

import streamlit as st 
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain, SequentialChain 
from langchain.memory import ConversationBufferMemory
from langchain.utilities import WikipediaAPIWrapper

wiki = WikipediaAPIWrapper()
os.environ['OPENAI_API_KEY'] = apikey
import time

# App framework
st.title('🔗 Content Creator :)')
prompt = st.text_input('Input your prompt here') 

# Prompt templates
title_template = PromptTemplate(
    input_variables = ['topic'], 
    template='write me a content title about {topic} related to VOIP consisting of at least 1 positive, 1 power word and must be of 60 characters And  Meta for {topic} which must be consist of 160 characters.'
)
print(title_template)
#time.sleep(1)
script_template = PromptTemplate(
    input_variables = ['title'], 
    template='My Keyword is title Title : {title} Based ON provided Information, Create outline and divide into 4 partsand for the blog '
)
print(script_template)
#time.sleep(1)

first_template = PromptTemplate(
    input_variables = ['title', 'script_output'],
    template='Consider the keyword{title} & considering {script_output}, create blog on 1st outline for atleast 150 or max 200 words'
)
print(first_template)
#time.sleep(3)

benefits_template = PromptTemplate(
    input_variables = ['title', 'script_output'],
    template='Consider the keyword {title} & considering {script_output},on 2nd outline provide content to create blog between 150 or max 180 words'
)
print(benefits_template)
#time.sleep(3)
benefiits_template = PromptTemplate(
    input_variables = ['title', 'script_output','benefits_output'],
    template='Consider the keyword {title},{script_output} & considering {benefits_output}, provide more content on 2nd outline for atleast 150 or max 180 words'
)
print(benefiits_template)
#time.sleep(3)
benefiiits_template = PromptTemplate(
    input_variables = ['title', 'script_output','benefits_output','benefiits_output'],
    template='Consider the keyword {title},{script_output} & considering {benefits_output},{benefiits_output}, provide more content on 2nd outline for atleast 150 or max 180 words'
)
print(benefiiits_template)
#time.sleep(3)

features_template = PromptTemplate(
    input_variables = ['title','script_output'],
    template='Consider the keyword {title} & considering {script_output}, create a blog section on 3rd outline for atleast 150 or max 180 words'
)
print(features_template)
#time.sleep(3)
featuresii_template = PromptTemplate(
    input_variables = ['title','features_output'],
    template='Consider the keyword {title}& considering {features_output}, create a blog section on in continous 3rd outline for atleast 150 or max 200 words'
)
print(featuresii_template)
featuresiii_template = PromptTemplate(
    input_variables = ['title','features_output','featuresii_output'],
    template='Consider the keyword {title}& considering {features_output} and {featuresii_output}, create more related section on 3rd outline for atleast 150 or max 200 words'
)
print(featuresiii_template)
bfconclusion_template=PromptTemplate(
    input_variables=['script_output'],
    template='Considering {script_output} provide content on 4th outline atleast 159 words and max 180 words'
)
print(bfconclusion_template)

third_template = PromptTemplate(
    input_variables = ['title', 'script_output'],
    template='Consider the keyword {title} & considering {script_output} wrap-up conclusion of article for 150 words and max 180 words'
)
print(third_template)
thiird_template = PromptTemplate(
    input_variables = ['title','third_output'],
    template='Consider the keyword {title} & considering {third_output} create provide summarise conclusion of article for 150 words'
)
print(thiird_template)

fourth_template = PromptTemplate(
    input_variables = ['title', 'script_output'],
    template='Based on the title {title} & considering {script_output}provide final conclusion for 150 words and  Provide minimum 7 faqs within 150 words'
)
print(fourth_template)
from langchain.memory import ConversationBufferMemory
buffer_size=1000000000
# Memories
title_memory = ConversationBufferMemory(input_key='topic', memory_key='chat_history')
script_memory = ConversationBufferMemory(input_key='title', memory_key='chat_history')
first_memory = ConversationBufferMemory(input_key='script_output', memory_key='chat_history',buffer_size=buffer_size)
benefits_memory = ConversationBufferMemory(input_key='script_output', memory_key='chat_history',buffer_size=buffer_size)
benefiits_memory = ConversationBufferMemory(input_key='benefits_output', memory_key='chat_history',buffer_size=buffer_size)
benefiiits_memory = ConversationBufferMemory(input_key='benefiits_output', memory_key='chat_history',buffer_size=buffer_size)

features_memory = ConversationBufferMemory(input_key='script_output', memory_key='chat_history',buffer_size=buffer_size)
featuresii_memory = ConversationBufferMemory(input_key='features_output', memory_key='chat_history',buffer_size=buffer_size)
featuresiii_memory = ConversationBufferMemory(input_key='featuresii_output', memory_key='chat_history',buffer_size=buffer_size)

bfconclusion_memory = ConversationBufferMemory(input_key='script_output', memory_key='chat_history',buffer_size=buffer_size)

third_memory = ConversationBufferMemory(input_key='script_output', memory_key='chat_history',buffer_size=buffer_size)
thiird_memory = ConversationBufferMemory(input_key='script_output', memory_key='chat_history',buffer_size=buffer_size)

fourth_memory = ConversationBufferMemory(input_key='script_output', memory_key='chat_history',buffer_size=buffer_size)
final_memory = ConversationBufferMemory(input_key='script_output', memory_key='chat_history',buffer_size=buffer_size)

# Llms
llm = OpenAI(temperature=0.5)

# Define the chains
title_chain = LLMChain(llm=llm, prompt=title_template, verbose=True, output_key='title', memory=title_memory)
script_chain = LLMChain(llm=llm, prompt=script_template, verbose=True, output_key='script_output', memory=script_memory)
first_chain = LLMChain(llm=llm, prompt=first_template, verbose=True, output_key='first_output', memory=first_memory)
benefits_chain = LLMChain(llm=llm, prompt=benefits_template, verbose=True, output_key='benefits_output', memory=benefits_memory)
benefiits_chain = LLMChain(llm=llm, prompt=benefiits_template, verbose=True, output_key='benefiits_output', memory=benefiits_memory)
benefiiits_chain = LLMChain(llm=llm, prompt=benefiiits_template, verbose=True, output_key='benefiiits_output', memory=benefiits_memory)

features_chain = LLMChain(llm=llm, prompt=features_template, verbose=True, output_key='features_output', memory=features_memory )
featuresii_chain = LLMChain(llm=llm, prompt=featuresii_template, verbose=True, output_key='featuresii_output', memory=featuresii_memory )
featuresiii_chain = LLMChain(llm=llm, prompt=featuresiii_template, verbose=True, output_key='featuresiii_output', memory=featuresii_memory )

bfconclusion_chain = LLMChain(llm=llm, prompt=bfconclusion_template, verbose=True, output_key='bfconclusion_output', memory=features_memory )

third_chain = LLMChain(llm=llm, prompt=third_template, verbose=True, output_key='third_output', memory=third_memory)
thiird_chain = LLMChain(llm=llm, prompt=thiird_template, verbose=True, output_key='thiird_output', memory=thiird_memory)

fourth_chain = LLMChain(llm=llm, prompt=fourth_template, verbose=True, output_key='fourth_output', memory=fourth_memory)

# If there's a prompt
if prompt:
    # Get the title and wikipedia research
    title = title_chain.run(prompt)
    wiki_research = wiki.run(prompt)

    # Create a dictionary to hold your inputs
    inputs = {'title': title, 'wikipedia_research': wiki_research}

    # Create a list of your chains
    chains = [script_chain, first_chain, benefits_chain,benefiits_chain,benefiiits_chain,features_chain,featuresii_chain,featuresiii_chain,bfconclusion_chain, third_chain,thiird_chain, fourth_chain]

    # Create a list of your memories
    memories = [script_memory, first_memory, benefits_memory,benefiits_memory,benefiiits_memory,features_memory,featuresii_memory,featuresiii_memory, third_memory,thiird_memory, fourth_memory]

    # Write the title to Streamlit
    st.write(title)

    # Loop over your chains and memories
    for chain, memory in zip(chains, memories):
        # Run the chain with the current inputs and get the output
        output = chain.run(**inputs)

        # Update the inputs with the current output
        inputs[chain.output_key] = output

        # Write the output to Streamlit
        st.write(output)

        # Show memory buffer to Streamlit for 'title' and 'fourth_output'
        if chain.output_key == 'title' or chain.output_key == 'fourth_output':
            with st.expander(f'{chain.output_key} History'):
                st.info(memory.buffer)

# Generate the final text
    segments = [
    'Refer to the {title}. With {first_output}, {script_output},{benefits_output},{benefiits_output},{benefiiits_output},{features_output},{featuresiii_output},{featuresii_output},{bfconclusion_output},{thiird_output} and {third_output}, complete this.',
    'Given {title}, {first_output}, {script_output},{benefits_output},{benefiits_output},{benefiiits_output},{featuresii_output},{features_output},{featuresiii_output},{bfconclusion_output},{thiird_output} and {third_output}, complete this.',
    'Considering {title}, {first_output}, {script_output}, {benefits_output},{benefiits_output},{benefiiits_output},{featuresii_output},{features_output},{featuresiii_output},{bfconclusion_output},{thiird_output}  and {third_output}, complete this.',
    'Based on {title}, {first_output}, {script_output},{benefits_output},{benefiits_output},{benefiiits_output},{featuresii_output},{features_output},{featuresiii_output},{bfconclusion_output},{thiird_output} and {third_output}, complete this.'
]

    final_text = " "
    #fourth_output=''
    for segment in segments:
        final_template = PromptTemplate(
            input_variables=['title', 'first_output', 'script_output', 'features_output',
                             'featuresii_output','featuresiii_output','benefits_output',
                             'benefiits_output','benefiiits_output','bfconclusion_output',
                            'third_output','thiird_output'],
            template=segment
                    )
        final_chain = LLMChain(llm=llm, prompt=final_template, verbose=True, output_key='final_output', memory=final_memory)
        output = final_chain.run(title=title, first_output=inputs['first_output'], script_output=inputs['script_output'],
                                benefits_output=inputs['benefits_output'],benefiits_output=inputs['benefiits_output'],benefiiits_output=inputs['benefiiits_output'], 
                                features_output=inputs['features_output'],featuresii_output=inputs['featuresii_output'],featuresiii_output=inputs['featuresiii_output'],
                                bfconclusion_output=inputs['bfconclusion_output'],
                                third_output=inputs['third_output'],thiird_output=inputs['thiird_output'] )
        final_text += output
# Write the final text to Streamlit
    st.write(final_text)
else:
    title = ""
    wiki_research = ""      
