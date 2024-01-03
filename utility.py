import streamlit as st
import sqlite3
import pandas as pd
import openpyxl as openpyxl
from datetime import date

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

def premium_lcsaf(age):
     if 1 <=age <=20 :  
        return 2.20
     elif 21 <=age <=25 :  
        return 2.60
     elif 26 <=age <=30 :  
        return 3.70 
     elif 31 <=age <=35 :  
        return 5.40
     elif 36 <=age <=40 :  
        return 9.00
     elif 41 <=age <=45 :  
        return  9.00
     elif 46 <=age <=50 :  
        return 24.80
     elif 51 <=age <=55 :  
        return 37.80
     elif 56 <=age <=60 :  
        return 52.20
     elif 61 <=age <=65 :    
        return 72.70
     elif 66 :
      return 94.50
     elif 67:
      return 105.80
     elif 68 :
      return 118.40
     elif 69 :
      return 132.50
     elif 70 :
      return 148.50
     
def premium_tlsaf(age):
     if 1 <=age <=20 :  
        return 2.50
     elif 21 <=age <=25 :  
        return 2.50
     elif 26 <=age <=30 :  
        return 2.50 
     elif 31 <=age <=35 :  
        return 2.50
     elif 36 <=age <=40 :  
        return 2.50
     elif 41 <=age <=45 :  
        return  2.50
     elif 46 <=age <=50 :  
        return 2.50
     elif 51 <=age <=55 :  
        return 2.50
     elif 56 <=age <=60 :  
        return 2.50
     elif 61 <=age <=65 :    
        return 2.50
     elif 66 :
      return 35.30
     elif 67:
      return 40.10
     elif 68 :
      return 48.30
     elif 69 :
      return 57.40
     elif 70 :
      return 63.00
     2.50



def getMdianSalary_by_AgeRange(age):
    if 0 <=age <=19 :  
        return 1198 
    elif 20 <=age <=24 :  
        return 2500 
    elif 25 <=age <=29 :  
        return 3850 
    elif 30 <=age <=34 :  
        return 5000
    elif 35 <=age <=39 :  
        return 5850
    elif 40 <=age <=44 :  
        return  5958
    elif 45 <=age <=49 :  
        return 5833 
    elif 50 <=age <=54 :  
        return 5000 
    elif 55 <=age <=59 :  
        return 3792 
    elif 60 <=age :  
        return 2475


def getCover_by_LIA_guideline(product_code , median_sal):
    if product_code =="LCSAF" :
     return 4 * median_sal 
    else:
     return 9* median_sal
    
def calculate_recommndation(product_code , lc_cover):
    if product_code == "TLSAF" :
     return min(lc_cover,1000000) 
    else:
     return min(lc_cover,500000) 
    
def calculate_delta(G,CE):
    temp = G - CE;
    return max(0 , temp)

def sa_suggestion(D,SA):
    return (D+SA)




def calculate_age(born):
    today = date.today()
    return today.year - born

def v_customer_workflow(nric):
     con = sqlite3.connect("customer.db")
     cur = con.cursor()
     cur.execute("SELECT PRODUCT_CODE, ANNUAL_PREMIUM, ACCEPTED_SA_AMT, DOB FROM customer where NRIC='"+nric+"';")
     found_records = cur.fetchall();
     PE2=0
     CE2=0
     PE1=0
     CE1=0
     DOB = ""

     for record in found_records:
        if(record[0]=='TLSAF'):
           PE1 = record[1]
           CE1 = record[2]
           DOB = record[3]
        elif (record[0]=='LCSAF'):
          PE2 = record[1]
          CE2 = record[2]
        
       
    #  st.write("found_record >>>> :",found_records)
    
     
    #  if (found_record.fetchone() == None):
    #   st.write("NO  found_record :",found_record)
    #  else:
    #   st.write("found_record :",found_record)

    # found_record= "select PRODUCT_CODE,ANNUAL_PREMIUM,ACCEPTED_SA_AMT,DOB from customer where nric="+nric+";";
    #  PRODUCT_CODE = found_record[0]
    #  ANNUAL_PREMIUM = found_record[1]
    #  ACCEPTED_SA_AMT = found_record[2]
    #  DOB = found_record[3]
    #  st.write("PRODUCT_CODE :",PRODUCT_CODE)
   #   st.write("ANNUAL_PREMIUM :",PE1)
   #   st.write("ACCEPTED_SA_AMT :",CE1)
   #   st.write("ANNUAL_PREMIUM :",PE2)
   #   st.write("ACCEPTED_SA_AMT :",CE2)
   #   st.write("DOB :",DOB)

     year_of_birth  = DOB.split('-')[0]

   #   st.write("year_of_birth :",year_of_birth)

     age = calculate_age(int(year_of_birth))
   #   st.write("age  :",age)


     median_sal= getMdianSalary_by_AgeRange(int(age))
   #   st.write("getMdianSalary_by_AgeRange :",median_sal)

    # Constraint 1 
     c1= 9 * median_sal 
     c2= 4 * median_sal 
   #   st.write("cover_c1 :",c1)
   #   st.write("cover_c2 :",c2)

     # Constraint 2
     G1 =  min(c1,1000000)
     G2=  min(c2,500000)
   #   st.write("recommend_value_g1 :",G1)
   #   st.write("recommend_value_g2 :",G2)


    #Deltas 
     d1 = max(0,(G1-CE1))
     d2 = max(0,(G2-CE2))
   #   st.write("delta_1 :",d1)
   #   st.write("delta_2 :",d2)

     
     #New SA to clsoe GAP
     G1A = CE1+d1
     G2A = CE2 +d2
   #   st.write("G1_A :",G1A)
   #   st.write("G2_A :",G2A)

     #calculate permium pay base on above
     P1= premium_tlsaf(age) *12
     P2= premium_lcsaf(age) *12
     P3=(median_sal *15)/100

     if(P1+P2 <=P3):
        st.write(msg_to_user(PE1,PE2,CE1,CE2,median_sal,c1,c2,G1,G2,P1,P2,P3))
        # st.write("B1...B9.. write")
     else:
        st.write("B1...B9.. write")


    #  st.write("calculate_delta :",calculate_delta)
    #  sa_sug = sa_suggestion(int(delta),int(ANNUAL_PREMIUM))
    #  st.write("sa_suggestion :",sa_sug)
    #  if(PRODUCT_CODE == "LCSAF" ):
    #    premium =premium_lcsaf(int(age))
    #  else:
    #    premium =premium_tlsaf(int(age))
    
    #  st.write("premium :",premium)
       



    
    
# def non_v_customer_workflow(nric):
#     #check if NRIC in Voluntary Scheme
#         ismendef = is_v_scheme_customer(nric)
#         st.write("ismendefn!!",ismendef)
#           # st.write("Mendef" ,ismendef)
#           # check for PR and age
#         isCitizen=is_pr(nric[0])
#       #   st.write("isCitizen" ,isCitizen)
#         if(isCitizen):
#          st.write("you are Citizend and Mendef")
#          med_sal= find_value(int(nric[1:3]))
#         #  st.write("med_sal >>> " ,med_sal)
#          C1,C2= contraint_1(int(med_sal))
#         #  st.write("C1 .C2 >>>>" ,C1,C2)
#          G1 = find_minimum_of_2(int(C1), 1000000)
#          G2= find_minimum_of_3(int(G1), int(C2), 500000)
#         #  st.write("G1 >> " ,G1)
#         #  st.write("G2 >> " ,G2)
#         #  if(contraint_3(int(G1),int(G2),int(med_sal))):
             
#         #      A1_data = open("A_1.txt","r")
#         #      st.write(A1_data.read())
#         #  else:
            
#         #     A2_data = open("A_2.txt","r")
#         #     st.write(A2_data.read()) 
           
     
#     # else:
#     #   C_data = open("C.txt","r")
#     #   st.write(C_data.read())
#           #  st.write("you are NOT Citizend and Mendef")
 
def read_sample_customer():
     #local
   #   customer = pd.read_excel(".\\resources\\Sample_Customer_Data.xlsx", sheet_name='TestSet')
     customer = pd.read_excel("Sample_Customer_Data.xlsx", sheet_name='TestSet'
     upload_xls_to_Db(customer,"customer")
    #  return customer

def read_voluntry_scheme():
     v_scheme = pd.read_excel("resources\\Voluntary_Scheme_Premiu_Table.xlsx", sheet_name='premiums')
     upload_xls_to_Db(v_scheme,"v_scheme")
    #  return v_scheme


def upload_xls_to_Db(wb,dbname):
           cxn = sqlite3.connect(dbname+'.db')
        #    wb = pd.read_excel("C:\\Users\\ayush\\OneDrive - Singapore Life\\Documents\\projects\\dyipoc\\dyi_test.xlsx", sheet_name='TestSet')
           #append
           
           wb.to_sql(name=dbname,con=cxn,if_exists='replace',index=True)
           cxn.commit()
           cxn.close()   

def is_v_scheme_customer(nric):
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


# def validate_nric(nric):
#     # this is a simple script to valiate nric numbers

#     # grab user input
#     nric = input('Enter the nric to validate: ')

#     x = (int(nric[1]) * 2) + (int(nric[2]) * 7) + (int(nric[3]) * 6) + (int(nric[4]) * 5) + (int(nric[5]) * 4) + (int(nric[6]) * 3) + (int(nric[7]) * 2)

#     if nric[0] == 'T' or nric[0] == 'G':
#         x = x + 4

#     y = x % 11

#     if nric[0] == 'S' or nric[0] == 'T':
#         z = last_char1(y)

#         if nric[8] == z:
#             print('nric is valid!\n')
#             quit()
#         else:
#             print('nric is invalid!\n')
#             quit()
#     elif nric[0] == 'F' or nric[0] == 'G':
#         z = last_char2(y)

#         if nric[8] == z:
#             return True
            
#         else:
#             return True
            

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

# def contraint_1(salary):
#     C1= 9 * salary
#     C2 = 4 * salary
#     return C1 ,C2

# def find_minimum_of_3(a, b, c):  
#     if a <= b and a <= c:  
#         return a  
#     elif b <= a and b <= c:  
#         return b  
#     else:  
#         return c 
    
# def find_minimum_of_2(a, b):  
#     if a <= b:  
#         return a  
#     else:  
#         return b  
# def contraint_3(P1,P2,P3):
#      P3 = (15 *P3 )/100
#     #  st.write("P3 is >> ",P3)
#      if P1+P2 < P3 : 
#         msg_to_user(G1,CE1,G2,CE2)
#         return True
#      else : 
         
#          return False
     

def msg_to_user(PE1,PE2,CE1,CE2,median_sal,c1,c2,G1,G2,P1,P2,P3):
   if(G1 <CE1 and G2 < CE2):
      #B1
      return getCommonMSg_1(median_sal)+B1()+getCommonMSg_2(CE1,PE1,CE2,PE2,(P1+P2),((P1+P2)/median_sal))+getB1_B4()
   elif(G1 <CE1 and G2 ==CE2):
      #B3
      return getCommonMSg_1(median_sal)+B3()+getCommonMSg_2(CE1,PE1,CE2,PE2,(P1+P2),((P1+P2)/median_sal))+getB1_B4()+getCommonMSG_last()
   elif(G1 <CE1 and G2 > CE2):
      #B7
      return getCommonMSg_1(median_sal)+B7()+getCommonMSg_2(CE1,PE1,CE2,PE2,(P1+P2),((P1+P2)/median_sal))+getB7_B8(CE1,PE1,G2,P2,(P1+P2),((P1+P2)/median_sal))+getCommonMSG_last()
   elif(G1 ==CE1 and G2 <CE2):
      #B2
      return getCommonMSg_1(median_sal)+B2()+getCommonMSg_2(CE1,PE1,CE2,PE2,(P1+P2),((P1+P2)/median_sal))+getB1_B4()+getCommonMSG_last()
   elif(G1 ==CE1 and G2 ==CE2):
      #B4
      return getCommonMSg_1(median_sal)+B4()+getCommonMSg_2(CE1,PE1,CE2,PE2,(P1+P2),((P1+P2)/median_sal))+getB1_B4()+getCommonMSG_last()
   elif(G1 ==CE1 and G2 >CE2):
      #B8
      return getCommonMSg_1(median_sal)+B8()+getCommonMSg_2(CE1,PE1,CE2,PE2,(P1+P2),((P1+P2)/median_sal))+ getB7_B8(CE1,PE1,G2,P2,(P1+P2),((P1+P2)/median_sal))+getCommonMSG_last()
   elif(G1 >CE1 and G2 <CE2):
      #B5
      return getCommonMSg_1(median_sal)+B5()+getCommonMSg_2(CE1,PE1,CE2,PE2,(P1+P2),((P1+P2)/median_sal))+getB5_B6(G1,P1,CE2,PE2,(P1+P2),((P1+P2)/median_sal))+getCommonMSG_last()
   elif(G1 >CE1 and G2 ==CE2):
      #B6
      return getCommonMSg_1(median_sal)+B6()+getCommonMSg_2(CE1,PE1,CE2,PE2,(P1+P2),((P1+P2)/median_sal))+getB5_B6(G1,P1,CE2,PE2,(P1+P2),((P1+P2)/median_sal))+getCommonMSG_last()
   elif(G1 <CE1 and G2 >CE2):
      #B9
      return getCommonMSg_1(median_sal)+B9()+getCommonMSg_2(CE1,PE1,CE2,PE2,(P1+P2),((P1+P2)/median_sal))+getB9(G1,P1,G2,P2,(P1+P2),((P1+P2)/median_sal))+getCommonMSG_last()
   

     
def getCommonMSg_1(median_sal):
    return f"""\n\nThank you for being a member of the MINDEF-MHA voluntary group insurance scheme.
    \n​The median annual income of people in your age group is {median_sal}​ .
    \nAt Singlife, we protect those who have served to protect Singapore."""
 

def getCommonMSg_2(ce1,pe1,ce2,pe2,p1bp2b,pe1pe2median):
    return f"""\n\nYou are currently protected by the following MINDEF-MHA voluntary group insurance plans:​

\nDeath cover of {ce1} with annual premium of {pe1} and monthly

\nCritical illness cover of {ce2} with annual premium of {pe2}

\nThis annual premium of {p1bp2b} is only {pe1pe2median}of the median annual income of people in your age group.​"""
 

def getB1_B4():
   return """\n\nOur Singlife Relationship Consultants will be contacting you to help you optimize your protection portfolio and chart you path towards financial freedom.​
   \nShare your discovery and commitment to start your financial freedom by clicking here this is where we have the hyperlink to post to social media."""

def getB5_B6(g1b,p1b,ce2,pe2,p1bpe2,p1bpe2median):
   return f"""\n\nYou could consider the following covers as your foundation protection as recommended by the LIA financial planning guide*:​

Increase your death to {g1b} with annual premium of {p1b}

Maintain your critical illness cover at {ce2} with annual premium of {pe2}

This annual premium of {p1bpe2} is only {p1bpe2median} % of the median annual income of people in your age group.​

Click on the following links to be protected today​

MINDEF : https://ebh.singlife.com/eb/mindef-mha/?MINDEF​

MHA : https://ebh.singlife.com/eb/mindef-mha/?groupName=MHA​

Our Singlife Relationship Consultants will be contacting you to help you close your protection gap and chart you path towards financial freedom.​

Share your discovery and commitment to start your financial freedom by clicking here https://facebook.com/  \n https://instagram.com/.​"""


def getB7_B8(ce1,pe1,g2b,p2b,pe1p2b,pe12bmedian):
   return f"""\n\nYou could consider the following covers as your foundation protection as recommended by the LIA financial planning guide*:​

Maintain your death to {ce1} with annual premium of {pe1}

Increase your critical illness cover at {g2b} with annual premium of {p2b}

This annual premium of {pe1p2b} is only {pe12bmedian}  % of the median annual income of people in your age group.​

Click on the following links to be protected today​

MINDEF : https://ebh.singlife.com/eb/mindef-mha/?MINDEF​

MHA : https://ebh.singlife.com/eb/mindef-mha/?groupName=MHA​

Our Singlife Relationship Consultants will be contacting you to help you close your protection gap and chart you path towards financial freedom.​

Share your discovery and commitment to start your financial freedom by clicking here https://facebook.com/  \n https://instagram.com/."""

def getB9(g1b,p1b,g2b,p2b,p1np2b,p1bp2bmedain):
   return f"""\n\nYou could consider the following covers as your foundation protection as recommended by the LIA financial planning guide*:​

Increase your death to {g1b} with annual premium of {p1b}

Increase your critical illness cover at {g2b} with annual premium of {p2b}

This annual premium of {p1np2b} is only {p1bp2bmedain} of the median annual income of people in your age group.​

Click on the following links to be protected today​

MINDEF : https://ebh.singlife.com/eb/mindef-mha/?MINDEF​

MHA : https://ebh.singlife.com/eb/mindef-mha/?groupName=MHA​

Our Singlife Relationship Consultants will be contacting you to help you close your protection gap and chart you path towards financial freedom.​

Share your discovery and commitment to start your financial freedom by clicking here https://facebook.com/  \n https://instagram.com/."""


def getCommonMSG_last():
   return """\n\n LIA financial planning guide recommends to have​
               Death cover of at least 9x annual income.​ Critical illness of at least 4x annual income.​To spend no more than 15% of annual income on premium for insurance protection."""


def B1():
   return """\n\n You are currently well covered for death and critical illness."""
def B2():
   return """ \n\n You currently have good protection for death and well covered for critical illness."""
def B3():
   return """\n\nYou are currently well covered for death and have good cover for critical illness."""
def B4():
   return """\n\nYou currently have good cover for death critical illness.."""
def B5():
   return """ \n\nYou are currently under protected for death and  and well covered for critical illness"""
def B6():
   return """ You are currently under covered for death and have good cover for critical illness."""
def B7():
   return """\n\nYou are currently well covered for death and under covered for critical illness."""
def B8():
   return """\n\nYou currently have good cover for death and under covered for critical illness."""
def B9():
   return """\n\nYou are currently under covered for death and critical illness."""
