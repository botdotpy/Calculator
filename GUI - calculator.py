from tkinter import*

#def backspace(): #function deletes the last character on the calculator screen   
#    global calculator_screen
#    calculator_screen= calculator_screen[:-1]
#    calculator_screen_string.set(calculator_screen)

def button_press(button): #formula takes in any calculator button symbol/number as parameters and casts them as strings
    global calculator_screen #refers to the global calculator screen variable
    calculator_screen = calculator_screen + str(button)
    calculator_screen_string.set(calculator_screen)

def equals():
    global calculator_screen
    
    try:
        total = str(eval(calculator_screen)) #eval would pass whatever expression is passed into the calculator screen label
        calculator_screen_string.set(total)
        calculator_screen = total  #to reuse the total parsed from a previous expression

    except ZeroDivisionError:
        calculator_screen_string.set("arithmetic error") #sets the calculator screen to display arithmetic error for zero division errors
        calculator_screen= "" #displays an empty set of quotes afterwards 
    
    except SyntaxError: #sets the calculator screen to display syntax errors for syntax errors
        calculator_screen_string.set("syntax error") #displays an empty set of quotes afterwards 
        calculator_screen=""

def clear(): #clear function sets the calculator screen string as empty set of quotes, clearing whatever expression earlier displayed
    global calculator_screen
    calculator_screen_string.set("")
    calculator_screen = ""

window = Tk() #instantiates the instance of a window

calculator_screen = "" #serves as the string source for the calculator_screen_string variable
calculator_screen_string = StringVar() #defines the string values passed to be displayed on the calculator screen label

#label forming the calculator screen that takes text variables from the calculator buttons casted as strings
calculator_screen_label = Label(window, textvariable=calculator_screen_string, font=('Consolas', 20),
                     bg='white', width=24,height=2)
calculator_screen_label.pack()


#placing the buttons in frames
frame = Frame(window)
frame.pack()

button1 = Button(frame,text=1,height=4,width=9,font=35,command= lambda: button_press(1))
button1.grid(row=0,column=0)

button2 = Button(frame,text=2,height=4,width=9,font=35,command= lambda: button_press(2))
button2.grid(row=0,column=1)

button3 = Button(frame,text=3,height=4,width=9,font=35,command= lambda: button_press(3))
button3.grid(row=0,column=2)

button4 = Button(frame,text=4,height=4,width=9,font=35,command= lambda: button_press(4))
button4.grid(row=1,column=0)

button5 = Button(frame,text=5,height=4,width=9,font=35,command= lambda: button_press(5))
button5.grid(row=1,column=1)

button6 = Button(frame,text=6,height=4,width=9,font=35,command= lambda: button_press(6))
button6.grid(row=1,column=2)

button7 = Button(frame,text=7,height=4,width=9,font=35,command= lambda: button_press(7))
button7.grid(row=2,column=0)

button8 = Button(frame,text=8,height=4,width=9,font=35,command= lambda: button_press(8))
button8.grid(row=2,column=1)

button9 = Button(frame,text=9,height=4,width=9,font=35,command= lambda: button_press(9))
button9.grid(row=2,column=2)

button0 = Button(frame,text=0,height=4,width=9,font=35,command= lambda: button_press(0))
button0.grid(row=3,column=0)

add = Button(frame,text='+',height=4,width=9,font=35,command= lambda: button_press('+'))
add.grid(row=0,column=3)

subtract = Button(frame,text='-',height=4,width=9,font=35,command= lambda: button_press('-'))
subtract.grid(row=1,column=3)

divide = Button(frame,text='/',height=4,width=9,font=35,command= lambda: button_press('/'))
divide.grid(row=2,column=3)

equal = Button(frame,text='=',height=4,width=9,font=35,command=equals)
equal.grid(row=3,column=1)

decimal = Button(frame,text='.',height=4,width=9,font=35,command= lambda: button_press('.'))
decimal.grid(row=3,column=2)

clear_button = Button(frame,text='clear',height=4,width=9,font=35,command= clear)
clear_button.grid(row=3,column=3)

#backspace_button = Button(frame,text='←',height=4,width=9,font=35,command= backspace)
#backspace_button.grid(row=4,column=3) #for a backspace button that deletes the last string on the calculator screen
            
window.title("Calculator")
window.geometry("500x500")
window.mainloop() #displays a window screen