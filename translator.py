
#-*-coding: UTF-8 -*-
# XML translator version 0.1

from __future__ import print_function

from googletrans import Translator
import xml.etree.ElementTree as ET  
import sys

fileName=""
NoneType = type(None)

def getTree():
	global fileName
	fileName= raw_input("Insert the name of XML file or the file path: \n")
	return ET.parse(fileName, parser=ET.XMLParser(encoding='utf-8'));

	
def main():
	translator = Translator()
	tree = getTree()
	root = tree.getroot()

	language = getLanguage()

	for elem in root:
		elem.text = translator.translate(elem.text, dest=language).text
		for subelem in elem.iter():
			if type(subelem.text) != NoneType:
				print(subelem.text)
				subelem.text = translator.translate(subelem.text, dest=language).text
			else:
				print("Can not be translated")
	tree.write(fileName[0:len(fileName)-4]+"_XMLtranslated_"+language+".xml", encoding="UTF-8")


def getLanguage():
    showOptions()
    try:
        languageIndex = int (raw_input('Select language number (1...5)\n'))
        if(languageIndex < 1 or languageIndex >5):
            sys.exit()
        else:
            selectedLanguage = menu(languageIndex)
            return selectedLanguage
    except:
        print('Invalid option')
        print('Closing program...')
        sys.exit()
        
def menu(arg):
    switcher = {
            1: "es",
            2: "fr",
            3: "it",
            4: "en",
            5: "ru"
    }
    return switcher.get(arg, "No valid option, closing program...")

def showOptions():
    print('---------Select the language to translate--------')
    print('\t1...Spanish')
    print('\t2...French')
    print('\t3...Italian')
    print('\t4...English')
    print('\t5...Russian')



if __name__ == '__main__':
    main()
