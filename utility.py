import streamlit as st
import sqlite3
import pandas as pd
import openpyxl as openpyxl

# def find_data(df,var):
#    for col in list(df):
#     try:    
#         df[col] == var
#         return df[df[col] == var]
#     except TypeError:
#         continue 
     
def readIncome():
     income = pd.read_excel("resources\\Median_ Income_ from_ Ministry_of_ Manpower.xlsx", sheet_name='For Model')
     upload_xls_to_Db(income,"income")
    #  data = income.columns.values[0]
    #  st.write(income)
    #  st.write(find_data(income,10))
    #  income[income.eq("3,850").any(1)]
    #  st.write(income.columns.values[4])
    #  st.write(income.columns.values[5])
    #  return income

def read_sample_customer():
     customer = pd.read_excel("resources\\Sample_Customer_Data.xlsx", sheet_name='TestSet')
     upload_xls_to_Db(customer,"customer")
    #  return customer

def read_voluntry_scheme():
     v_scheme = pd.read_excel("resources\\Voluntary_Scheme_Premiu_Table.xlsx", sheet_name='premiums')
     upload_xls_to_Db(v_scheme,"v_scheme")
    #  return v_scheme


def upload_xls_to_Db(wb,dbname):
           cxn = sqlite3.connect(dbname+'.db')
        #    wb = pd.read_excel("C:\\Users\\ayush\\OneDrive - Singapore Life\\Documents\\projects\\dyipoc\\dyi_test.xlsx", sheet_name='TestSet')
           wb.to_sql(name=dbname,con=cxn,if_exists='replace',index=True)
           cxn.commit()
           cxn.close()   
           
def check_if_mendef(nric):
          con = sqlite3.connect("customer.db")
          cur = con.cursor()
          rows = cur.execute("SELECT NRIC_NAME FROM customer where NRIC='"+nric+"';")
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
def last_char1(val):
    switch = {
        0: 'J',
        1: 'Z',
        2: 'I',
        3: 'H',
        4: 'G',
        5: 'F',
        6: 'E',
        7: 'D',
        8: 'C',
        9: 'B',
        10: 'A'
    }
    return switch.get(val)


def last_char2(val):
    switch = {
        0: 'X',
        1: 'W',
        2: 'U',
        3: 'T',
        4: 'R',
        5: 'Q',
        6: 'P',
        7: 'N',
        8: 'M',
        9: 'L',
        10: 'K'
    }
    return switch.get(val)


def validate_nric(nric):
    # this is a simple script to valiate nric numbers

    # grab user input
    nric = input('Enter the nric to validate: ')

    x = (int(nric[1]) * 2) + (int(nric[2]) * 7) + (int(nric[3]) * 6) + (int(nric[4]) * 5) + (int(nric[5]) * 4) + (int(nric[6]) * 3) + (int(nric[7]) * 2)

    if nric[0] == 'T' or nric[0] == 'G':
        x = x + 4

    y = x % 11

    if nric[0] == 'S' or nric[0] == 'T':
        z = last_char1(y)

        if nric[8] == z:
            print('nric is valid!\n')
            quit()
        else:
            print('nric is invalid!\n')
            quit()
    elif nric[0] == 'F' or nric[0] == 'G':
        z = last_char2(y)

        if nric[8] == z:
            return True
            
        else:
            return True
            
def validation(nric):
 if validate_nric(nric)== False:
  st.write(" NRIC is not valid ")
  return False
 else :
     return True

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