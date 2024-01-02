

import re

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