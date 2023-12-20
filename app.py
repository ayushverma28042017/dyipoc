from dotenv import load_dotenv
import streamlit as st
import openpyxl as openpyxl
from utility import *     
 
      
def main():
    init()
    load_dotenv(".streamlit/secrets.toml")
    st.set_page_config(page_title="Enter details")
    st.header("Enter your details 💬")
    
    with st.form(key = "Info"):
          st.write("Inside the form")
          name=st.text_input(label = "Enter the your name")
          nric=st.text_input(label = "Enter the nric ")
          option = st.selectbox(
        "Gender?",
        ("Male", "Female"))
          phonNo=st.text_input(label = "Enter the phone No ")
          email=st.text_input(label = "Enter the email ")
    
          submit = st.form_submit_button(label="submit", help="Click to submit!")
    
    if submit:
        if not(name and nric and option and phonNo and email) :
          st.write("Please enter the mandatory information!!")
          return 
        # elif a:
        #  validation()
        elif is_v_scheme_customer(nric)==True:
           v_customer_workflow(nric)
        else :
          v_customer_workflow(nric)
          # non_v_customer_workflow(nric)
         
         
def init():
   read_sample_customer()
  #  read_voluntry_scheme()
  #  readIncome()

          
if __name__ == '__main__':
    main()
