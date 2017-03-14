import random
import string

def main():
    lol = True
    while(lol):
        choice = raw_input('To or from?: ')
        if choice.lower() == 'to' or choice == '1':
            toEng()
        elif choice.lower() == 'from' or choice == '2':
            fromEng()
        elif choice.lower() == 'exit' or choice == '3':
            lol = False
        else:
            print 'Please enter an accepted choice!'

def fromEng():
    str = raw_input('Please type the sentence you wish to translate: ')
    newStr = ''
    o = 0
    for i in range(len(str) * 2):
        if i % 2 == 0:
            newStr += str[o]
            o += 1
        else:
            #make random at home
            newStr += random.choice(string.ascii_lowercase)
    print newStr

def toEng():
    str = raw_input('Please type the sentence you wish to translate: ')
    newStr = ''
    for i in xrange(0,len(str),2):
        newStr += str[i]
    print newStr

main()

