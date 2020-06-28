# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 17:15:01 2020

@author: Benny
"""

import proj03library


def main():
    test1 = 'Hello'
    test2 = 'H3ll0 W0r1d'
    test3 = '12345'
    #is_alpha
    print('is_alpha')
    print(test1 + '\nResult: ' + str(proj03library.is_alpha(test1)))
    print(test2 + '\nResult: ' + str(proj03library.is_alpha(test2)))
    print(test3 + '\nResult: ' + str(proj03library.is_alpha(test3)))
    print('\n')
    
    #is_digit
    print('is_digit')
    print(test1 + '\nResult: ' + str(proj03library.is_digit(test1)))
    print(test2 + '\nResult: ' + str(proj03library.is_digit(test2)))
    print(test3 + '\nResult: ' + str(proj03library.is_digit(test3)))
    print('\n')
    
    #to_lower
    print('to_lower')
    print(test1 + '\nResult: ' + str(proj03library.to_lower(test1)))
    print(test2 + '\nResult: ' + str(proj03library.to_lower(test2)))
    print(test3 + '\nResult: ' + str(proj03library.to_lower(test3)))
    print('\n')
    
    #to_upper
    print('to_upper')
    print(test1 + '\nResult: ' + str(proj03library.to_upper(test1)))
    print(test2 + '\nResult: ' + str(proj03library.to_upper(test2)))
    print(test3 + '\nResult: ' + str(proj03library.to_upper(test3)))
    print('\n')
    
    #find_chr
    print('find_chr')
    print("The index of o in " + test1 + ' ' 'is: ' + str(proj03library.find_chr(test1, 'o')))
    print('The index of 1 in' + test2 + ' ' 'is: ' + str(proj03library.find_chr(test2, '1')))
    print('\n')
    
    #find_str
    print('find_str')
    print('the lowest index where llo is found in ' + test1 + ' ' 'is: ' +str(proj03library.find_str(test1, 'llo')))
    print('the lowest index where W0r1 is found in ' + test2 + ' ' 'is: '+str(proj03library.find_str(test2, 'W0r1')))
    print('\n')

    #replace_chr
    print('replace_chr')
    print("Replace 'l' with 'h' in " + test1 + "\n Result: " + str(proj03library.replace_chr(test1, 'l', 'h')))
    print("Replace '0' with 'z' in " + test2 + "\n Result: " + str(proj03library.replace_chr(test2, '0', 'z')))
    print('\n')
    
    #replace_str
    print('replace_str')
    print("Replace 'll' with 'Benny' in " + test1 + "\n Result: " + str(proj03library.replace_str(test1, 'll', 'Benny')))
    print("Replace 'H3llo' with 'G00d M0rning' in " + test2 + "\n Result: " + str(proj03library.replace_str(test2, 'H3ll0', 'G00d M0rning')))
    

#Run    
if __name__ == "__main__":
    main()