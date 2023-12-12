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

def find_value(age):  
    if age >= 15 and age <= 19:  
        return 1198  
    elif age >= 20 and age <= 24:  
        return 2500  
    elif age >= 25 and age <= 29:  
        return 3850  
    elif age >= 30 and age <= 34:  
        return 5000  
    elif age >= 35 and age <= 39: 
        return 5850  
    elif age >= 40 and age <= 44:  
        return 5958  
    elif age >= 45 and age <= 49:  
        return 5833  
    elif age >= 50 and age <= 54:  
        return 5000  
    elif age >= 55 and age <= 59:  
        return 3792  
    elif age >= 60:  
        return 2475  
    else:  
        return "Invalid age input"     

def contraint_1(salary):
    C1= 9 * salary
    C2 = 4 * salary
    return C1 ,C2

def find_minimum_of_3(a, b, c):  
    if a <= b and a <= c:  
        return a  
    elif b <= a and b <= c:  
        return b  
    else:  
        return c 
    
def find_minimum_of_2(a, b):  
    if a <= b:  
        return a  
    else:  
        return b  
def contraint_3(P1,P2,P3):
     P3 = (15 *P3 )/100
    #  st.write("P3 is >> ",P3)
     if P1+P2 < P3 : 
        
        return True
     else : 
         
         return False
     
 
# def calculate_premium(G1,G2): 
#     P1 = annual premium corresponding to G1​
#     P2 = annual premium corresponding to G2​
#     P3 = 15% of median annual salary​
      
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
         if(contraint_3(int(G1),int(G2),int(med_sal))):
             
             A1_data = open("A_1.txt","r")
             st.write(A1_data.read())
         else:
            
            A2_data = open("A_2.txt","r")
            st.write(A2_data.read()) 
           
     
    # else:
    #   C_data = open("C.txt","r")
    #   st.write(C_data.read())
          #  st.write("you are NOT Citizend and Mendef")
           
  
          
if __name__ == '__main__':
    main()
