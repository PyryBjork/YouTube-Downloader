import PySimpleGUI as sg
import pytube

type = ''
itag_list = ('1080p, 60fps', '720p, 60fps', '720p, 30fps', '480p, 30fps')
sg.theme('Topanga')
itag = 0


layout = [ [sg.Text('URL: ', size=(10, 1)), sg.InputText(size=(60, 2), key='URL')],
            [sg.Text('itag: ', size=(10, 1)), sg.InputText(size=(60, 2), key='ITAG')],
            [sg.Button('Download', tooltip='Start the download'), sg.Button('List available itags'), sg.Button('Clear')],
            [sg.Output(size=(70, 20))]  ]

window = sg.Window('Youtube Downloader', layout)



def Download(url, itag):
    video = pytube.YouTube(url)
    stream = video.streams.get_by_itag(itag)
    print('Ladataan...')
    stream.download()
    print('Valmis')


while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Close': # if user closes window or clicks cancel
        break
    if event == 'Clear':
        window['URL']('')
        window['ITAG']('')
    if event == 'List available itags':
        print('Printing itags...')
        video = pytube.YouTube(values['URL'])
        for stream in video.streams:
            h = str(stream).split('codec')
            g = h[0][9:]
            g = g[:-2]
            print(g)
    if event == 'Download':
        itag = int(values['ITAG'])
        url = values['URL']
        Download(url, itag)
