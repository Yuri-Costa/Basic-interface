from PySimpleGUI import PySimpleGUI as sg

#layout
sg.theme('Reddit')
layout=[
    [sg.Text("Usuario"), sg.Input(key='Usuario', size=(20,1))],
    [sg.Text('Senha'), sg.Input(key='senha', password_char='*', size=(20,1))],
    [sg.Checkbox('Deseja salvar o Login?')],
    [sg.Button('Entrar')]
]

#Janela
janela = sg.Window('Tela de login', layout)


#leitura dos eventos
while True :
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos== 'Entrar':
        if valores['Usuario'] == 'Yuri' and valores ['senha']=='123456': 
            print('Seja Muito Bem Vindo!')
           

