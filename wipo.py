from requests_html import HTMLSession
import datetime
session = HTMLSession()
headers = {"User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36 OPR/67.0.3575.137"}
status_url= f'https://patentscope.wipo.int/search/en/detail.jsf?docId=WO2020190855&_cid=P11-KQ6CCK-39257-2'
status_url2= f'https://patentscope.wipo.int/search/en/detail.jsf?docId=WO2020190855&_cid=P11-KQ6CCK-39257-2#detailMainForm:MyTabViewId:PCTDOCUMENTS'
html = session.get(status_url,timeout=(3.05, 27))
#WO2020191111
print(html.text)
html = html.html

file = open("sample.html","w")
file.write(str(html))
file.close()



publicationNumber = ''
publicationDate=''
Title=''
international_app=''
International_Filing=''
Applicants=''
Inventors=''
Agents=''
Priority_Data=''
     
elements = html.find('div.ps-field.ps-biblio-field')
counter=0
for element in elements:
    temp = element.text
    counter=counter+1
    #print(counter)
    #print(temp)
    if "Publication Number" in temp:
        temp = temp.split()
        temp.reverse()
        publicationNumber = temp[0]

    if "Publication Date" in temp:
        temp = temp.split()
        temp.reverse()
        publicationDate = temp[0]

    if "Title" in temp:
        #print("this is title")
        #print(element)
        titleval=element.find('.needTranslation-biblio')
        for c in titleval:
            Title= c.text

    if "International Application No." in temp:
        temp = temp.split()
        temp.reverse()
        international_app = temp[0]

    if "International Filing Date" in temp:
        temp = temp.split()
        temp.reverse()
        International_Filing = temp[0]

    if "Applicants" in temp:
        #print(temp)
        Applicants = temp
        Applicants=Applicants.replace("Applicants","")
        Applicants=Applicants.strip()

    if "Inventors" in temp:
        #print(temp)
        Inventors = temp
        Inventors=Inventors.replace("Inventors","")
        Inventors=Inventors.strip()

    if "Agents" in temp:
        #print(temp)
        Agents = temp
        Agents=Agents.replace("Agents","")
        Agents=Agents.strip()

    if "Priority Data" in temp:
        #print(temp)
        date = element.find('tr',first=True)
        Priority_Data=(date.text)
        #Priority_Data = temp
        #Priority_Data=Priority_Data.replace("Priority Data","")
        #Priority_Data=Priority_Data.strip()
        #Priority_Data=Priority_Data.split(" ")
        #Priority_Data=Priority_Data[0]
            

print("publication number is")
print(publicationNumber)
print("publication date is")
print(publicationDate)
print("title is")
print(Title)
print("this is internation application no")
print(international_app)
print("international filing date is")
print(International_Filing)
print("Applicants name is")
print(Applicants)
print("this is inventors")
print(Inventors)
print("Agents name is")
print(Agents)
print("Prioriy data is")
print(Priority_Data)

#extracting data for pdf
html = session.get(status_url2)
#WO2020191111
html = html.html
print("This is pdf link .page33333333333333333333333333333333333333333333333333333333333333")
#print(html.html)
print(html.html)
