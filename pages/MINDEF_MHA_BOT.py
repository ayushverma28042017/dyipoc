import requests
import json
import streamlit as st
from dotenv import load_dotenv
import os 
import streamlit as st
from streamlit_chat import message

load_dotenv(".streamlit/secrets.toml")
# st.image("Geine.jpg", width=100)
url=os.environ["api_base_url"]
api_key=os.environ["AZURE_OPENAI_API_KEY"]
azureSearchKey=os.environ["azureSearchKey"]
st.image("Geine.jpg", width=100)
st.header("Let's discover how you can achieve an affordable protection portfolio with Singlfe .... ")
headers = {

    "api-key": api_key,

    "Content-Type": "application/json"
}

def generate_response(prompt):
    data = {
         "dataSources": [
                {
            "type": "AzureCognitiveSearch",
            "parameters": {
                "endpoint": "https://cognitive-search-dyi.search.windows.net",
                "key": azureSearchKey,
                "indexName": "mendefindex"
            }
                 }
    ],
    "model": "GPT-4",
     "temperature": 0.1,
    "messages": [
       {
           "role":"system",
           "content":"""you are a financial advisor. Answer in plain text , dotn use bullet points.if you dont know any answer you can say you dont know.
           Sample squestion answers . 
             Question: What is the Group Term Life Coverage Amount?
               Answer: 100,000 $
               Question: What is the Monthly premium rate for Group Term Life for ages below 65 years old?
               Answer 2.50
               Question: What is the Monthly premium rate for Group Term Life for age 66 years old?
               Answer 35.30
               Question: What is the Monthly premium rate for Group Term Life for age 67 years old?
               Answer 40.10
               Question: What is the Monthly premium rate for Group Term Life for age 68 years old?
               Answer 48.30
               Question: What is the Monthly premium rate for Group Term Life for age 69 years old?
               Answer 57.40
               Question: What is the Monthly premium rate for Group Term Life for age 70 years old?
               Answer 63.60
               Question: What is the Group Term Life Coverage Amount?
                 Answer: 100,000 $
                 Question: What is the Monthly premium rate for Living Care for ages between 1 to 20 years old?
                 Answer 2.20
                 Question: What is the Monthly premium rate for Living Care for ages between 21 to 25 years old?
                 Answer 2.60
                 Question: What is the Monthly premium rate for Living Care Life for ages between 26 to 30 years old?
                 Answer 3.70
                 Question: What is the Monthly premium rate for Living Care for ages between 31 to 35 years old?
                 Answer 5.40
                 Question: What is the Monthly premium rate for Living Care for ages between 36 to 40 years old?
                 Answer 9.00
                 Question: What is the Monthly premium rate for Living Care Life for ages between 41 to 45 years old?
                 Answer 9.00
                 Question: What is the Monthly premium rate for Living Care for ages between 46 to 50 years old?
                 Answer 24.80
                 Question: What is the Monthly premium rate for Living Care for age between 51 to 55 years old?
                 Answer 37.80
                 Question: What is the Monthly premium rate for Living Care for age between 56 to 60 years old?
                 Answer 52.20
                 Question: What is the Monthly premium rate for Living Care for age between 61 to 65 years old?
                 Answer 72.70
                 Question: What is the Monthly premium rate for Living Care for age 66 years?
                 Answer 94.50
                 Question: What is the Monthly premium rate for Living Care for age 67 years old?
                 Answer 105.80
                 Question: What is the Monthly premium rate for Living Carefor age 68 years old?
                 Answer 118.40
                 Question: What is the Monthly premium rate for Living Care for age 69 years old?
                 Answer 132.50
                 Question: What is the Monthly premium rate for Living Care for age 70 years old?
                 Answer 148.50
                 MEDIAN GROSS MONTHLY INCOME for ages between 16 to 19 years is 1,198
                 MEDIAN GROSS MONTHLY INCOME for ages between 20 to 24 years is 2,500
                 MEDIAN GROSS MONTHLY INCOME for ages between 25 to 29 years is 3,850
                 MEDIAN GROSS MONTHLY INCOME for ages between 30 to 34 years is 5,000
                 MEDIAN GROSS MONTHLY INCOME for ages between 35 to 39 years is 5,850
                 MEDIAN GROSS MONTHLY INCOME for ages between 40 to 44 years is 5,958
                 MEDIAN GROSS MONTHLY INCOME for ages between 45 to 49 years is 5,833
                 MEDIAN GROSS MONTHLY INCOME for ages between 50 to 54 years is 5,000
                 MEDIAN GROSS MONTHLY INCOME for ages between 55 to 59 years is 3,792
                 MEDIAN GROSS MONTHLY INCOME for ages between 60 to 100 years is 2,475""",
},
    {
            "role": "user",
            "content": prompt
        }
    ]

}
    st.session_state['messages'].append({"role": "user", "content": prompt})

    completion = requests.post(url, headers=headers, data=json.dumps(data))
    # response = requests.post(url, headers=headers, data=json.dumps(data))   
    if completion.status_code == 200: 
            response = completion.json()["choices"][0]["message"]["content"]
            response=response.replace('[doc1]','')
            response=response.replace('[doc2]','')
            response=response.replace('[doc3]','')
            response= str(response)

            st.session_state['messages'].append({"role": "assistant", "content": response})
            total_tokens = str(completion.json()["usage"]["total_tokens"])
            prompt_tokens = str(completion.json()["usage"]["prompt_tokens"])
            completion_tokens = str(completion.json()["usage"]["completion_tokens"])
       
            return response, total_tokens, prompt_tokens, completion_tokens
    else:
            st.write("Failed to fetch data") 
            st.write("Status code:", response.status_code)
            st.write("Response:", response.json())


# Initialise session state variables
if 'generated' not in st.session_state:
    st.session_state['generated'] = []
if 'past' not in st.session_state:
    st.session_state['past'] = []
if 'messages' not in st.session_state:
    st.session_state['messages'] = [
        {"role": "system", "content": "You are a helpful assistant."}
    ]
if 'model_name' not in st.session_state:
    st.session_state['model_name'] = []
if 'cost' not in st.session_state:
    st.session_state['cost'] = []
if 'total_tokens' not in st.session_state:
    st.session_state['total_tokens'] = []
if 'total_cost' not in st.session_state:
    st.session_state['total_cost'] = 0.0

# Sidebar - let user choose model, show total cost of current conversation, and let user clear the current conversation
# st.sidebar.title("Sidebar")
model_name = st.sidebar.radio("Choose a model:", ("Azure-Gen-AI(GPT3.5)", "Oracle-Gen-AI(Cohere)"))
counter_placeholder = st.sidebar.empty()
counter_placeholder.write(f"Total cost of this conversation: ${st.session_state['total_cost']:.5f}")
clear_button = st.sidebar.button("Clear Conversation", key="clear")

# Map model names to OpenAI model IDs
if model_name == "GPT-3.5":
    model = "gpt-3.5-turbo"
else:
    model = "gpt-4"

# reset everything
if clear_button:
    st.session_state['generated'] = []
    st.session_state['past'] = []
    st.session_state['messages'] = [
        {"role": "system", "content": "You are a Singlife Advisor assistant."}
    ]
    st.session_state['number_tokens'] = []
    st.session_state['model_name'] = []
    st.session_state['cost'] = []
    st.session_state['total_cost'] = 0.0
    st.session_state['total_tokens'] = []
    counter_placeholder.write(f"Total cost of this conversation: ${st.session_state['total_cost']:.5f}")
# container for chat history
response_container = st.container()
# container for text box
container = st.container()
with container:
    with st.form(key='my_form', clear_on_submit=True):
    # st.write('data')
     user_input = st.text_area("Enter Q&A  :", key='prompt')
     submit_button = st.form_submit_button(label='Send')
    # input_data = "Create summary in 300 words in very simple english language without any grammar mistake ,simple sentence ,active voice and use more we and you and keep usage of promoun for below conversation between Financial Advisor and Customer :\n\nConversation:"+prompt
    # submit_form = st.form_submit_button(label="submit", help="Click to submit")
     if user_input and submit_button:
        output, total_tokens, prompt_tokens, completion_tokens = generate_response(user_input)
        st.session_state['past'].append(user_input)
        st.session_state['generated'].append(output)
        st.session_state['model_name'].append(model_name)
        st.session_state['total_tokens'].append(total_tokens)

        # from https://openai.com/pricing#language-models
        # st.write("total_tokens....",total_tokens)
        if model_name == "GPT-3.5":
            total_tokens=float(total_tokens)
            cost = (total_tokens * 0.002)/ 1000
        
        else:
            prompt_tokens=float(prompt_tokens)
            completion_tokens= float(completion_tokens)
            cost = (prompt_tokens * 0.03) + (completion_tokens * 0.06) / 1000

        st.session_state['cost'].append(cost)
        st.session_state['total_cost'] += cost

if st.session_state['generated']:
    with response_container:
        for i in range(len(st.session_state['generated'])):
            message(st.session_state["past"][i], is_user=True, key=str(i) + '_user')
            message(st.session_state["generated"][i], key=str(i))
            # st.write(
            #     f"Model used: {st.session_state['model_name'][i]}; Number of tokens: {st.session_state['total_tokens'][i]}; Cost: ${st.session_state['cost'][i]:.5f}")
            # counter_placeholder.write(f"Total cost of this conversation: ${st.session_state['total_cost']:.5f}")
      





