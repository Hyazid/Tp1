import webbrowser
import csv
filename = 'hello world.html'
webbrowser.open_new_tab(filename)
def listToString(s):  
    
    # initialize an empty string 
    str1 = ""  
    
    # traverse in the string   
    for ele in s:  
        str1 += ele   
    
    # return string   
    return str1  
  
###################################################
mesageHTML =""" 
<!DOCTYPE html>
<html>
<head>
    <meta charset='utf-8'>
    <meta http-equiv='X-UA-Compatible' content='IE=edge'>
    <title>Page Title</title>
    
    
    
    
</head>
<body>
</br></br>


    
</body>
</html>
"""
nameListe =[]
S1= []
S2= []
credit=[]
csvFile= open('C:\\Users\\Mon pc\\Desktop\\cours\\javascript\\test1.csv', 'r',)
htmlFile =open("hello world.html","w")
csvReader = csv.reader(csvFile)
next(csvReader)
for element in csvReader:
    nameListe.append(element[0])
    S1.append(element[1])
    S2.append(element[2])
    credit.append(element[3])
htmlFile.write(mesageHTML)
print("s1",S1)
print("s2",S2)
######################################
#calculer moyenne
moyenne = []
cptFS2=0
if len(S1)==len(S2):
    for s in S1:
        calcul=(float(s)+float(S2[cptFS2]))
        print(calcul,"",s,"",S2[cptFS2],"")
        calcul1=calcul/2
        print(calcul1)
        moyenne.append(str(calcul1))
        cptFS2=cptFS2+1
print(moyenne)





print(len(S1))



cpt=0
for names in nameListe:
    
    if cpt < 4:
        if float(credit[cpt]) <45 and float(moyenne[cpt])>=10:
            htmlFile.write("""<table width=55% border="4"><tr><td width=20%>"""+names+"""</td><td width=20%>"""+S1[cpt]+
            """</td><td width=20%>"""+S2[cpt]+"""  </td><td width=20%>admis avec dettes</td><td width=20%>"""+credit[cpt]+"""</td><td width=20%>"""+moyenne[cpt]+"""</td></tr> </table>""")
        
        elif float(credit[cpt]) <45 and float(moyenne[cpt])<10:
            htmlFile.write("""<table width=55% border="4"><tr><td width=20%>"""+names+"""</td><td width=20%>"""+S1[cpt]+
            """</td><td width=20%>"""+S2[cpt]+"""  </td><td width=20%>ajurner</td><td width=20%>"""+credit[cpt]+"""</td><td width=20%>"""+moyenne[cpt]+"""</td></tr> </table>""")
        

        else:
             htmlFile.write("""<table width=55% border="4"><tr><td width = 20%>"""+names+"""</td><td width=20%>"""+S1[cpt]+
            """</td><td width=20%>"""+S2[cpt]+"""  </td><td width=20%>admis</td><td width=20%>"""+credit[cpt]+"""</td><td width=20%>"""+moyenne[cpt]+"""</td></tr> </table>""")
            
    
    cpt =cpt+1
    print(cpt)



str1 = listToString(nameListe)
#for note in S1:
#    htmlFile.write("""<table width=60% border="1"><tr width =60% border="1"><td>"""+S1[1]+"""</td></tr></table> """)

print(str1)















htmlFile.close()