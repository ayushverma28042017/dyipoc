from dotenv import load_dotenv
import streamlit as st
import sqlite3
import pandas as pd
import openpyxl as openpyxl


def upload_xls_to_Db():
           cxn = sqlite3.connect("dyi_mask_data"+'.db')
           wb = pd.read_excel("C:\\Users\\ayush\\OneDrive - Singapore Life\\Documents\\projects\\dyipoc\\dyi_test.xlsx", sheet_name='TestSet')
           wb.to_sql(name="dyi_mask_data",con=cxn,if_exists='replace',index=True)
           cxn.commit()
           cxn.close()   
def check_if_mendef(nric):
          con = sqlite3.connect("dyi_mask_data.db")
          cur = con.cursor()
          rows = cur.execute("SELECT NRIC_NAME FROM dyi_mask_data where NRIC='"+nric+"';")
          if (rows.fetchone() == None):
           return False
          else:
              return True
def is_pr(isPR):
     if(isPR =='S' or isPR =='T'):
        return True
     else:
         return False
def getAge(nric):
    return nric[1:3]
    
def validation():
    st.write(" fill the required information")

     
def main():
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
    
          submit = st.form_submit_button(label="submit", help="Click to submit!")
    
    if submit:
        if not(name and nric and option) :
          return validation()
        else: 
          ismendef = check_if_mendef(nric)
          st.write("Mendef" ,ismendef)
          # check for PR and age
        isCitizen=is_pr(nric[0])
        st.write("isCitizen" ,isCitizen)
        if(isCitizen):
         st.write("you are Citizend and Mendef")
        else:
           C_data = open("C.txt","r")
           st.write(C_data.read())
          #  st.write("you are NOT Citizend and Mendef")
  
          
if __name__ == '__main__':
    main()
