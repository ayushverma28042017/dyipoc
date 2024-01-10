import requests
import json
import streamlit as st
from dotenv import load_dotenv
import os 

load_dotenv(".streamlit/secrets.toml")
url=os.environ["api_base_url"]
api_key=os.environ["AZURE_OPENAI_API_KEY"]
azureSearchKey=os.environ["azureSearchKey"]
 
headers = {

    "api-key": api_key,

    "Content-Type": "application/json"
}
with st.form(key = 'userdata'):
    # st.write('data')
    prompt = st.text_area("Enter Q&A  :", key='prompt')
    # input_data = "Create summary in 300 words in very simple english language without any grammar mistake ,simple sentence ,active voice and use more we and you and keep usage of promoun for below conversation between Financial Advisor and Customer :\n\nConversation:"+prompt
    submit_form = st.form_submit_button(label="submit", help="Click to submit")
    if submit_form:
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
    "messages": [
        {
            "role": "system",
            "content": "you are a Financial advisor assistant who helps people find information and responds in simple english . If the user asks you a question you don't know the answer to, say so"
        },
        {
            "role": "user",
            "content": prompt
        }
    ]

}
      response = requests.post(url, headers=headers, data=json.dumps(data))   
      if response.status_code == 200: 
            st.write("Success!!!!")   
            # st.write(response.json())
            st.write(response.json()["choices"][0]["message"]["content"])
      else:
            st.write("Failed to fetch data") 
            st.write("Status code:", response.status_code)
            st.write("Response:", response.json())
