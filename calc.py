from tkinter import * 

def iCalc_window(source, side):
    storeObj = Frame(source, borderwidth=1,bd=0, bg="sky blue")
    storeObj.pack(side=side, expand =YES, fill = BOTH)
    return storeObj

def button(source,side,text,command=None):
    storeObj = Button(source, text=text, command=command)
    storeObj.pack(side=side, expand=YES, fill=BOTH)
    return storeObj

class app(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.option_add('*Font', 'Helvetica 20 bold' )
        self.pack(expand=YES, fill=BOTH)
        self.master.title('PY Calc!')

        display = StringVar()
        Entry(self, relief=RIDGE, textvariable=display, justify='center', bd=30, fg='black', bg='DarkSlateGray1').pack(side=TOP, expand=YES, fill=BOTH)
        
        for ClearButton in (['C']):
            erase = iCalc_window(self, TOP)
            for ichar in ClearButton:
                button(erase, LEFT, ichar, lambda 
                storeObj=display, q=ichar: storeObj.set(''))
        
        for NumbersButton in ("789/", "456*", "123-", ".0+"):
            FunctionNumbers = iCalc_window(self, TOP)
            for iEqual in NumbersButton:
                button(FunctionNumbers, LEFT, iEqual, lambda
                storeObj = display, q=iEqual: storeObj.set(storeObj.get() + q))
        
        EqualButton = iCalc_window(self, TOP)
        for iEquals in "=":
            if iEquals == "=":
                btniEquals = button(EqualButton, LEFT, iEquals)
                btniEquals.bind('<ButtonRelease-1>', lambda e,s=self, 
                                storeObj=display: s.calculate(storeObj), '+')
            
            else: 
                btniEquals = button(EqualButton, LEFT, iEquals,
                                    lambda storeObj=display, s=' %s ' % iEquals:storeObj.set(storeObj.get() + s))


    def calculate(self, display):
        try:
            display.set(eval(display.get()))
        except:
            display.set("Error!")

if __name__ == '__main__':
    app().mainloop()
