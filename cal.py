#CALCULATOR
import openpyxl
from pathlib import Path
import PySimpleGUI as sg
global window_2
window_2 = sg.Window
menu_def = [['&File', ['&Open', '&Save', '---', 'Properties', 'E&xit'  ]],['&Edit', ['Paste', ['Special', 'Normal',], 'Undo'],],['&Help', '&About...']]
right_click_menu = ['Unused', ['Right', '!&Click', '&Menu', 'E&xit', 'Properties']]
def initial_window():
    sg.theme('Dark Amber 5')
    layout = [[sg.Menu(menu_def, tearoff=False, pad=(200, 1))],
            [sg.Text('WELCOME TO THERMODYNAMIC PROPERTIES CALCULATOR', auto_size_text=True ,justification='center', font=("Algerian", 40))],
            [sg.Button("GO TO CALCULATOR",auto_size_button=True,font=("Algerian", 25))],
            [sg.Button("ABOUT DEVELOPERS",auto_size_button=True,font=("Algerian", 25),)],
            [sg.Button("EXIT",auto_size_button=True)]]
    window = sg.Window(title="CALCULATOR", layout = layout,resizable= True,right_click_menu=right_click_menu,default_button_element_size=(40,2),default_element_size=(40,5),auto_size_buttons=True,auto_size_text=True,element_justification='center')
    # Create an event loop 
    while True:
        event, values = window.read()
        # End program if user closes window or
        # presses the OK button
        if event == "GO TO CALCULATOR":
            window.close()
            calculator_window()
        elif event == "ABOUT DEVELOPERS":
            window.close()
            about_window()
        elif event == "EXIT" or event == sg.WIN_CLOSED or "Exit":
            break

#Saransh is great
def type_selector_window():
    refrigerant_list = ['Water','Steam','Air','Tetraflouroethane-R134a']
    sg.theme('Dark Amber 5')
    layout_type =[[sg.Menu(menu_def, tearoff=False, pad=(200, 1))],
    [sg.Text("Select the Property",size=(20,2),auto_size_text=True,font= ("Calibri", 20))],
    [sg.Button(refrigerant_list[0],size=(20,2),enable_events=True,font= ("Calibri", 20),key="data")],
    [sg.Button(refrigerant_list[1],size=(20,2),enable_events=True,font= ("Calibri", 20),key="data1")],
    [sg.Button(refrigerant_list[2],size=(20,2),enable_events=True,font= ("Calibri", 20),key="data2")],
    [sg.Button(refrigerant_list[3],size=(20,2),enable_events=True,font= ("Calibri", 20),key="data3")],
    [sg.Button("EXIT"),sg.Button("PREVIOUS")]]  
    window_type = sg.Window(title="CALCULATOR", layout = layout_type,resizable= True,right_click_menu=right_click_menu,default_button_element_size=(40,2),default_element_size=(40,5),auto_size_buttons=True,auto_size_text=True,element_justification='left')
    while True:
        event, values = window_type.read()
        if event == "PREVIOUS":
            window_type.close()
            callback()
            break
        elif event == "data":
            name = "Water"
            window_type.close()
            break
        elif event == "data1":
            name = "Steam"
            window_type.close()
            break
        elif event == "data2":
            name = "Air"
            window_type.close()
            break
        elif event == "data3":
            name = "Tetraflouroethane-R134a"
            window_type.close()
            break
        elif event == "EXIT" or event == sg.WIN_CLOSED:
            break
    return name
    
def calculator_window():
    name = type_selector_window()
    if name=="Steam":
        name2="saturated steam"
        name1="superheated steam"
    else:
        name1=name
        name2=" saturated "+name
    x =False
    counter = "none"
    sg.theme('Dark Amber 5')
    pressure_units = [['Pa'],['Bar'],['mmHg'],['kg/m^2'],['atm'],['torr'],['lbf/inch^2']]
    temperature_units =[['celcius'], ['Kelvin'], ['Fahrenheit']]
    layout_2 = [[sg.Menu(menu_def, tearoff=False, pad=(200, 1))],
        [sg.Text('WELCOME', size=(40, 1), justification='center', font=("Algerian", 25))],
        [sg.Text("Calculation of Thermodynamic Property of " + name, auto_size_text= True, justification='left', font=("Algerian", 25))],
        [sg.Text("Calculate "+name1, auto_size_text=True,justification='center',font=("Algerian",20))],
        [sg.Text("Temperature", auto_size_text=True,justification='left',font=("Algerian",15)),sg.Input( size=(25, 1), font=("Algerian", 25),key="__IN__1"),sg.Drop(temperature_units,size=(10,1),default_value="select unit",auto_size_text=True,enable_events=True,font= ("Calibri", 20),key="units1")],
        [sg.Text("Pressure", auto_size_text=True,justification='left',font=("Algerian",15)),sg.Input( size=(25, 1), font=("Algerian", 25),key="__IN__2"),sg.Drop(pressure_units,size=(10,1),default_value="select unit",auto_size_text=True,enable_events=True,font= ("Calibri", 20),key="units2")],
        [sg.Button("CALCULATE",font=("Algerian",20),auto_size_button=True,enable_events=True,key="cal1")],
        [sg.Text("Calculate "+ name2, auto_size_text=True,justification='center',font=("Algerian",20))],
        [sg.Text("Temperature", auto_size_text=True,justification='left',font=("Algerian",15)),sg.Input( size=(25, 1), font=("Algerian", 25),key="__IN__3"),sg.Drop(temperature_units,size=(10,1),default_value="select unit",auto_size_text=True,enable_events=True,font= ("Calibri", 20),key="units3")],
        [sg.Text("OR", auto_size_text=True,justification='left',font=("Algerian",15))],
        [sg.Text("Pressure", auto_size_text=True,justification='left',font=("Algerian",15)),sg.Input( size=(25, 1), font=("Algerian", 25),key="__IN__4"),sg.Drop(pressure_units,size=(10,1),default_value="select unit",auto_size_text=True,enable_events=True,font= ("Calibri", 20),key="units4")],
        [sg.Button("CALCULATE",font=("Algerian",20),auto_size_button=True,enable_events=True,key="calc2")],
        [sg.Button("EXIT"),sg.Button("PREVIOUS")]]
    window_2 = sg.Window(title="CALCULATOR", layout = layout_2,resizable= True,right_click_menu=right_click_menu,default_button_element_size=(40,2),default_element_size=(40,5),auto_size_buttons=True,auto_size_text=True,element_justification='left')
    while True:
        event, values = window_2.read()
        print
        if event == "PREVIOUS":
            window_2.close()
            callback()
            break
        elif event == "cal1":
            value1 = values["__IN__1"]
            value2 = values["__IN__2"]
            unit1 = values["units1"]
            unit2= values["units2"]
            x = error_check(value1,value2,unit1,unit2)
            '''
            if x == True:
                calculation(d_type,value,unit,counter)
            else:
                pass
            '''
        elif event == "calc2":
            if values["__IN__3"] != "":
                value1 = values["__IN__3"]
                value2 = "0"
                unit1 = values["units3"]
                unit2 = "Randy Ortan"
                x = error_check(value1,value2,unit1,unit2)
                
            elif values["__IN__4"] != "":
                value2 = values["__IN__4"]
                value1 = "0"
                unit2= values["units4"]
                unit1 = "Underwear"
                x = error_check(value1,value2,unit1,unit2)
            
            elif values["__IN__3"] == "" and values["__IN__4"]=="":
                value2 = ""
                value1 = ""
                unit2= "select unit"
                unit1 = "select unit"   
                x = error_check(value1,value2,unit1,unit2)                
            '''
            x = error_check(d_type,value,unit,counter)
            if x == True:
                calculation(d_type,value,unit,counter)
            else:
                pass
            '''
        elif event == "EXIT" or event == sg.WIN_CLOSED:
            break


def about_window():
    sg.theme('Dark Amber 5')
    layout_3 = [[sg.Menu(menu_def, tearoff=False, pad=(200, 1))],
        [sg.Text('ABOUT THE DEVELOPERS', size=(40, 1), justification='center', font=("Algerian", 40))],
        [sg.Text('DHEERESH KUMAR CHATURVEDI', size=(25, 1), justification='left', font=("Algerian", 25))],
        [sg.Text('Then God said, Let Us make man in Our image, h.',font=("Arial", 10))],
        [sg.Text('SARANSH PANDEY', size=(25, 1), justification='left', font=("Algerian", 25))],
        [sg.Text('Then God said,abcbsabcsandsnlnsadkfnsadnfsanfnsadlfnsldfdsfjlsdnfla')],
        [sg.Button("EXIT"),sg.Button("PREVIOUS")]]
    window_3 = sg.Window(title="CALCULATOR", layout = layout_3,resizable= True,right_click_menu=right_click_menu,default_button_element_size=(40,2),default_element_size=(40,5),auto_size_buttons=True,auto_size_text=True,element_justification='center')
    while True:
        event, values = window_3.read()
        if event == "PREVIOUS":
            window_3.close()
            callback()
            break
        elif event == "EXIT" or event == sg.WIN_CLOSED:
            break
    window_3.close()

def error_check(value1,value2,unit1,unit2):
    if value1 == "" or value2 == "" or unit1 == "select unit" or unit2 =="select unit":
        if value1 == "": 
            sg.popup_cancel("Enter Data")
        elif value2 == "":
            sg.popup_cancel("Enter Data")   
        elif unit1 == "select unit":
            sg.popup_cancel("Select the unit")
        elif unit2 =="select unit":   
            sg.popup_cancel("Select the unit") 
    else:
        return True

def calculation(data_type,value,unit,type):
    comp1 =['R-134A']
    comp2 =['water']
    comp3= ['air']
    comp4= ['dheeresh']
    comp5=["saransh"]
    if data_type == comp1:
        str_file = "r1344a"
    elif data_type == comp2:
        str_file = "water"
    elif data_type == comp3:
        str_file ="air"
    elif data_type == comp4:
        str_file ="dheeresh"
    elif data_type == comp5:
        str_file ="saransh"
    xlsx_file = Path('/Users/DHEERESH/Desktop/calculator', str_file + ".xlsx")
    file = openpyxl.load_workbook(xlsx_file)
    sheet = file.active
    i=1
    k=0
    while i<=40:
        if sheet["A" + str(i)].value == value:
            print(value)
            print(sheet["A" + str(i)].value)
            print("mila gaya ")
            k=1
        else:
            print("dhoondh raha")
            print(value)
            print(sheet["A" + str(i)].value)
            print(i)
        if k==0:
            i=i+1
        else:
            break


def callback():
    initial_window()

if __name__=="__main__":
    initial_window()