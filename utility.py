import streamlit as st
import sqlite3
import pandas as pd
import openpyxl as openpyxl
from datetime import date
import re
from fpdf import FPDF

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
    if 15 <=age <=19 :  
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

def v_customer_workflow(nric,name):
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
           PE1 = int(record[1])
           CE1 = int(record[2])
           DOB = record[3]
        elif (record[0]=='LCSAF'):
          PE2 = int(record[1])
          CE2 = int(record[2])
        

     year_of_birth  = DOB.split('-')[0]

   #   st.write("year_of_birth :",year_of_birth)

     age = calculate_age(int(year_of_birth))
   #   st.write("age  :",age)


     median_sal= getMdianSalary_by_AgeRange(int(age))
   #   st.write("getMdianSalary_by_AgeRange :",median_sal)

    # Constraint 1 
     c1= 9 * median_sal 
     c2= 4 * median_sal 
 

     # Constraint 2
     G1 =  min(c1,1000000)
     G2=  min(c2,500000)



    #Deltas 
     d1 = max(0,(G1-CE1))
     d2 = max(0,(G2-CE2))


     
     #New SA to clsoe GAP
     G1A = CE1+d1
     G2A = CE2 +d2


     #calculate permium pay base on above
     P1= premium_tlsaf(age) *12
     P2= premium_lcsaf(age) *12
     P3=(median_sal *15)/100
     median_sal = median_sal* 12
   #   st.write("P1 >",P1)
   #   st.write("P2 >",P2)
   #   st.write("P3 >",P3)
     if((P1+P2 <=P3)):
         # st.write("IFFFFFFFFFF >",P3)
      #   st.image('full_cover.png', width=400)
      #   st.write(msg_to_user(PE1,PE2,CE1,CE2,median_sal,c1,c2,G1,G2,P1,P2,P3))
      #   export_as_pdf = st.button("Share")
      #   st.write(clickmindefbot())
         col1, col2 = st.columns(2)
         # col1.image('full_cover.png', use_column_width=True)
         if(P3 > 800):
          col1.image('half.jpg', use_column_width=True)
         else:
          col1.image('full.jpg', use_column_width=True)
         col2.write(msg_to_user(name,PE1,PE2,CE1,CE2,median_sal,c1,c2,G1,G2,P1,P2,P3))
         export_as_pdf = st.button("Share")
         st.write(clickmindefbot())
     else:
         # st.write("elseeeeee >",P3)
      #   st.image('half_cover.png', width=400)
      #   st.write(msg_to_user(PE1,PE2,CE1,CE2,median_sal,c1,c2,G1,G2,P1,P2,P3))
         col1, col2 = st.columns(2)
         # col1.image('half_cover.png', use_column_width=True)
         col1.image('half.jpg', use_column_width=True)
         col2.write(msg_to_user(name,PE1,PE2,CE1,CE2,median_sal,c1,c2,G1,G2,P1,P2,P3))
         export_as_pdf = st.button("Share")
         st.write(clickmindefbot())
 

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

     

def msg_to_user(name,PE1,PE2,CE1,CE2,median_sal,c1,c2,G1,G2,P1,P2,P3):
   if(G1 <CE1 and G2 < CE2):
      #B1
      return getCommonMSg_1(median_sal,name)+B1()+getCommonMSg_2(CE1,PE1,CE2,PE2,(P1+P2),((P1+P2)/median_sal))+getB1_B4()
   elif(G1 <CE1 and G2 ==CE2):
      #B3
      return getCommonMSg_1(median_sal,name)+B3()+getCommonMSg_2(CE1,PE1,CE2,PE2,(P1+P2),((P1+P2)/median_sal))+getB1_B4()+getCommonMSG_last()
   elif(G1 <CE1 and G2 > CE2):
      #B7
      return getCommonMSg_1(median_sal,name)+B7()+getCommonMSg_2(CE1,PE1,CE2,PE2,(P1+P2),((P1+P2)/median_sal))+getB7_B8(CE1,PE1,G2,P2,(P1+P2),((P1+P2)/median_sal))+getCommonMSG_last()
   elif(G1 ==CE1 and G2 <CE2):
      #B2
      return getCommonMSg_1(median_sal,name)+B2()+getCommonMSg_2(CE1,PE1,CE2,PE2,(P1+P2),((P1+P2)/median_sal))+getB1_B4()+getCommonMSG_last()
   elif(G1 ==CE1 and G2 ==CE2):
      #B4
      return getCommonMSg_1(median_sal,name)+B4()+getCommonMSg_2(CE1,PE1,CE2,PE2,(P1+P2),((P1+P2)/median_sal))+getB1_B4()+getCommonMSG_last()
   elif(G1 ==CE1 and G2 >CE2):
      #B8
      return getCommonMSg_1(median_sal,name)+B8()+getCommonMSg_2(CE1,PE1,CE2,PE2,(P1+P2),((P1+P2)/median_sal))+ getB7_B8(CE1,PE1,G2,P2,(P1+P2),((P1+P2)/median_sal))+getCommonMSG_last()
   elif(G1 >CE1 and G2 <CE2):
      #B5
      return getCommonMSg_1(median_sal,name)+B5()+getCommonMSg_2(CE1,PE1,CE2,PE2,(P1+P2),((P1+P2)/median_sal))+getB5_B6(G1,P1,CE2,PE2,(P1+P2),((P1+P2)/median_sal))+getCommonMSG_last()
   elif(G1 >CE1 and G2 ==CE2):
      #B6
      return getCommonMSg_1(median_sal,name)+B6()+getCommonMSg_2(CE1,PE1,CE2,PE2,(P1+P2),((P1+P2)/median_sal))+getB5_B6(G1,P1,CE2,PE2,(P1+P2),((P1+P2)/median_sal))+getCommonMSG_last()
   elif(G1 <CE1 and G2 >CE2):
      #B9
      return getCommonMSg_1(median_sal,name)+B9()+getCommonMSg_2(CE1,PE1,CE2,PE2,(P1+P2),((P1+P2)/median_sal))+getB9(G1,P1,G2,P2,(P1+P2),((P1+P2)/median_sal))+getCommonMSG_last()
   

def clickmindefbot():
   link = '[Mindef-Bot](https://insurancediscovery.streamlit.app/MINDEF_MHA_BOT)'
   st.markdown(link, unsafe_allow_html=True)
     
def getCommonMSg_1(median_sal,name):
    return f""" Hello {name} \n\nThank you for being a member of the MINDEF-MHA voluntary group insurance scheme.
    \n​The median annual income of people in your age group is """+ "${:,.2f}".format(median_sal)+""".
    At Singlife, we protect those who have served to protect Singapore."""
 

def getCommonMSg_2(ce1,pe1,ce2,pe2,p1bp2b,pe1pe2median):
    return f"""\n\nYou are protected by the following MINDEF-MHA voluntary group insurance plans:
              \n Death cover of  """+ "\${:,.2f}".format(ce1) +f""" with annual premium of \${pe1:,}.
             \n Critical illness cover of """+ "\${:,.2f}".format(ce2) +f""" with annual premium of \${pe2:,}.
             \n This annual premium of """ + "\${:,.2f}".format(p1bp2b) + f"""  is only {pe1pe2median:.2%} of the 
             median annual income of people in your age group.​"""
 

def getB1_B4():
   return """\n\nOur Singlife Relationship Consultants will be contacting you to help you optimize your protection portfolio and chart you path towards financial freedom.​
   \nShare your discovery and commitment to start your financial freedom by clicking here : \nhttps://facebook.com/  \n https://instagram.com/."""

def getB5_B6(g1b,p1b,ce2,pe2,p1bpe2,p1bpe2median):
   return f"""\n\nYou could consider the following covers as your foundation protection as recommended by the LIA financial planning guide*:​

Increase your death to \${g1b:,.2f} with annual premium of \${p1b::..2f}

Maintain your critical illness cover at ${ce2:,.2f} with annual premium of ${pe2:..2f}

This annual premium of """ + "\${:,.2f}".format(p1bpe2) + f""" is only """ + "${:,.2%}".format(p1bpe2median)  +""""  of the median annual income of people in your age group.​

Click on the following links to be protected today​

MINDEF : https://ebh.singlife.com/eb/mindef-mha/?MINDEF​

MHA : https://ebh.singlife.com/eb/mindef-mha/?groupName=MHA​

Our Singlife Relationship Consultants will be contacting you to help you close your protection gap and chart you path towards financial freedom.​

Share your discovery and commitment to start your financial freedom by clicking here \n https://facebook.com/  \n https://instagram.com/.​"""


def getB7_B8(ce1,pe1,g2b,p2b,pe1p2b,pe12bmedian):
   return f"""\n\nYou could consider the following covers as your foundation protection as recommended by the LIA financial planning guide*:​

Maintain your death cover to \${ce1:,} with annual premium of \${pe1:,}

Increase your critical illness cover at \${g2b:,} with annual premium of \${p2b:,}

This annual premium of """ + "${:,.2f}".format(pe1p2b) + f""" is only""" + "${:,.2%}".format(pe12bmedian)  +"""" of the median annual income of people in your age group.​

Click on the following links to be protected today​

MINDEF : https://ebh.singlife.com/eb/mindef-mha/?MINDEF​

MHA : https://ebh.singlife.com/eb/mindef-mha/?groupName=MHA​

Our Singlife Relationship Consultants will be contacting you to help you close your protection gap and chart you path towards financial freedom.​

Share your discovery and commitment to start your financial freedom by clicking here \n https://facebook.com/  \n https://instagram.com/."""

def getB9(g1b,p1b,g2b,p2b,p1np2b,p1bp2bmedain):
   return f"""\n\nYou could consider the following covers as your foundation protection as recommended by the LIA financial planning guide*:​

Increase your death to \${g1b:,} with annual premium of \${p1b:,}

Increase your critical illness cover at \${g2b:,} with annual premium of \${p2b:.2}

This annual premium of """ + "${:,.2f}".format(p1np2b) + f"""  is only """ + "${:,.2%}".format(p1bp2bmedain)  +"""" of the median annual income of people in your age group.​

Click on the following links to be protected today​

MINDEF : https://ebh.singlife.com/eb/mindef-mha/?MINDEF​

MHA : https://ebh.singlife.com/eb/mindef-mha/?groupName=MHA​

Our Singlife Relationship Consultants will be contacting you to help you close your protection gap and chart you path towards financial freedom.​

Share your discovery and commitment to start your financial freedom by clicking here \n https://facebook.com/  \n https://instagram.com/."""


def getCommonMSG_last():
   return """\n\n LIA financial planning guide recommends to have​
               \n Death cover of at least 9x annual income.​ \nCritical illness of at least 4x annual income.\n​To spend no more than 15% of annual income on premium for insurance protection.
               \n https://www.mas.gov.sg/news/media-releases/2023/mas-and-financial-industry-launch-basic-financial-planning-guide \n\n"""


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

def format_currency_in_string(s):
    # Find all occurrences of monetary values in the string
    matches = re.findall(r'\$\d+', s)
 
    for match in matches:
        # Remove the dollar sign and convert to an integer
        num = int(match[1:])
 
        # Format the number with commas and two decimal places
        formatted_num = f'${num:,.2f}'
 
        # Replace the original number with the formatted number in the string
        s = s.replace(match, formatted_num)
 
    return s
 