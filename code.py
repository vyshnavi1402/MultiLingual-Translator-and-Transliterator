from googletrans import Translator
from gtts import gTTS
from playsound import playsound
import os
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from PIL import Image,ImageTk
import PyPDF2
from indic_transliteration import sanscript
from indic_transliteration.sanscript import transliterate
import pyaudio
import speech_recognition as sr

root=Tk()
root.geometry("1000x280")
root.state('zoomed')
root.title('Language Translator ...')

#for background
my_img=PhotoImage(file='C:\\Users\\vyshg\\Downloads\\w.png')
lab=Label(root,image=my_img)
lab.pack()

#enter text

label1=Label(root,text='Enter text here',font=('verdana',18, 'bold'),fg='black',bg='white')
label1.place(x=19,y=23)
text_entry1=Text(root,height=15,width=35,bg='white',fg='purple',font=('Times',17))
text_entry1.place(x=50,y=70)

#for translated text

label2=Label(root,text='Translation here',font=('verdana',18, 'bold'),fg='black',bg='white')
label2.place(x=1150,y=20)
text_entry2=Text(root,height=15,width=35,fg='purple',font=('Times',17))
text_entry2.place(x=1090,y=70)

label3=Label(root,text='or',fg='black',font=('calibre',18, 'bold'),bg="white")
label3.place(x=270,y=20)

def speech():
  r = sr.Recognizer()
  with sr.Microphone() as source:
        print("speak now!")
        # Adjust the noise threshold to account for ambient noise
        r.pause_threshold=0.5
        r.adjust_for_ambient_noise(source)
        
        # Listen for the user's speech input
        audio = r.listen(source)
        
        
        try:
            # Convert the user's speech to text
            text1 = r.recognize_google(audio)
            print(text1)
            text_entry1.insert('1.0',text1)
        except sr.UnknownValueError:
            print("could not find")



def clear():
    text_entry1.delete(1.0,'end')
    text_entry2.delete(1.0,'end')


def browse_file():
    file_path = filedialog.askopenfilename()
    # read the contents of the file and display in the file_contents Text widget
    with open(file_path, 'r') as file:
        text = file.read()
        text_entry1.insert('1.0', text)
   
    
def show():
    
    if os.path.exists("translate.mp3"):
                      os.remove("translate.mp3")
                      text_entry2.delete(1.0,'end')
    result=text_entry1.get(1.0,END)
    t=Translator()# googletrans
    to=clicked.get()
    if to == "English":
            abbr="en"
    elif to == "Telugu":
            abbr="te"
    elif to =="Hindi":
            abbr="hi"
    elif to =="Marathi":
            abbr="mr"
    elif to == "Bengali":
            abbr="bn"
    elif to == "Kannada":
            abbr="kn"
    elif to == "Malayalam":
            abbr="ml"
    elif to == "Gujarati":
            abbr="gu"
    elif to == "Tamil":
            abbr="ta"
    
    
    
    
    
    translated=t.translate(result, dest=abbr)
    translated=translated.text
    obj=gTTS(text=translated, slow=False,lang = abbr)
    obj.save('translate.mp3')
    text_entry2.insert("1.0",translated)
    playsound('translate.mp3')



options = [
    "English",
    "Telugu",
    "Hindi",
    "Marathi",
    "Bengali",
    "Kannada",
    "Malayalam",
    "Gujarati",
    "Tamil"
    
]
clicked = StringVar()
#drop down
clicked.set("Select Language!")
drop = OptionMenu(root , clicked , *options)
drop.configure(background="deeppink", foreground="white",width=28, font=('calibre',12, 'bold'))
drop.place(x= 570, y=12)
#button
button = Button(root , text = "Translate!", bg="white",fg="lightseagreen", font=('verdana',18, 'bold'), command=show)
button.place(x=500, y=350)
but2 = Button(root , text = "Clear!",bg="lightseagreen",command=clear,fg="white", font=('verdana',18, 'bold'))
but2.place(x=800, y=350)
browsebutton = Button(root, text="Browse",command=browse_file,font=('verdana',15, 'bold'),bg='skyblue')
browsebutton.place(x=350,y=20)
#arrow image
arrowimage=PhotoImage(file='C:\\Users\\vyshg\\Downloads\\a1.png')
image_label=Label(root,image=arrowimage,width=200)
image_label.place(x=620,y=180)

# for transliteration
language_scripts = {
    "Devanagari": sanscript.DEVANAGARI,#Hindi,marati,sanskrit,nepali
    "Bengali": sanscript.BENGALI,#Bengali,Assamese
    "Gujarati": sanscript.GUJARATI,
    "Gurmukhi": sanscript.GURMUKHI,
    "Kannada": sanscript.KANNADA,
    "Malayalam": sanscript.MALAYALAM,
    "Oriya": sanscript.ORIYA,
    "Tamil": sanscript.TAMIL,
    "Telugu": sanscript.TELUGU,
    "English":sanscript.ITRANS,
    
}
def transliterate_text():
    
    #this is for input which is output of translator
    e_text=text_entry2.get('1.0', END)
    print(e_text)
    input_language = input_language_var.get()
    target_language = target_language_var.get()
    target_script = language_scripts[target_language]
    input_script = language_scripts[input_language]
    transliterated_text = transliterate(e_text,input_script,target_script)
    # Insert the transliterated text into the output textbox
    output_textbox.delete("1.0", "end")
    output_textbox.insert("end", transliterated_text)


output_textbox = Text(root, width=30, height=10,bg='#F0FFFF',font=('verdana',13,'bold'))
output_textbox.place(x=550,y=500)

# Create the dropdown menus for selecting the input and target languages
language_options = ["English", "Devanagari", "Bengali", "Gujarati", "Gurmukhi", "Kannada", "Malayalam", "Oriya", "Tamil", "Telugu"]
input_language_var =StringVar(root)
input_language_var.set("source Language!")
input_language_dropdown = OptionMenu(root, input_language_var, *language_options)
input_language_dropdown.place(x=200,y=550)
target_language_var = StringVar(root)
target_language_var.set("Target Language!")
target_language_dropdown = OptionMenu(root, target_language_var, *language_options)
target_language_dropdown.place(x=1090,y=550)

# Create the "Transliterate" button to trigger the transliteration
transliterate_button = Button(root, text="Transliterate",bg="LavenderBlush",fg="forestgreen", font=('verdana',16,'bold'),command=transliterate_text)
transliterate_button.place(x=640,y=700)

# speak button
speakbutton = Button(root, text="speak",command=speech,font=('verdana',13,'bold'))
speakbutton.place(x=230,y=460)

root.mainloop()

