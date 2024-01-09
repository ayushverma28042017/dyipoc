import requests
import json
import streamlit as st
from dotenv import load_dotenv
import os 

load_dotenv(".streamlit/secrets.toml")
url=os.environ["AZURE_OPENAI_ENDPOINT_CHAT"]
api_key=os.environ["AZURE_OPENAI_API_KEY"]
 
headers = {

    "api-key": api_key,

    "Content-Type": "application/json"
}
def rewerite(prompt):

      data = {
         "dataSources": [
                {
            "type": "AzureCognitiveSearch",
            "parameters": {
                "endpoint": "https://cognitive-search-dyi.search.windows.net",
                "key": api_key,
                "indexName": "premium-index"
            }
                 }
    ],
    "model": "GPT-4",
    "messages": [
        {
            "role": "system",
            "content": "rewrite as  financial advisor"
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
            st.write(response.json())
            st.write(response.json()["choices"][0]["message"]["content"])
      else:
            st.write("Failed to fetch data") 
            st.write("Status code:", response.status_code)
            st.write("Response:", response.json())
