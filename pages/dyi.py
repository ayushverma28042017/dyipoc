from dotenv import load_dotenv
import streamlit as st
import openpyxl as openpyxl
from utility import *  
from non_vcustomer import *   
import re  
 
      
def main():
    # init()
    load_dotenv(".streamlit/secrets.toml")
    st.image("logo.JPG", width=100)
    st.title("Let's discover how you can achieve an affordable protection portfolio with Singlife...")
#     st.set_page_config(
#      page_title="Discover Your Insurance",
#      page_icon="🧊",
#      layout="centered",
#      initial_sidebar_state="auto"
# )
    # st.set_page_config(page_title="Enter details")
    # st.header("Enter your details 💬")
    
    with st.form(key = "Info"):
          # st.write("Inside the form")
        #   st.header("Are you an existing MINDEF & MHA Group Insurance member?")
        #   st.header("Enter your details to check if you are an existing insured member")
        #   genaimsg = st.checkbox('Use genAI for message')
          name=st.text_input(label = "Please enter your **Name**")
          nric=st.text_input(label = "Please enter a **NRIC** number ")
          option = st.selectbox(
        "Select Gender",
        ("Male", "Female"))
          phonNo=st.text_input(label = "Please enter **Phone No**")
          email=st.text_input(label = "Please enter **Email** ")
    
          submit = st.form_submit_button(label="**Check now**", help="Click to submit!")
    
    if submit:
        if not(name and nric and option and phonNo and email) :
          st.write("Please enter the mandatory information!!")
          return 
        if not(check(email)):
         st.write("Please enter the valid  email ")
        # elif a:
        #  validation()
        elif is_v_scheme_customer(nric)==True:
           v_customer_workflow(nric,name)
        else :
          new_customer_workflow(nric,name)
          # non_v_customer_workflow(nric)
         
         
# def init():
#   #  read_sample_customer()
#   #  read_voluntry_scheme()
#   #  readIncome()
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
def check(email):
 
    # pass the regular expression
    # and the string into the fullmatch() method
    if(re.fullmatch(regex, email)):
        # print("Valid Email")
        return True
 
    else:
        # print("Invalid Email")
        return False
          
if __name__ == '__main__':
    main()
