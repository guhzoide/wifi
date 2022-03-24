import PySimpleGUI as sg
import subprocess

def main():
    dados = subprocess.check_output(["netsh", "wlan", "show", "profiles"], encoding="cp860")
    
    sg.theme("Lightgray1")
    menu = [
        [sg.Multiline(dados, size=(95,35))],
        [sg.Text('Digite o nome do wi-fi como esta a cima'), sg.Input(key='nome', size=(25,1))],
        [sg.Button('Próximo')]
    ]

    win = sg.Window("Menu", menu, element_justification='c')
    e, v = win.read()

    if e == sg.WINDOW_CLOSED:
        win.close()
    
    elif e == 'Próximo':
        wifi = v['nome'] 
        info = subprocess.check_output(["netsh", "wlan", "show", "profile", wifi, "key", "=", "clear"], encoding="cp860")
        for line in info.split("\n"):
            if "Conteúdo da Chave" in line:
                posi = line.find(":")
                senha = line[posi+2:]
                sg.popup_ok(wifi + " = " + senha)
                win.close()
                main()
                
    elif e == 'sair':
        quest = sg.popup_yes_no("Deseja sair?")
        if quest == 'Yes':
            win.close()
        else:
            win.close()
            main()
main()    
