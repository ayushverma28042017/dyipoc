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
def rewerite(prompt):

      data = {
         "dataSources": [
                {
            "type": "AzureCognitiveSearch",
            "parameters": {
                "endpoint": "https://cognitive-search-dyi.search.windows.net",
                "key": azureSearchKey,
                "indexName": "premium-index"
            }
                 }
    ],
    "model": "GPT-4",
    "messages": [
        {
            "role": "system",
            "content": "you are a financial advisor"
        },
        {
            "role": "user",
            "content": "rewrite " +{prompt}
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
