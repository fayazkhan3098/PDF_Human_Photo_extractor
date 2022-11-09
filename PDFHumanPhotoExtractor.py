'''
=============================================================================================================================================================
--------------------------------------------------------HUMAN PHOTO EXTRACTER BY FAIYAZ KHAN-----------------------------------------------------------------
=============================================================================================================================================================

                                            The copyright symbol © OR the word “Copyright”.

                                            The first publication year: january-2022

                                            The copyright holders name: Faiyaz Minhaj Khan

                                           the publication is done for the company: thefm Solutions PVT LTD

-------------------------------------------------------------------------------------------------------------------------------------------------------------
'''
__author__ = """Faiyaz Khan """
__email__ = 'fayazkhan3098@gmail.com'
__version__ = '0.0.1'


from tkinter import *                       #installing GUI based module
from tkinter import filedialog as fd        #installing filedialog from tkinter for opening filepicker dialog box 
from tkinter import messagebox              #installing to show small notification messages at different levels of program 
import tkPDFViewer as pdv                   #pdf viewing module present in same directory
import fitz                                 #associated with pymupdf package to extract photos from pdf
import os                                   #used to do operating system based operations
import glob                                 #used to iterate files from a perticular folder
import shutil                               #used to transfer or move a file from one folder to onother folder
import photodetector as fc                  #our build package photodector to detect photos from extracted photos

'''
-------------------------------------------------------------------------------------------------------------------------------------------------------------

Innitialization of window with tkinter package
'''   
root=Tk()                                                   #declaring object for tkinter package as root window
root.title("Human Photo Extracter by Thefm solutions")      #setting window title as program defines
root.geometry('950x600')                                    #restricting window size to height=950 and height=600
root.resizable(False,False)                                 #Restricting window from resizing by user 
root.iconbitmap('PHPEicon.ico')                             #setting window icon to PHPEicon.ico file which is 
                                                            #saved in same directory where this program PDFHumanphotodetector.py is saved 
'''
==============================================================================================================================================================
Top Frame with their Attributes and widgets

this frame contains mainly Two widgets
1) company Icon Button which shows the developer details
2) Main label as Human Photo Extracter
'''
topframe=Frame(root,height=50,highlightbackground='black',highlightthickness=1)     #Creating a topFrame as widget of root window with height 50 pixels
topframe.pack(side=TOP,fill=BOTH)                                                   #and packing it at the top of the root window and it is filling both
                                                                                    # side of the root window
#____________________________________________________________________________________________________________________________________________________________
'''
This about function defined to show the messege box about developer
when abtbutton is pressed  
'''
def about():                                                                                     #Defined or declared about method
    messagebox.showinfo("ABOUT",                                                           #
    "Information about the developer of this program \t \t  \nThis programs all rights reserved by : \t\t \nThe copyright holders name: Faiyaz Minhaj Khan \nThe first publication year: january-2022\nThank you for using this software")                                   
                                                                                        # Defining developers information and the date of development
#____________________________________________________________________________________________________________________________________________________________

about_btn=PhotoImage(file='fm.png')                                         #Reading fm.png image icon to about_btn variable to pass to abtbutton button
abtbutton=Button(topframe,image=about_btn,command=about)                    #declared abtbutton for top frame and and given command as to execute 
abtbutton.pack(side=LEFT,pady=20,padx=20)                                   #about() function in response and packed it to the left side of top frame

#____________________________________________________________________________________________________________________________________________________________

toplabel=Label(topframe,                                                #Declared a label with Toplabel name in topframe 
                    text="HUMAN PHOTO EXTRACTER FROM PDF",              #with text of Application Title
                    fg = "gray",                                        #with gray foreground
                    bg = "white",                                       #with white background
                    font = "Helvetica 16 bold italic").pack(side=LEFT,  #with helvetica font 16 size Style bold italic and  
                    expand = True,                                      #packed it next right to abtbutton in top frame with 
                    fill = BOTH)                                        #full expandation and filling both side of remaining frame 

'''
==============================================================================================================================================================
Bottom Frame and its content and widgets
'''
            
botFrame = Frame(root,height=50,                              #Declaired Bottom frame to the main root window with 50 pixels of height 
                    highlightbackground='black',              #and with black background and size 1 thicked bordered
                    highlightthickness=1)                                                                                                        
botFrame.pack(side=BOTTOM,fill=BOTH)                          #and Packed it at bottom of main root window frame and filled both side                     

'''
==============================================================================================================================================================
Left Frame and its content and widgets

this frame contains mainly Six Widgets
1) Button Clear Button to clear the window 
2) Button Save button to save the extracted photo 
3) Button Extract button to extract photos from selected PDF
4) Button Impoert file button to import PDF file from users device
5) Canvas as extracted_photo for photo whichever human photo get detected will be displayed here
6) Label Label1 for displaying selected PDF file name on the screen
'''
            
leftframe=Frame(root,width=300,height=450,              # Declaring Left frame to the main root window with 300 and 450 pixels width and height respectively 
                bg='aliceblue',                         # with Alice Blue Colored background
                highlightbackground='black',            # black highlighted background and 
                highlightthickness=1)                   # side thickness of 1
leftframe.pack(side=LEFT,expand = True, fill = BOTH)    # Packing declared left frame to the left side of root window  

#____________________________________________________________________________________________________________________________________________________________

clear_btn=Button(leftframe ,text='CLEAR')               # Declared Claer_btn Button in Leftframe with CLEAR Title
clear_btn.pack(side=BOTTOM,fill=BOTH,ipady=5)           # and Packed it to the Bottom of leftframe with 5 pixels internal padding in y direction
                                                        # and filled with both sode of left frame

#____________________________________________________________________________________________________________________________________________________________

saveAbtn=Button(leftframe ,text='SAVE',state=DISABLED)  # Declared saveAbtn Button in Leftframe with SAVE Title and disabled it to deny early access
saveAbtn.pack(side=BOTTOM,fill=BOTH,ipady=5)            # and Packed it to the Bottom of leftframe above clear_btn
                                                        # with 5 pixels internal padding in y direction and filled with both sode of left frame

#____________________________________________________________________________________________________________________________________________________________

extract_btn=Button(leftframe,text='EXTRACT',state=DISABLED) # Declared extract_btn Button in Leftframe with EXTRACT Title & disabled it to deny early access
extract_btn.pack(side=BOTTOM,fill = BOTH,ipady=5)           # and Packed it to the Bottom of leftframe above saveAbtn
                                                            # with 5 pixels internal padding in y direction and filled with both sode of left frame

#____________________________________________________________________________________________________________________________________________________________

import_filebtn=Button(leftframe,text='IMPORT FILE')     # Declared import_filebtn Button in Leftframe with IMPORT FILE Title
import_filebtn.pack(side=BOTTOM,fill = BOTH,ipady=5)    # and Packed it to the Bottom of leftframe above extract_btn
                                                        # with 5 pixels internal padding in y direction and filled with both sode of left frame

#____________________________________________________________________________________________________________________________________________________________

            
extracted_photo=Canvas( leftframe,                          # Declared extracted_photo Canvas in Leftframe 
                        height = 261,                       # with 261 pixels of height
                        width = 250,                        # with 250 pixels of width
                        highlightbackground='black',        # with black colored highlighted background
                        highlightthickness=1)               # and size 1 of border thickness

humanbgp=PhotoImage(file='humanbgp.png')                    #Reading humanbgp.png image file to humanbgp variable to pass to extracted_photo canvas

hmnbgp=extracted_photo.create_image(0,0,                    # calling create_image method from Canvas to put photo in canvas with 0,0 x,y respective indexing
                                    anchor="nw",        # anchors can specify where a widget is located inside a frame when the frame is bigger than the widget.
                                    image=humanbgp)         # and passed already red photo image at humanmgp 

extracted_photo.pack(side=TOP,padx=10,expand=TRUE)          # and Packed it to the Top of the left frame above label1 

#____________________________________________________________________________________________________________________________________________________________

Label1=Label(leftframe)                                     # Declared Label1 to left frame 
Label1.pack(side=TOP,fill=BOTH)                             # and packed it to Top of left frame, below Extracted_photo canvas and above import_file button 

'''
==============================================================================================================================================================
PDF Frame right to left frame with its content and widgets

this frame contains mainly A Single Widgets
1) the Pdf frame it self is used to add another pdf showing Pdf from tkpdfviewer package

'''

pdfframe=Frame( root,                                   # Declaring PDFframe to the main root window  
                width=650, height=450,                  # with 650 and 450 pixels width and height respectively
                bg='cornflowerblue',                    # with cornflower blue colored background
                highlightbackground='black',            # and with black colored 
                highlightthickness=1)                   # and 1 pixel thick sized border  

pdfframe.pack(side=LEFT,expand = True, fill = BOTH)     # and Packed it to right side of left frame in main root window

'''
==============================================================================================================================================================
Director Method and its Functioning

this method is created to import pdf file from the user 
display it on the pdfframe and detecting all pictures from pdf
and saving it to temp folder 

'''

def director():                                                                     # Initiated director method whose command is given to import file button
#____________________________________________________________________________________________________________________________________________________________

    filename=fd.askopenfilename(initialdir='/',                                     # created an object from filedialog package from tkinter to open file
                                                                                    # navigator & passed initial directory as same as the program is running in
    title='Open a PDF file',                                                        # titled as Open a PDF File
    filetypes=[('All PDF files', '*.pdf'),('All PDF files', '*.PDF')])              # with two extension type of all pdf files 
                                                        
#____________________________________________________________________________________________________________________________________________________________              
    Label1['text']=("Selected file ->\n "                                           # passing the PDF file name which is selected by user to the label1 
                    +os.path.basename(filename))                                    # which is declared in
#____________________________________________________________________________________________________________________________________________________________
    d=pdv.ShowPdf().pdf_view(   pdfframe,pdf_location=filename,                     # Creating an object of pdfview method from tkPDFViewer package
                                                                                    # to display pdf to user in the form of frame d at pdfframe 
                                width=100,height=200)                               # with pdf location 100 & 200 pixels width & height respectively
    #__________________________________________________________________________________________________________________
    d.pack(expand=True)                                                             # And packing d frame expanded all over to pdfframe
    print('pdf dislayed')                                                           # and confirming the status of program in console
#____________________________________________________________________________________________________________________________________________________________                 
    pdf = fitz.open(filename)                                                       # object created for opening pdf file using Fitz package                 
    image_list=pdf.getPageImageList(0)                                              # detecting all images from pdf file in at page no 1(indexing starts with 0 )                
    for image in image_list:                                                        # converting image to pixel format 
        xref = image[0]                                                             # index value of image array given to xref 
        pix= fitz.Pixmap(pdf, xref)                                                 # Each pixel is described by a number of bytes (“components”) defining
                                                                                    # Create a pixmap from an image contained in PDF doc identified by its XREF number.
                                                                                    # All pixmap properties are set by the image.
        #__________________________________________________________________________________________________________________
                                                                                    # its color, plus an optional alpha byte defining its transparency.
        if pix.n < 5:                                                               # checking bytes per pixel in each image page of pdf
                                                                                    
            pix.writePNG(f'temp\{os.path.basename(filename)}.png')                  # if it is less than 5 then saving that image into temp file
        #__________________________________________________________________________________________________________________
        else:                                                                       # and if grater than 5 then 
            pix1=fitz.open(fitz.csRGB, pix)                                         # Colorize (tint) a pixmap with a color provided as a value triple (red, green, blue).
            pix1.writePNG(f'temp\{os.path.basename(filename)}.png')                 # and then then saving that image into temp file
            pix1 = None                                                             # vacating pix1 variable after completion of else
        pix=None                                                                    # vacating pix1 variable after completion of if-else
    #__________________________________________________________________________________________________________________
    strr=str(filename+str(len(image_list))+'detected')                              # collecting to display on console file name and length of image list 
    print(strr)                                                                     # and confirming the status of program in console

#____________________________________________________________________________________________________________________________________________________________
                        
    import_filebtn['state'] = DISABLED                                              # As importing of pdf file id completed then disabeling importfilebtn to stop errors
    extract_btn['state'] = NORMAL                                                   # and enabling Extract btn as it is ready to perform extreaction of human photo


'''
===================================================================================================================================================================================
Extracter Method and its Functioning

this method is created to detect Human Photo from the list of photos at temp folder
'''

def extracter():                                        # Initiated extracted method whose command is given to extractbtn button
#____________________________________________________________________________________________________________________________________________________________
    global face                                         # Globally declaring face variable to access it from different methods
    face=fc.Innerextracter().facade()                   # calling facade method from innerextracter class throug photodetoector package
                                                        # which returns the path of human photo or a text  
    #__________________________________________________________________________________________________________________
    if os.path.isfile(face)==False:                     # lets ckeck it is text or a path of photo is os Package method isfile()
        messagebox.showinfo("Process Status",               # If it is a text the 'no human photo detected 'message box will be shown on the screen
                            "OOPs! sorry \nTheir is No Human Picture been Detected in PDF")
        #__________________________________________________________________________________________________________________
        extract_btn['state'] = DISABLED                     # as No human photo found so disabling extractbtn button to save application from over attempt
        saveAbtn['state'] = DISABLED                        # as No human photo found so disabling extractbtn button to save application from over attempt
        #__________________________________________________________________________________________________________________
    else:                                                   #else 
        img2 = PhotoImage(file=face)                        # Reading image to img2 variable from returned face photo path
        extracted_photo.delete('all')                       # deleting all widgets or items from canvas
        extracted_photo.create_image(0,0,                   # calling create_image method from Canvas to put photo in canvas with 0,0 x,y respective indexing
                                    anchor="center",        # anchors can specify where a widget is located inside a frame when the frame is bigger than the widget.
                                    image=img2)

                                                            # changing photo of canvas extracted photo to human photo 
        saveAbtn['state'] = NORMAL                          # and as Saving can be done so enabling savebtn button

'''
==================================================================================================================================================================================
Navigator Method and its Functioning

This method is created to take path from user for saving detected picture 
and to move the extracted photo to given path 

'''

def navigator():                                                                    # Initiated extracted method whose command is given to savebtn Button
    #____________________________________________________________________________________________________________________________________________________________________________
            try:                                                                    # code has been putted in try method for handling errors
                print('face:   ',face)                                              # Accessing face object path for restricting Nameerror 
                #__________________________________________________________________________________________________________________    
                nobj= fd.asksaveasfile(mode='a',initialfile = 'extracted photo ',   # Asked User to give path where we could append the extracted photo
                defaultextension=".png",                                            # with append mode, initialfilename as extracted photo andpng extention
                filetypes=[("png pictures","*.png"),("PNG pictures","*.PNG")])      # suggested file types
                print('nobj.name:  ',nobj)                                          # and confirming the status of program in console
            #__________________________________________________________________________________________________________________    
                shutil.move(face,nobj.name)                                         # using move method of shutil package moving file to asked directory 
                print('navigation completed')                                       # and confirming the status of program in console
            #__________________________________________________________________________________________________________________
                messagebox.showinfo("Process Status", "Photo has been extracted succesfully and saved at your Navigated directory !!!")
                                                                                    # and giving Confirmation to the user that photo moved 
            #__________________________________________________________________________________________________________________    
            except NameError as e:
                messagebox.showwarning('wrong Step','OOPs! \nFor saving your photo please complete import and extract procedure first !!!')
                                                                                    # if error occured warning user for such 

'''
===============================================================================================================================================================================
Cleaner Method and its Functioning

This method is created to clear or 
vanish the widgets and data which may act as cashes in program 

'''

def cleaner():                                                          #Initiated cleaner method whose command is given to clearbtn Button
#_____________________________________________________________________________________________________________________________________________________________
    for wid in pdfframe.winfo_children():                               # accesing displayed pdf in pdf frame 
                            print(wid,'destroing')                      # confirming the status of program in console
                            wid.destroy()                               # Destroying d frame from pdfframe
    #__________________________________________________________________________________________________________________                       
    Label1['text']=''                                                   # vacating label1 from selected file name
    #__________________________________________________________________________________________________________________
    extracted_photo.delete('all')                     # deleting all widgets or items from canvas
    extracted_photo.create_image(0,0,                 # calling create_image method from Canvas to put humanbackground  
                                                      # back again photo in canvas with 0,0 x,y respective indexing
                                    anchor="nw",      # anchors can specify where a widget is located inside a frame when the frame is bigger than the widget.
                                    image=humanbgp)   # changing extracted photo to human baground photo in extracted_photo canvas
    #__________________________________________________________________________________________________________________
    import_filebtn['state'] = NORMAL                                    # making import file btn accesible for new execution
    #__________________________________________________________________________________________________________________
    for imagePath in glob.glob('temp/*.png'):                           # if and only if the user wants to clear screen before 
        os.remove(imagePath)                                            # extraction and save the detected pictures in temp folder will be removed to trash

'''
================================================================================================================================================================================
This section basically used to give command of methods 
to the perticular Button to perform perticular 
Action

'''

saveAbtn['command']         =navigator          # Given Navigator method command to SaveAbtn Button    
extract_btn['command']      =extracter          # Given Extracter method Command to extract_btn Button
import_filebtn['command']   =director           # Given director method Command to import_filebtn Button
clear_btn['command']        =cleaner            # Given Cleaner method Command to clear_btn Button

'''
=================================================================================================================================================================================
root. mainloop() is a method on the main window which we execute when we want to run our application. 
This method will loop forever, waiting for events from the user, until the user exits the program , 
Either by closing the window, or by terminating the program with a keyboard interrupt in the console.

'''

root.mainloop()         #lets Tkinter to start running the application by closing its root object

'''
==============================================================================================================================================================

---------------------------------------------------------------------Acknowledgement---------------------------------------------------------------------------



'''