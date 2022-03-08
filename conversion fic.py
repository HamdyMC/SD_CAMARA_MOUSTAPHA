
import csv
import yaml
import json
import xmltodict
from dicttoxml import dicttoxml 

#nomfichier="en_j.json"
#ext=nomfichier.split(".")
tf={1:"json",2:"yaml",3:"xml",4:"csv"}

#dertermination extension
def detext(nomfic):
    ext=nomfic.split(".")
    ext=ext[-1]
    return ext


#csv to dictionnary to csv

def csvtodic(nomfic):
    dicr = csv.DictReader(open(nomfic, 'r'))
    dic=[]
    for row in dicr:
        dic.append(row)
    ordered_dict_from_csv = list(dic)[0]
    dic= dict(ordered_dict_from_csv)
    return dic

def dictocsv(dic):
    keys= dic[0].keys()
    f = open("en_c.csv", "w")
    cfile = csv.DictWriter(f, keys)
    cfile.writeheader()
    cfile.writerows(dic)
    return cfile

#Yaml to dictionnary to yaml

def yamltodic(nomfic):
    
    with open(nomfic) as file:
        dic= yaml.load(file, Loader=yaml.FullLoader)
    return dic

def dictoyaml(dic):
    with open('en_y.yaml', 'w') as file:
        yfile = yaml.dump(dic, file)
    return yfile


# json to dictionnary to json

def jsontodic(nomfic):
    with open(nomfic,'r') as f:
        data = json.load(f)
    dic=data
    return dic
def dictojson(dic):
    f=open('en_j.json','w')
    jfile = json.dump(dic,f)
    return jfile
# xml to dictionnary to xml

def xmltodic(nomfic):
    with open(nomfic, 'r') as file:
        my_xml = file.read()
    dic = xmltodict.parse(my_xml)
    return dic
def dictoxml(dic):    
    
    with open('en_x.xml','w', encoding="utf-8") as file:
        x = dicttoxml(dic)
        xfile=file.write(str(x))
    return xfile



def dftochoice(nomfic):
    ext=detext(nomfic)
    if ext=="csv":
        dic=csvtodic(nomfic)
        return dic
    elif ext=="json":
        dic=jsontodic(nomfic)
        return dic
    elif ext=="yaml":
        dic=yamltodic(nomfic)
        return dic
    elif ext=="xml":
        dic=xmltodic(nomfic)
        return dic
    else:
        print("Format inconnue")
        return 0

        
def saisie():
    nomfichier=input('Saisir le nom du fichier avec lextention et le chemin')
    ext=detext(nomfichier)
    dftochoice(nomfichier)
    if ext=="xml" or ext=="yaml" or ext=="json" or ext=="csv":
        return nomfichier
    else:
        pri
    


ext=detext(nomfichier)
#choix=dftochoice(nomfichier)
if ext=="csv":
    choix=4
elif ext=="json":
    choix=1
elif ext=="yaml":
    choix=2
elif ext=="xml":
    choix=3
del tf[choix]

print(tf)

c="retry"
#c=int(input())
while c=="retry":
    print("le fichier choisi est de type <<",ext,">>. Faites votre choix de conversion:")
    #c=3
    c=int(input())
    if c==1:
        dic=dftochoice(nomfichier)
        jfile=dictojson(dic)
    elif c==2:
        dic=dftochoice(nomfichier)
        yfile=dictoyaml(dic)
    elif c==3:
        dic=dftochoice(nomfichier)
        xfile=dictoxml(dic)
    elif c==4:
        dic=dftochoice(nomfichier)
        cfile=dictocsv(dic)
    else:
        print("choix indisponible")
        c="retry"
