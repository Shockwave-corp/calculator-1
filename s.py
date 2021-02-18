import PySimpleGUI as sg

names = ['Roberta', 'Kylie']

layout = [[sg.Listbox(names, size=(20, 4), key='_LIST_')],
          [sg.InputOptionMenu(names, size=(20, 4), key='_LIST_')]]

window = sg.Window('').Layout(layout).Finalize()

new_values = ['Bill', 'Jeff']
window.Element('_LIST_').Update(new_values)

while True:
    event, values = window.Read()
    if event is None or event == 'Exit':
        break

window.Close()