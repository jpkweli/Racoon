from tkinter import *
from tkinter import filedialog, Tk
import xml.etree.ElementTree as ET

loadx =""
savex = ""
process = False
message = 'Load, Name, and Convert please'

window = Tk()
window.title ('RACOON Unmerges Clips')

def racoon():
    l5["text"] = 'Processing...'
    if l3["text"] !="Input File" and l4["text"] != "Output File":
        # Lists
        narchivo = []  # List containing Clips' file names (Audio).
        nid = []  # List containing Clip's IDs (Audio)
        narchivo2 = []  # List containing Clips' file names (Video).
        nid2 = []  # List containing Clip's IDs (Video)
        # Mere Counters
        nu = 0  # File Name Counter (Audio)
        nux = 0  # Name Counter (Audio)
        nux2 = 0  # Name Counter (Audio)
        vu = 0  # File Name Counter (Video)
        vux = 0  # Name Counter (Video)
        vux2 = 0  # Name Counter (Video)
        # Other
        duplicates = 0
        replacements = 0

        tree = ET.parse(l3["text"])
        root = tree.getroot()
        print ('Restore All Clips Original Names')

        #Get File IDs & File Names
        for elid in root.findall (".//clipitem/file"):
            nid.insert(nu, (elid.get('id'))) #Warning: .get only accesses tag's attributes (inside <>)
            temp = elid.find('name')
            if temp is not None:
                narchivo.insert (nu,(str(temp.text))) #Warning: .text accesses content after end of tag: '>'
            else:
                narchivo.insert (nu,'EMPTY')
            print(nu, nid[nu], narchivo[nu]) #Number listed, Id from File, Name of Clip.
            nu += 1

        #Writing New Names in ClipItem's Name tag.
        for newname in root.findall (".//clipitem/name"):

            if narchivo[nux] != 'EMPTY': #Directly embed names of clips that has name tag with content.
                newname.text = str(narchivo[nux])
                print (nux,'had a name and it was', newname.text)
                replacements += 1
            else: #Search for clips with same IDs and steal their names, for those clips that has no name tag with content
                for nid [nux2] in nid:
                    if nid[nux2]==nid[nux] and nux2!=nux: #Search Clips with same ID and Name...
                        print (nux, 'is a duplicate from', nux2)
                        duplicates +=1
                        if narchivo[nux2] !='EMPTY': #whose name is not empty...
                            newname.text= str(narchivo[nux2])
                            print (nux,'didnt have name and was copied from', nux2, newname.text)
                            replacements += 1
                            nux2 = 0
                            break
                    if nux2 ==nu-1:
                        nux2 = 0
                        break
                    nux2 += 1
            if nux == nu-1:
                print('End of Process')
                break
            nux += 1

        print ('Made',replacements,'replacements')

        tree.write(l4["text"])
        l5["text"] = 'Done!'

def load():
    global loadx
    root = Tk()
    root.filename = filedialog.askopenfilename(initialdir="/", title="Select file", filetypes=(("XML files", "*.xml"), ("all files", "*.*")))
    loadx = str(root.filename)
    l3["text"] = loadx

def save():
    global savex
    root = Tk()
    root.filename = filedialog.asksaveasfilename(initialdir="/", title="Select file",filetypes=(("XML file", "*.xml"), ("all files", "*.*")))
    savex = str(root.filename)
    l4["text"] = savex

l1=Label(window, text="Select Your Original XML File:")
l1.grid(row=0,column=0)

l2=Label(window, text="Name Your Output XML File:")
l2.grid(row=2,column=0)

l3=Label(window, text='Input File Pending',font=('Helvetica', 10, 'italic'))
l3.grid(row=1,column=0)

l4=Label(window, text='Output File Pending',font=('Helvetica', 10, 'italic'))
l4.grid(row=3,column=0)

l5=Label(window, text='',font=('Helvetica', 10, 'italic'))
l5.grid(row=4,column=0)

b1=Button(window,text="Load", width=12, command=load)
b1.grid (row=0, column=2)

b2=Button(window,text="Save As...", width=12, command=save)
b2.grid (row=2, column=2)

b3=Button(window,text="Racoon It!", width=12, command=racoon)
b3.grid (row=4, column=2)

window.mainloop()

