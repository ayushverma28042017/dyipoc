from utility import *   
from fpdf import FPDF


def check(email):
 regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    # pass the regular expression
    # and the string into the fullmatch() method
 if(re.fullmatch(regex, email)):
    print("Valid Email")
    quit()
 else:
    print("Invalid Email")
    quit()


def validation(nric):
 if validate_nric(nric)== False:
  st.write(" NRIC is not valid ")
  return False
 else :
     return True
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
     print('nric is valid!\n')
     quit()
    else:
     print('nric is invalid!\n')
     quit()

def validation(name):
    for char in name:
        if  not (("A" <= char and char <= "Z") or ("a" <= char and char <= "z") or (char == " ")):
            return False
    return True

def create_download_link(val, filename):
                 b64 = base64.b64encode(val)  # val looks like b'...'
                 return f'<a href="data:application/octet-stream;base64,{b64.decode()}" download="{filename}.pdf">Download file</a>'
def new_customer_workflow(nric,name):
     
    birthyr  = nric[1:3]
    current_year = 2024

    age = current_year-(int(birthyr)+1900) 
    firstChar = nric[0:1]
    # st.write("Age is :: ",age)


    if((firstChar == 'S' or firstChar == 'T') and (18 <age <40)):
   

      median_sal=median_sal= getMdianSalary_by_AgeRange(int(age))

    # Constraint 1 
      c1= 9 * median_sal 
      c2= 4 * median_sal 
     # Constraint 2
      G1 =  min(c1,1000000)
      G2=  min(c2,500000)


     #calculate permium pay base on above
      P1= premium_tlsaf(age) *12
      P2= premium_lcsaf(age) *12
      P3=(median_sal *15)/100
      median_sal = 12 * median_sal

      if(P1+P2<=P3):
        # st.write(getA1Message(median_sal,G1,G2,P1,P2))
        col1, col2 = st.columns(2)
        col1.image('no_cover_1.png', use_column_width=True)
        col2.write(getMessageC(median_sal,G1,G2,P1,P2))
        export_as_pdf = st.button("Share")
      else:
        #  st.write(getA1Message(median_sal,G1,G2,P1,P2))
         col1, col2 = st.columns(2)
         col1.image('no_cover_1.png', use_column_width=True)
         col2.write(getMessageC(median_sal,G1,G2,P1,P2))
         export_as_pdf = st.button("Share")
    else:
            #  st.image('no_cover.png', width=400)
            #  st.write(getMessageC())
             
            #  st.subheader(f"""Hello {name}""")
             col1, col2 = st.columns(2)
             col1.image('no_cover_1.png', use_column_width=True)
             col2.write(getMessageC(name))
             export_as_pdf = st.button("Share")
            
# def getA1Message(median_sal,G1,G2,P1,P2):
#      return f"""The median annual income of people in your age group is \${median_sal}
#                 \nAt Singlife, we protect those who have served to protect Singapore.​
#                 \nYou could consider the following covers as your foundation protection as recommended by the LIA financial planning guide:​
#                    a)Death cover of \${G1:,} with annual premium of \${P1:.}​
#                    b)Critical illness cover of \${G2:,} with annual premium of \${P2:.}
#                    c)This annual premium of \${(P1+P2):,} is only {((P1+P2)/median_sal):.%}  of the median annual income of people in your age group.​

#                Click on the following links to be protected today​
#                 MINDEF : https://ebh.singlife.com/eb/mindef-mha/?MINDEF​
#                 MHA : https://ebh.singlife.com/eb/mindef-mha/?groupName=MHA​

#             Our Singlife Relationship Consultants will be contacting you to help you chart you path towards financial freedom.​
#             Share your discovery and commitment to start your financial freedom by clicking here :
#               \n https://facebook.com/ 
#              \n https://instagram.com/

#             LIA financial planning guide recommends to have​
#               \n1.Death cover of at least 9x annual income.​
#               \n2.Critical illness of at least 4x annual income.​
#               \n3.To spend no more than 15% of annual income on premium for insurance protection.​
#             https://www.mas.gov.sg/news/media-releases/2023/mas-and-financial-industry-launch-basic-financial-planning-guide ​"""


def getMessageC(name):
   return f""" Hello {name} \n\n Our SRC can help you with a comprehensive financial review.​
    \nOur Singlife Relationship Consultants will be contacting you to help you chart you path towards financial freedom."""