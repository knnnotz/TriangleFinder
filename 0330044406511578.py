from tkinter import *
from tkinter.ttk import Combobox
import math  

"""
-------------------------------
--- Triangle Finder Program ---
-------------------------------

1.Find the type of Triangle [Left Side]
    1.1 Input : 3 values (input has value more than 0.0 and less than 1000.0)
    1.2 Output : 1 value (Click Enter Button and see at the result label)
    
2.Find the last side of Triangle by input 2 sides and type of Triangle
    2.1 Input : 3 values 
        2.1.1 Length Side : 2 values (input has value more than 0.0 and less than 1000.0)
        2.1.2 Type of Triangle : 1 value             
            text='1. right triangle'
            text='2. equilateral triangle'
            text='3. isosceles triangle'
            text='4. scalene triangle'
    2.2 Output : 1 value (Click Enter Button and see at the result label)

---------------------
Last Edit 6 May, 2019
--------------------- 
Subject IT Project Management
Computer Engineering, King Mongkut's Institute of Technology Ladkrabang
- 59010330 Chinnawat Chaisuriyasak
- 59010444 Nuttapat Pimthong
- 59010651 Thawin Boonchoen 
- 59011578 Itiwat Supensilp
"""

def main():
    root = Tk()
    root.title('Triangle Finder')
    mywin=MyWindow(root)
    root.minsize(width=650,  height=350)
    root.mainloop()

class MyWindow:
    """
    --- Section 1 ---
    Get 3 inputs -> 1 result
    """
    def __init__(self, win):
        self.lbl1=Label(win, text='Label 1')
        self.lbl2=Label(win, text='Label 2')
        self.lbl3=Label(win, text='Label 3')
        self.lbl4=Label(win, text='Result')
        self.t1=Entry()
        self.t2=Entry()
        self.t3=Entry()
        self.t4=Entry()
        self.btn1 = Button(win, text='Enter')

        #Position Label, Text
        self.lbl1.place(x=25, y=50)
        self.t1.place(x=125, y=50)
        self.lbl2.place(x=25, y=80)
        self.t2.place(x=125, y=80)
        self.lbl3.place(x=25, y=110)
        self.t3.place(x=125, y=110)
        self.lbl4.place(x=125, y=140)

        self.b1=Button(win, text='Enter', command=self.enter1)
        self.b2=Button(win, text='Result')
        self.b1.place(x=25, y=140)

        """
        Section 2 
        Get 2 inputs 1 triangle type -> 1 output (Another Side)
        """
        self.lbl6=Label(win, text='Label 1')
        self.lbl7=Label(win, text='Label 2')
        self.lbl8=Label(win, text='Select Type')
        self.lbl9=Label(win, text='1. right triangle')
        self.lbl10=Label(win, text='2. equilateral triangle')
        self.lbl11=Label(win, text='3. isosceles triangle')
        self.lbl12=Label(win, text='4. scalene triangle')
        self.lbl13=Label(win, text='Result')
        self.t6=Entry()
        self.t7=Entry()
        self.t8=Entry()
        self.btn2 = Button(win, text='Enter')

        #Position Label, Text
        self.lbl6.place(x=375, y=50)
        self.t6.place(x=475, y=50)
        self.lbl7.place(x=375, y=80)
        self.t7.place(x=475, y=80)
        self.lbl8.place(x=375, y=110)
        self.t8.place(x=475,y=110)
        self.lbl9.place(x=475,y=140)
        self.lbl10.place(x=475, y=170)
        self.lbl11.place(x=475, y=200)
        self.lbl12.place(x=475, y=230)
        self.lbl13.place(x=475, y=260)

        self.b3=Button(win, text='Enter', command=self.enter2)
        self.b4=Button(win, text='Result')

        self.b3.place(x=375, y=260)


    def enter1(self):
        """
        This function 'enter1' is Triangle Finder
        Get 3 Inputs -> Result Type of Triangle
        """
        sidea = float(self.t1.get())
        sideb = float(self.t2.get())
        lastSide = float(self.t3.get())

        side1 = float(format(sidea,'.5f'))
        side2 = float(format(sideb,'.5f'))
        side3 = float(format(lastSide,'.5f'))
        #find min_side, mid_side, max_side
        min_side = min(side1,side2,side3)
        max_side = max(side1,side2,side3)

        if side1 <= side2 <= side3 or side3 <= side2 <= side1:
            mid_side = side2
        elif side2 <= side1 <= side3 or side3 <= side1 <= side2:
            mid_side = side1
        else:
            mid_side = side3

        #check value > 0.0 && <= 1000
        if (0.0 < (side1 and side2 and side3) <= 1000):

            #check is that Triangle 
            #if  (side1 + side2 > side3 or side2 + side3 > side1 or side1 + side3 > side2) and (side1 or side2 or side3 > 0):
            if(min_side + mid_side >= max_side):
                #if each side = 0
                #if each size = negative number
                #if each size has no value

                #equilateral triangle
                if side1 == side2 == side3 :
                    result=('Result: equilateral triangle')
                
                #isosceles triangle
                elif (side1 == side2 and side1 != side3) or (side2 == side3 and side2 != side1) or (side1 == side3 and side1 != side2) :
                    result=('Result: isosceles triangle')
                
                #--- right triangle ---
                    # normal case: precios length size
                    # elif (side1**2 + side2**2 == side3**2) or (side1**2 + side3**2 == side2**2) or (side2**2 + side3**2 == side1**2) :
                # sensitive case use to proof in floating point
                elif (abs(side1**2 + side2**2 - side3**2)<0.1) or (abs(side1**2 + side3**2 - side2**2)<0.1) or (abs(side2**2 + side3**2 - side1**2)<0.1) :
                    result=('Result: right triangle')
                
                #scalene triangle
                elif side1 != side2 != side3 :
                    result=('Result: scalene triangle')

            else:
                result=('Your length could not be Triangle or Invalid')
        else:
            result=('input value less than 0 or more than 1000')

        string_to_display = result
        self.lbl4["text"]=string_to_display

        v0=IntVar()

    def enter2(self):
        """
        This function 'enter2' is Triangle Side Finder
        Get 2 Inputs And Type of Triangle -> Result length side of Triangle
        """
        side4 = float(self.t6.get())
        side5 = float(self.t7.get())
        side6 = int(self.t8.get()) #get type of triangle
        list = [side4,side5]
        list.sort()

        """
        Note
            text='1. right triangle'
            text='2. equilateral triangle'
            text='3. isosceles triangle'
            text='4. scalene triangle'
        """
        #text='1. right triangle'
        if side6 == 1:
            result2 = math.sqrt(list[0]**2 + list[1]**2)
            lastSide = float(format(result2, '.5f'))
            result2=("Result: Another Side is " + str(lastSide))
        
        #text='2. equilateral triangle'
        elif side6 == 2:
            if side4 == side5:
                lastSide = float(format(side4, '.5f'))
                result2=("Result: Another Side is " + str(lastSide))
            else:
                result2=("* Side A and B not equal")
        
        #text='3. isosceles triangle'
        elif side6 == 3:
            if side4 == side5:
                lastSide = side4 + side5 - 1
                result2=("Result: Another Side is " + str(lastSide))
            else:
                lastSide = float(format(list[1], '.5f'))
                result2= ("Result: Another Side is " + str(lastSide))
        
        #text='4. scalene triangle'
        elif side6 == 4:
            lastSide = side4 + side5 - 1
            result2=("Result: Another Side is " + str(lastSide))
        else:
            print("* Something went wrong")

        string_to_display = result2
        self.lbl13["text"]=string_to_display

if __name__ == "__main__":
    main()