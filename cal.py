#CALCULATOR
import PySimpleGUI as sg
menu_def = [['&File', ['&Open', '&Save', '---', 'Properties', 'E&xit'  ]],['&Edit', ['Paste', ['Special', 'Normal',], 'Undo'],],['&Help', '&About...']]
right_click_menu = ['Unused', ['Right', '!&Click', '&Menu', 'E&xit', 'Properties']]
def initial_window():
    sg.theme('Dark Amber 5')
    layout = [[sg.Menu(menu_def, tearoff=False, pad=(200, 1))],
            [sg.Text('WELCOME', size=(40, 1), justification='center', font=("Algerian", 40))],
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




def calculator_window():
    kt =False
    kp =False
    sg.theme('Dark Amber 5')
    refrigerant_list = [['R-134A'], ['water'], ['steam'],['dheeresh'], ['saransh']]
    pressure_units = [['Pa'],['Bar'],['mmHg'],['kg/m^2'],['atm'],['torr'],['lbf/inch^2']]
    temperature_units =[['celcius'], ['Kelvin'], ['Fahrenheit']]
    layout_2 = [[sg.Menu(menu_def, tearoff=False, pad=(200, 1))],
        [sg.Text('WELCOME', size=(40, 1), justification='center', font=("Algerian", 25))],
        [sg.Drop(refrigerant_list,size=(20,2),auto_size_text=True,enable_events=True,default_value="select the refrigerant",font= ("Calibri", 20),)],
        [sg.Checkbox('Pressure',size=(20,2),auto_size_text=True,enable_events=True,default=False,key ='Pressure'),sg.Checkbox('Temperature',size=(20,2),auto_size_text=True,enable_events=True,default=False,key='Temperature')],
        [sg.Input(default_text = "enter the values", size=(25, 1), font=("Algerian", 25),key="__IN__"),sg.Drop(temperature_units,size=(10,1),auto_size_text=True,enable_events=True,font= ("Calibri", 20),visible=False,key="units")],
        [sg.Button("EXIT"),sg.Button("PREVIOUS")]]
    window_2 = sg.Window(title="CALCULATOR", layout = layout_2,resizable= True,right_click_menu=right_click_menu,default_button_element_size=(40,2),default_element_size=(40,5),auto_size_buttons=True,auto_size_text=True,element_justification='left')
    while True:
        event, values = window_2.read()
        if event == "PREVIOUS":
            window_2.close()
            callback()
            break
        elif event =="Temperature":
            layout_2 = [[sg.Menu(menu_def, tearoff=False, pad=(200, 1))],
            [sg.Text('WELCOME', size=(40, 1), justification='center', font=("Algerian", 25))],
            [sg.Drop(refrigerant_list,size=(20,2),auto_size_text=True,enable_events=True,default_value="select the refrigerant",font= ("Calibri", 20),)],
            [sg.Checkbox('Pressure',size=(20,2),auto_size_text=True,enable_events=True,default=False,key ='Pressure'),sg.Checkbox('Temperature',size=(20,2),auto_size_text=True,enable_events=True,default=True,key='Temperature')],
            [sg.Input(default_text = "enter the values", size=(25, 1), font=("Algerian", 25),key="__IN__"),sg.Drop(temperature_units,size=(10,1),auto_size_text=True,enable_events=True,font= ("Calibri", 20),visible=True,key="units")],
            [sg.Button("EXIT"),sg.Button("PREVIOUS")]]
            window_2 = sg.Window(title="CALCULATOR", layout = layout_2,resizable= True,right_click_menu=right_click_menu,default_button_element_size=(40,2),default_element_size=(40,5),auto_size_buttons=True,auto_size_text=True,element_justification='left')
        elif event =="Pressure":
            window_2['Temperature'].Update(False)
            layout_2 = [[sg.Menu(menu_def, tearoff=False, pad=(200, 1))],
            [sg.Text('WELCOME', size=(40, 1), justification='center', font=("Algerian", 25))],
            [sg.Drop(refrigerant_list,size=(20,2),auto_size_text=True,enable_events=True,default_value="select the refrigerant",font= ("Calibri", 20),)],
            [sg.Checkbox('Pressure',size=(20,2),auto_size_text=True,enable_events=True,default=True,key ='Pressure'),sg.Checkbox('Temperature',size=(20,2),auto_size_text=True,enable_events=True,default=False,key='Temperature')],
            [sg.Input(default_text = "enter the values", size=(25, 1), font=("Algerian", 25),key="__IN__"),sg.Drop(pressure_units,size=(10,1),auto_size_text=True,enable_events=True,font= ("Calibri", 20),visible=True,key="units")],
            [sg.Button("EXIT"),sg.Button("PREVIOUS")]]
            window_2 = sg.Window(title="CALCULATOR", layout = layout_2,resizable= True,right_click_menu=right_click_menu,default_button_element_size=(40,2),default_element_size=(40,5),auto_size_buttons=True,auto_size_text=True,element_justification='left')

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
        if event == "EXIT" or event == sg.WIN_CLOSED:
            break
    window.close()
def callback():
    initial_window()




if __name__=="__main__":
    initial_window()
