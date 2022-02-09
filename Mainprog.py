from errno import EALREADY
from tkinter import *
from tkinter.font import BOLD
from tkinter.ttk import *
import time
from tkinter.messagebox import askyesno
import csv
from requests_html import HTMLSession
import datetime
import json
import threading
session = HTMLSession()
import _thread

trnumbers=[]

def prebar():
    import os.path
    file_exists = os.path.exists('Input.csv')
    print(file_exists)
    if file_exists==True:
        _thread.start_new_thread(bar,())
    else:
        progresslabel.config(text="Input.csv file not found",foreground='red')


def bar():
    btn.config(state="disabled")
    with open('Output.csv', 'a', newline='') as csvfile:
        fieldnames = ['trno','Literal Element',"Mark Type","Serial","TSDR","International Class(es)",
        "Filing Date","Publication Date","Correspondent Name/Address","Correspondent Organization","Correspondent Phone Number",
        "Legal Entity Type / Is Corporate Filer","TM5 Common Status / Alt Legal Status",
        "Status Date","Date_Abandoned","Mail Date","Latest Document Description","Summary of issues in latest office action","Date of latest office action","E-Mail 1","E-Mail 2","E-Mail 3",
        "E-Mail 4","E-Mail 5"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        with open('Input.csv') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                irnis = row['Serial-number']
                trnumbers.append(irnis)
            print("this is total no of patent in the sheet")
            print(len(trnumbers))
            tasks=len(trnumbers)
            x=0
            y=0
            # while (x==tasks):
            trno="NA"
            Mark = "NA"
            serialno = "NA"
            Filing_Date = "NA"
            Mark_Type = "NA"
            TM5_Descriptor = "NA"
            Status_Date = "NA"
            Publication_Date = "NA"
            Date_Abandoned = "NA"
            International_Class = "NA"
            Owner_Name = "NA"
            Correspondent_Name_Address = "NA"
            Legal_Entity_Type = "NA"
            Phone = "NA"
            Correspondent_e_mail = "NA"
            Document_Date = "NA"
            Document_Title = "NA"
            Offc_Action_Date = "NA"
            SUMMARY_OF_ISSUES = "NA"
            linkval = "NA"
            email1="NA"
            email2="NA"
            email3="NA"
            email4="NA"
            email5="NA"
            for c in trnumbers:
                print("Extracting data for")
                print(c)
                progresslabel.config(text="Fetching data from TSDR.......")
                trademarknolabel1.config(text="Extracting data for "+str(c))
                statuslabel.config(text=(str(x+1)+ " / " +str(tasks)))
                progress['value'] +=((x/tasks)*100)
                root.update_idletasks()
                lb.config(text=str(int((x/tasks)*100))+"%")
                # progtrack['value'] =100
                progtrack['value'] =(x/tasks)*100
                time.sleep(2)
                x+=1
                time.sleep(2)
                root.update_idletasks()
                linkval = "https://tsdr.uspto.gov/#caseNumber=" + str(c) + "&caseSearchType=US_APPLICATION&caseType=DEFAULT&searchType=statusSearch"
                headers = {"User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36 OPR/67.0.3575.137"}
                status_url= f'https://uspto-2021.herokuapp.com/fetch/'+c
                html = session.get(status_url)
                time.sleep(3)
                html = html.html
                print(html.text)
                if "Internal Server Error" not in html.text:    ##Add else conditio when "NA"

                    y = json.loads(html.text) 

                    Mark = (y["Mark"])
                    if Mark=="":
                        Mark="NA"

                    serialno = (y["US Serial Number"])
                    if serialno=="":
                        serialno="NA"

                    Filing_Date = (y["Application Filing Date"])
                    if Filing_Date=="":
                        Filing_Date="NA"

                    Mark_Type = (y["Mark Type"])
                    if Mark_Type=="":
                        Mark_Type="NA"

                    TM5_Descriptor = (y["TM5 Common Status Descriptor"])
                    if TM5_Descriptor=="":
                        TM5_Descriptor="NA"

                    Status_Date = (y["Status Date"])
                    if Status_Date=="":
                        Status_Date="NA"

                    Publication_Date = (y["Publication Date"])
                    if Publication_Date=="":
                        Publication_Date="NA"

                    Date_Abandoned = (y["Date Abandoned"])
                    if Date_Abandoned=="":
                        Date_Abandoned="NA"

                    International_Class = (y["International Class(es)"])
                    if International_Class=="":
                        International_Class="NA"

                    Owner_Name  = (y["Owner Name"])
                    if Owner_Name=="":
                        Owner_Name="NA"

                    Correspondent_Name_Address  = (y["Correspondent Name/Address"])
                    if Correspondent_Name_Address=="":
                        Correspondent_Name_Address="NA"

                    Legal_Entity_Type  = (y["Legal Entity Type"])
                    if Legal_Entity_Type=="":
                        Legal_Entity_Type="NA"

                    Phone  = (y["Phone No"])
                    if Phone=="":
                        Phone="NA"

                    Correspondent_e_mail  = (y["Email"])
                    if Correspondent_e_mail=="":
                        Correspondent_e_mail="NA"

                    Document_Date  = (y["Document Date"])
                    if Document_Date=="":
                        Document_Date="NA"

                    Document_Title  = (y["Document Title"])
                    if Document_Title=="":
                        Document_Title="NA"

                    Offc_Action_Date  = (y["Office Action Date "])
                    if Offc_Action_Date=="":
                        Offc_Action_Date="NA"

                    SUMMARY_OF_ISSUES  = (y["SUMMARY OF ISSUES"])
                    if SUMMARY_OF_ISSUES=="":
                        SUMMARY_OF_ISSUES="NA"
                        
                    if serialno == "NA":
                        linkval == "NA"
                else:
                    Mark = "NA"
                    serialno = "NA"
                    Filing_Date = "NA"
                    Mark_Type = "NA"
                    TM5_Descriptor = "NA"
                    Status_Date = "NA"
                    Publication_Date = "NA"
                    Date_Abandoned = "NA"
                    International_Class = "NA"
                    Owner_Name = "NA"
                    Correspondent_Name_Address = "NA"
                    Legal_Entity_Type = "NA"
                    Phone = "NA"
                    Correspondent_e_mail = "NA"
                    Document_Date = "NA"
                    Document_Title = "NA"
                    Offc_Action_Date = "NA"
                    SUMMARY_OF_ISSUES = "NA"
                    linkval = "NA"
                    email1="NA"
                    email2="NA"
                    email3="NA"
                    email4="NA"
                    email5="NA"
                            
                trno=trno.encode('ascii', 'ignore').decode('ascii')
                Mark=Mark.encode('ascii', 'ignore').decode('ascii')
                Mark_Type=Mark_Type.encode('ascii', 'ignore').decode('ascii')
                serialno =serialno.encode('ascii', 'ignore').decode('ascii')
                Filing_Date=Filing_Date.encode('ascii', 'ignore').decode('ascii')
                TM5_Descriptor=TM5_Descriptor.encode('ascii', 'ignore').decode('ascii')
                Status_Date=Status_Date.encode('ascii', 'ignore').decode('ascii')
                Publication_Date=Publication_Date.encode('ascii', 'ignore').decode('ascii')
                Date_Abandoned=Date_Abandoned.encode('ascii', 'ignore').decode('ascii')
                International_Class=International_Class.encode('ascii', 'ignore').decode('ascii')
                Owner_Name=Owner_Name.encode('ascii', 'ignore').decode('ascii')
                Correspondent_Name_Address=Correspondent_Name_Address.encode('ascii', 'ignore').decode('ascii')
                Legal_Entity_Type=Legal_Entity_Type.encode('ascii', 'ignore').decode('ascii')
                Phone=Phone.encode('ascii', 'ignore').decode('ascii')
                Correspondent_e_mail=Correspondent_e_mail.encode('ascii', 'ignore').decode('ascii')
                Document_Date=Document_Date.encode('ascii', 'ignore').decode('ascii')
                Document_Title=Document_Title.encode('ascii', 'ignore').decode('ascii')
                Offc_Action_Date=Offc_Action_Date.encode('ascii', 'ignore').decode('ascii')
                SUMMARY_OF_ISSUES=SUMMARY_OF_ISSUES.encode('ascii', 'ignore').decode('ascii')
                
                if " "in Correspondent_e_mail:
                    emailval= Correspondent_e_mail.split(" ")
                    counter=1
                    for i in emailval:
                        if counter ==1:
                            email1= i
                        if counter ==2:
                            email2= i
                        if counter ==3:
                            email3= i
                        if counter ==4:
                            email4= i
                        if counter ==5:
                            email5= i
                        counter = counter+1
                else:
                    email1= Correspondent_e_mail
                    email2= "NA"  
                    email3= "NA"
                    email4= "NA"
                    email5= "NA"
                    
                            
                    
                    
                writer.writerow({'trno':c,'Literal Element':Mark,"Mark Type":Mark_Type,"Serial":serialno,"TSDR":linkval,"International Class(es)":International_Class,    
                    "Filing Date":Filing_Date,"Publication Date":Publication_Date,"Correspondent Name/Address":Correspondent_Name_Address,"Correspondent Organization":Owner_Name,"Correspondent Phone Number":Phone,
                    "Legal Entity Type / Is Corporate Filer":Legal_Entity_Type,"TM5 Common Status / Alt Legal Status":TM5_Descriptor,
                    "Status Date":Status_Date,"Date_Abandoned":Date_Abandoned,"Mail Date":Document_Date,"Latest Document Description":Document_Title,"Summary of issues in latest office action":SUMMARY_OF_ISSUES,"Date of latest office action":Offc_Action_Date,"E-Mail 1":email1,"E-Mail 2":email2,"E-Mail 3":email3,
                    "E-Mail 4":email4,"E-Mail 5":email5})   

                Mark = ""
                serialno = ""
                Filing_Date = ""
                Mark_Type = ""
                TM5_Descriptor = ""
                Status_Date = ""
                Publication_Date = ""
                Date_Abandoned = ""
                International_Class = ""
                Owner_Name = ""
                Correspondent_Name_Address = ""
                Legal_Entity_Type = ""
                Phone = ""
                Correspondent_e_mail = ""
                Document_Date = ""
                Document_Title = ""
                Offc_Action_Date = ""
                SUMMARY_OF_ISSUES = ""
                linkval = ""
                
            print("Exitting for loop ..........")
            if x==tasks:
                lb.config(text=str((100))+"%")

            progtrack['value'] =100
            # progress1 = Progressbar(root,style="TProgressbar", length=650, mode='determinate')
            # progress1.place(x=20,y=150)
            # progress1['value'] =100
            progresslabel.config(text=" !!! Completed !!! ",foreground="white")

    #root.destroy()
def ask():
    answer= askyesno(title=None, message="Do You want to run?")
    if not answer:
        root.destroy()
    else:
        bar()

root = Tk()
root["bg"] = "#0a5371"

f1 = "arial 15 bold"
lb = Label(root,text="0%",font=f1,background="#0a5371",foreground="white")
lb.place(x=180,y=100)

#for processing label
progresslabel = Label(root,text="  Waiting to be run",font=("Arial","12",BOLD),background="#0a5371",foreground="#ffffff")
progresslabel.place(x=120,y=200)

trademarknolabel = Label(root,text="Trademark no...",font=("Arial","10",BOLD),background="#0a5371",foreground="white")
trademarknolabel.place(x=20,y=60)
trademarknolabel1 = Label(root,text="",font=("Arial","8"),background="#0a5371",foreground="white")
trademarknolabel1.place(x=20,y=80)

statuslabel = Label(root,text="Status",font=("Arial","8",BOLD),background="#0a5371",foreground="white")
statuslabel.place(x=310,y=120)
s = Style()
s.configure("TProgressbar", foreground='#09BF14', background='#09BF14', thickness=100)

progress = Progressbar(root,style="TProgressbar", length=360, mode='indeterminate')
progress.place(x=20,y=150)

progtrack = Progressbar(root,style="TProgressbar", length=360, mode='determinate')
progtrack.place(x=20,y=150)

btn = Button(root, text='Start',width=25, command=prebar)
btn.place(x=120,y=230)

root.title("Effectual Tredmark Tool")
#root.maxsize(height=400,width=600)
root.maxsize(height=300,width=400)
root.minsize(height=300,width=400)
#root.title("progress")
mainloop()
