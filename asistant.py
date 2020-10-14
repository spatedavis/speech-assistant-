import speech_recognition as sr 
import pyttsx3  
import tkinter as tk  
import wikipedia
import random
import pyjokes
# Initialize the recognizer  
r = sr.Recognizer()  

def SpeakText(command): 
      
    # Initialize the engine 
    engine = pyttsx3.init() 
    engine.say(command)  
    engine.runAndWait() 

root=tk.Tk()
root.geometry("300x200")
root.configure(bg="black")
root.title("J.A.R.V.I.S")
wel='i am jarvis what can i do for you sir '
 
jk =['joke','joke please','tell me a joke','tell a joke','tellajoke','jokeplease','tellmeajoke','jose please','jones please']
gf = 'who is your girlfriend' 
gs='Siri is my girlfriend'   
      
# Loop infinitely for user to 
# speak 
def SpeechRec():  
    while(1):     

        # Exception handling to handle 
 # exceptions at the runtime 
        #try: 

            # use the microphone as source for input. 
        with sr.Microphone() as source2: 

                # wait for a second to let the recognizer 
                # adjust the energy threshold based on 
                # the surrounding noise level  
            r.adjust_for_ambient_noise(source2, duration=0.1) 

                #listens for the user's input  
            audio2 = r.listen(source2) 

                # Using ggogle to recognize audio 
            MyText = r.recognize_google(audio2,language="en-in") 
            MyText = MyText.lower()
            
            for i in jk:
                if MyText == i:
                    joke=pyjokes.get_joke()
                    T.insert(tk.END,joke)
                    SpeakText(joke)
                    break
                elif MyText== gf:    
                    SpeakText(gs)
                    break
                else:
                    
                    
                    try:
                        result = wikipedia.summary(MyText, sentences = 2)
                        #result = wikipedia.summary(MyText, sentences = 2)          
                        T.insert(tk.END,result)
                        SpeakText(result)
                  
                    except wikipedia.DisambiguationError as e:
                        s = random.choice(e.options)
                 #result = wikipedia.page(s)
                        result = wikipedia.summary(s, sentences = 2)          
                        T.insert(tk.END,result)
                        SpeakText(result)                                 
                    break
            
        
              
def clear():
    T.delete("1.0","end")
            
T=tk.Text(root)
SpeakText(wel)
T.place(x=7,y=5,height=80,width=290)
b=tk.Button(root,text="Speak",fg="white",bg="red",command=SpeechRec)
b.place(x=35,y=100,height=50,width=100)
b1=tk.Button(root,text="Clear",fg="white",bg="blue",command=clear)
b1.place(x=150,y=100,height=50,width=100)

root.mainloop()