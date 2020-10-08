import replit
replit.clear()

#------------
# LISTS
#------------

arabic_roman_map = [(1000, 'M'), (900, 'DCCCC'), (500, 'D'), (400, 'CCCC'), (100, 'C'), (90, 'LXXXX'),
           (50, 'L'), (40, 'XXXX'), (10, 'X'), (9, 'VIIII'), (5, 'V'), (4, 'IIII'), (1, 'I')]

my_dict = {'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000}

invalid_map = [('IIIII'), ('VV'), ('XXXXX'), ('LL'), ('CCCCC'), ('DD')]

#------------
# FUNCTIONS
#------------

# This will convert from Roman Numerals to Arabic
def roman_arabic_convert(romannum):
  romannum = romannum.upper()
  total = 0

  for i in romannum:
    total += my_dict[i]
  
  return total


# This will convert from Arabic to Roman Numerals
def arabic_roman_convert(arabicnum):

    roman = ''

    while arabicnum > 0:
        for i, a in arabic_roman_map:
            while arabicnum >= i:
                roman += a
                arabicnum -= i

    return roman

# This will validate numbers greater than 4000
def validateArabic(arabicnum):
 
 if arabicnum > 4000:
    raise ValueError('Values above MMMM (4000) are not permitted')

    
# This will validate Roman numerals
def validateRoman(romannum):
  romannum = romannum.upper()
  x = 1
  y = 0 
  z = 0
  
  if romannum== "":
    raise ValueError('You have not entered a Numeral')
  else:
    for item in romannum:
      if item in my_dict:
        if x > 1: 
          z = y
        y = my_dict[item] 
        if y != 0 and z != 0:
          if z < y:  
            raise ValueError('Invalid Roman Numeral entered: letters must be in descending order of value')
        x += 1  
      else:
        raise ValueError('Invalid Roman Numeral entered')
      for itemX in invalid_map:
        if itemX in romannum:
          raise ValueError('Invalid Roman Numeral entered: numeral can be replaced by a letter')

#------------
# MAIN PROGRAM
#------------

print('Welcome to the Roman Numerals calculator. To use this tool, please follow the instructions below.\n')

#to convert the first Roman Numeral into Arabic

roman1 = input('Please enter the first Roman Numeral:\n')
validateRoman(roman1) #to validate the first Roman Numeral
arabic1 = float(roman_arabic_convert(roman1))
validateArabic(arabic1) #to validate the first Arabic Numeral

#to convert the second Roman Numeral into Arabic

roman2 = input('Please enter the second Roman Numeral:\n')
validateRoman(roman2) #to validate the second Roman Numeral
arabic2 = float(roman_arabic_convert(roman2))
validateArabic(arabic2) #to validate the second Arabic Numeral


operateSign = input('Please enter an operator (+ or -):\n') #prompts user to give an operator

print('The Arabic value of', roman1.upper(), 'is', int(arabic1))
print()
print('The Arabic value of', roman2.upper(), 'is', int(arabic2))
print()

#selection: to check whether operator is valid and whether it's plus or minus
if operateSign == '+':
  arabicTotal = arabic1 + arabic2

elif operateSign == '-':
  arabicTotal = arabic1 - arabic2
  if arabicTotal == 0:
    raise ValueError('Zero results are not permitted')
  elif arabicTotal < 0:
    raise ValueError('Negative results are not permitted')
elif operateSign == '':
  raise ValueError('You have not entered an operator')
else:
  raise ValueError('Invalid operator entered')

print()
print(int(arabic1), operateSign, int(arabic2), 'equals', int(arabicTotal))
print(roman1.upper(), operateSign, roman2.upper(), 'equals', arabic_roman_convert(arabicTotal))
print()
print('The Arabic total is', int(arabicTotal))
print('The Roman Numeral total is', arabic_roman_convert(arabicTotal))
print()

#to give user choice to clear display (only works on repl.it)
cleardisplay= input('Do you want to clear the display? (Yes/No)')
cleardisplay1 = cleardisplay.capitalize()
if cleardisplay1 == 'Yes':
  replit.clear()