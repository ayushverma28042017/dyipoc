# from dotenv import load_dotenv
# import streamlit as st
# import openpyxl as openpyxl
# from utility import *  
# from non_vcustomer import *    
 
      
# def main():
#     # init()
#     load_dotenv(".streamlit/secrets.toml")
#     st.image("logo.JPG", width=100)
#     st.title("Discover you Insurance ..")
# #     st.set_page_config(
# #      page_title="Discover Your Insurance",
# #      page_icon="🧊",
# #      layout="centered",
# #      initial_sidebar_state="auto"
# # )
#     # st.set_page_config(page_title="Enter details")
#     # st.header("Enter your details 💬")
    
#     with st.form(key = "Info"):
#           # st.write("Inside the form")
#           genaimsg = st.checkbox('Use genAI for message')
#           name=st.text_input(label = "Enter the your name")
#           nric=st.text_input(label = "Enter the NRIC ")
#           option = st.selectbox(
#         "Select Gender",
#         ("Male", "Female"))
#           phonNo=st.text_input(label = "Enter the phone No ")
#           email=st.text_input(label = "Enter the email ")
    
#           submit = st.form_submit_button(label="submit", help="Click to submit!")
    
#     if submit:
#         if not(name and nric and option and phonNo and email) :
#           st.write("Please enter the mandatory information!!")
#           return 
#         # elif a:
#         #  validation()
#         elif is_v_scheme_customer(nric)==True:
#            v_customer_workflow(nric)
#         else :
#           new_customer_workflow(nric,genaimsg)
#           # non_v_customer_workflow(nric)
         
         
# # def init():
# #   #  read_sample_customer()
# #   #  read_voluntry_scheme()
# #   #  readIncome()

          
# if __name__ == '__main__':
#     main()
