import PySimpleGUI as sg

layout = [
    [sg.Text("Insira o nome do anime:"), sg.Input(key='INPUT'),
     sg.Combo([5, 10, 20, 30], default_value=10)],
    [sg.Ok('Enviar')],
    [sg.Text("", size=(0, 1), key='OUTPUT')]
]

window = sg.Window("AnimeAPP", layout=layout, size=(600, 300), resizable=True)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break


def request_anime(genre: str, name: str, perPage: int, page: int):
    pass
