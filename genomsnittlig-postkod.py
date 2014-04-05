#!/usr/bin/env python
'''
    Written by Tim Lind
    @ http://www.timlind.net
    May be distributed and used freely.
    Just let this referene be here as proof,
    of your awesome heart.
'''

def f1_make_list(string):
    '''
        1. Create a list of all the post codes
    '''
    return string.split(", ")
    


def f2_get_total(the_list):
    '''
        2. Handle the syntax "XXX XX" then add them all to a total count
    '''
    total = 0
    for code in the_list:
        x1,x2 = code.split(" ")
        code = x1+x2
        total += int(code)
    return int(total)

def f3_get_avarage(total,count):
    '''   3. Calculate avarage '''
    return str(int(round(total/count)))

def f4_change_syntax(code):
    '''
        4. Change the syntax back to "XXX XX" and return the avarage postcode
    '''
    counter = 0
    changed_code = ""
    for x in list(str(code)):
        if counter == 3:
            changed_code += " "
        changed_code += x
        counter+=1
    return changed_code

def run(postcodes):
    the_list = f1_make_list(postcodes)
    total = f2_get_total(the_list)
    avarage = f3_get_avarage(total,len(the_list))
    code = f4_change_syntax(avarage)
    return code


# 1. Save all post codes to the variable postcodes, seperate with comma, syntax: "XXX XX, XXX XX"
postcodes = "901 19, 901 30, 901 31, 901 32, 901 33, 901 37, 901 70, 901 73, 901 74, 901 75, 901 76, 901 77, 901 78, 903 20, 903 21, 903 22, 903 23, 903 25, 903 26, 903 27, 903 28, 903 29, 903 30, 903 31, 903 32, 903 33, 903 34, 903 36, 903 37, 903 38, 903 39, 903 40, 903 42, 903 43, 903 44, 903 45, 903 46, 903 47, 903 51, 903 52, 903 53, 903 54, 903 55, 903 60, 903 61, 903 62, 903 63, 903 64, 903 65, 904 20, 904 21, 904 22, 904 26, 904 31, 904 32, 904 33, 904 34, 904 35, 904 36, 905 80, 905 81, 905 82, 905 83, 905 86, 905 87, 905 88, 905 91, 905 92, 905 93, 905 94, 905 95, 905 96, 906 20, 906 21, 906 22, 906 24, 906 25, 906 26, 906 27, 906 28, 906 29, 906 37, 906 38, 906 40, 906 41, 906 42, 906 43, 906 50, 906 51, 906 52, 906 53, 906 54, 906 55, 906 60, 907 28, 907 29, 907 30, 907 31, 907 32, 907 33, 907 34, 907 35, 907 36, 907 37, 907 38, 907 39, 907 40, 907 41, 907 42, 907 43, 907 46, 907 49, 907 50, 907 51, 907 52, 907 53"
avarage_postcode = run(postcodes)
print(avarage_postcode)
