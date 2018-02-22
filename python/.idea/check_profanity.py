import urllib
def read_text():
    #captures the text file in quotes
    quotes = open("C:\Users\Nicolas Guinand\OneDrive\FSNanodegree\python\Check.txt")
    #variable that collects the quotes
    contents = quotes.read()
    # print(contents)
    # print(type(quotes))
    quotes.close()
    check_profanity(contents)

def check_profanity(text_to_check):
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q=" + text_to_check)
    output = connection.read()
    #output is a string not a boolean..
    print(output)
    connection.close()
    if(output == "true" ):
        print("Profanity Alert!!")
    elif(output == "false"):
        print("This document has no curse words!")
    else:
        print("Could not scan the document properly.")

read_text()