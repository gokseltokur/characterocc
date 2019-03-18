# -*- coding: utf-8 -*-
import re
import locale

#Turkish Characters
locale.setlocale(locale.LC_ALL, 'tr_TR.utf8')

#Function to count ascii characters in given range
def asciirange(minascii, maxascii, str):
    for i in range(minascii, maxascii):
        ch = chr(i)
        #print(ch)
        cnt = len(re.findall( ch, str))
        if cnt > 3:
            print('Letter (%s)\'s occurrance is: %d'%(chr(i), cnt))

#Function to count special Turkish characters
def trcharacters(str):
    alpha = ['Ç', 'ç', 'Ğ', 'ğ', 'ı', 'İ', 'Ö', 'ö', 'Ş', 'ş', 'Ü', 'ü']
    for i in range(len(alpha)):
        ch = alpha[i]
        cnt = len(re.findall(ch, str))
        if cnt > 3:
            print('Letter (%s)\'s occurrance is: %d'%(ch, cnt))


str = "sdfsdfjaosfıdjasof asdfasdfasdfasdf sadfasd poınsadf dsfişlcxvş ömnewer dkjnfasdofıjeoıasdöcmçxc vzdfgladkfjg"
asciirange(48, 58, str) #numbers
asciirange(65, 91, str) #uppercase letters
asciirange(97, 123, str)#lowercase letters
trcharacters(str)
