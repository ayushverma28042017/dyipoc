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
        else: 
          #check if NRIC in Voluntary Scheme
         ismendef = check_if_mendef(nric)
         st.write("ismendefn!!",ismendef)
          # st.write("Mendef" ,ismendef)
          # check for PR and age
        isCitizen=is_pr(nric[0])
        st.write("isCitizen" ,isCitizen)
        if(isCitizen):
         st.write("you are Citizend and Mendef")
         med_sal= find_value(int(nric[1:3]))
        #  st.write("med_sal >>> " ,med_sal)
         C1,C2= contraint_1(int(med_sal))
        #  st.write("C1 .C2 >>>>" ,C1,C2)
         G1 = find_minimum_of_2(int(C1), 1000000)
         G2= find_minimum_of_3(int(G1), int(C2), 500000)
        #  st.write("G1 >> " ,G1)
        #  st.write("G2 >> " ,G2)
        #  if(contraint_3(int(G1),int(G2),int(med_sal))):
             
        #      A1_data = open("A_1.txt","r")
        #      st.write(A1_data.read())
        #  else:
            
        #     A2_data = open("A_2.txt","r")
        #     st.write(A2_data.read()) 
           
     
    # else:
    #   C_data = open("C.txt","r")
    #   st.write(C_data.read())
          #  st.write("you are NOT Citizend and Mendef")
def init():
   read_sample_customer()
   read_voluntry_scheme()
   readIncome()

          
if __name__ == '__main__':
    main()
