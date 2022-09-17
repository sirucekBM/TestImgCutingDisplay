import json
import os.path
import traceback
import pathlib
'''
Modul slouží ke čtení,zápisu a append různých formátů souborů
kodovani vsech souboru je UTF8
 
'''
 
#-----------------READ----------------------------------
def readJsonConfigFile():
    try:
        filePath = os.path.join(os.path.dirname(__file__), 'config.json')
        with open(filePath ,'r',encoding='utf8') as f:
            dataJson = json.load(f)
        return dataJson
    except Exception:
        return str(traceback.format_exc())
 
def readJsonFile(filePath):
    try:
        with open(filePath ,'r',encoding='utf8') as f:
            dataJson = json.load(f)
        return dataJson
    except Exception:
        return str(traceback.format_exc())
 
def readTextFile(filePath):
    try:
        with open(filePath,'r', encoding="utf-8") as f:
            dataFile  = f.read().splitlines()
        return dataFile
    except Exception:
        return str(traceback.format_exc())
 
#------------------CREATE-------------------------------
def createJsonFile(filePath, dictData):
    try:
        with open(filePath,"w", encoding='utf-8') as jsonfile:
            jsonfile.write(json.dumps(dictData,indent=4))
        return True
    except Exception:
        return str(traceback.format_exc())
 
def createTxtFile(filePath,textData):
    try:
        with open(filePath, 'w',encoding='utf-8') as fp:
            fp.write('\n'.join(textData))
        return True
    except Exception:
        return str(traceback.format_exc())
 
#--------------APPEND--------------------------
#----------metoda přidá na konec souboru předaný text
def appendTxtFile(filePath,textData):
    try:
        with open(filePath, "a",encoding='utf-8') as fp:
            fp.write(textData + '\n' )
    except Exception:
        return str(traceback.format_exc())
 
#-------------MERGE------------------------------
 
#----metode se preda list se seznamem souboru formatu json a metoda je spoji do jednoho
def mergeFilesDicts(listFilesDict):
    try:
        dictMergedDicts ={}
        dataJson ={}
        for fi in listFilesDict:
            dataJson = readJsonFile(fi)
            dictMergedDicts.update(dataJson)
        return dictMergedDicts
    except Exception:
        print(str(traceback.format_exc()))
        return str(traceback.format_exc())
def mergeTextFile(fileList,outFileName,zdrojFolder):
    with open(outFileName, 'w',encoding='utf-8') as outfile:
        for fname in fileList:
            xFile = zdrojFolder +"\\" +fname
            with open(xFile , encoding="utf-8") as infile:
                for line in infile:
                    outfile.write(line)
 
#---VRATI LIST SE SOUBORY V ZADANÉ SLOZCE
def getAllFilesFromFolder(strFolder):
    try:
        listFile=[]
        for path in os.listdir(strFolder):
            # check if current path is a file
            if os.path.isfile(os.path.join(strFolder, path)):
                listFile.append(path)
        return listFile
    except Exception:
        return str(traceback.format_exc())  
 
#---VRATI LIST SE SOUBORY URCITEHO TYPU V ZADANÉM LISTU
def getAllSelectTypeFilesFromFolder(listFiles,pathFile,typFile):
    try:
        listFile=[]
        for fi in listFiles:
            fileTyp = pathlib.Path(fi).suffix
            if(fileTyp == typFile):
                fileDataJson = pathFile + fi
                listFile.append(fileDataJson)
        return listFile
    except Exception:
        return str(traceback.format_exc()) 