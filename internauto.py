import gspread
from oauth2client.service_account import ServiceAccountCredentials
import time
import vlc
import datetime
import pafy
from gtts import gTTS
import json
import progressbar as pb

print("Automated Intercom Radio by Tomasz Gębarski & Jan Przebor is licensed under CC BY-SA 4.0. To view a copy of this license, visit https://creativecommons.org/licenses/by-sa/4.0")
#Main Programmer Tomasz Gębarski
#Idea Jan Sikora
with open('config.json') as config_file:
    config = json.load(config_file)
now = datetime.datetime.now()
cu = now.hour*60 + now.minute + 1
SPREADSHEET = config["sheet-name"]
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name(config["auth-file"], scope)
gc = gspread.authorize(credentials)
print("The following sheets are available:")
for sheet in gc.openall():
    print("{} - {}".format(sheet.title, sheet.id))
workbook = gc.open(SPREADSHEET)
sheet = workbook.sheet1
i = 1
link = "bootup"
if config["tts-on"]:
    vlc_tts = vlc.Instance()
    platts = vlc_tts.media_player_new()
    ttsP = gTTS(text="Początek Przerwy",lang='pl')
    ttsP.save("Pts.mp3")
    ttsPM = vlc_tts.media_new("Pts.mp3")
    ttsL = gTTS(text="Początek Lekcji",lang='pl')
    ttsL.save("Lts.mp3")
    ttsLM = vlc_tts.media_new("Lts.mp3")
vlc_instance = vlc.Instance()
player = vlc_instance.media_player_new()

def Sound(sound):
    media = vlc_instance.media_new(sound)
    player.set_media(media)
    player.play()
    time.sleep(1.5)
    c = int(player.get_length() // 1000)
    widgets = [' [', pb.Timer(), '] ', 
    pb.Bar(marker='█'),' (', 
    time.strftime('%H:%M:%S',time.gmtime(c)), ') ', 
    ] 
    bar = pb.ProgressBar(max_value=c,widgets=widgets).start()
    now = datetime.datetime.now()
    cu = now.hour*60 + now.minute + 1 + ( now.second / 60 )
    cen = c/60 + cu
    pom = 1
    if c <= config["max-length"] or config["max-length"] == 0:
        for o in bar((z for z in range(1,c))):
            now = datetime.datetime.now()
            cu = now.hour*60 + now.minute + 1 + ( now.second / 60)
            if cu in config["end-hours"]:
                if pom == 1:
                    player.pause()
                    print("Paused.")
                    if config["tts-on"]:
                        platts.set_media(ttsLM)
                        platts.play()
                    pom = 2
                    cen = cen + 45
            elif cu in config["start-hours"]:
                if pom == 2:
                    if config["tts-on"]:
                        platts.set_media(ttsPM)
                        platts.play()
                    player.play()
                    print("Started playing.")
                    pom = 1
            if cu >= cen:
                break
                print("Song Ended.")
            time.sleep(1)
    else:
        print("Requested song is Longer than ",config["max_length"],"s")
        player.stop()
    del(media)
    del(widgets)

while(True):
    if link != "":
        i += 1
    workbook = gc.open(SPREADSHEET)
    sheet = workbook.sheet1
    link = sheet.cell(i,2).value
    if link != "":
                aust = pafy.new(link)
                bas = aust.getbestaudio()
                url = bas.url
                print(aust.title)
                Sound(url)

