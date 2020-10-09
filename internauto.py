import gspread
from oauth2client.service_account import ServiceAccountCredentials
import time
import vlc
import datetime
import pafy
from gtts import gTTS
print("Automated Intercom Radio by Tomasz Gębarski is licensed under CC BY-ND 4.0. \n To view a copy of this license, visit https://creativecommons.org/licenses/by-nd/4.0")
#Main Programmer Tomasz Gębarski
#Idea Jan Sikora
now = datetime.datetime.now()
cu = now.hour*60 + now.minute + 1
SPREADSHEET = "Enter Sheet Name Here" #Edit this line
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name('auth.json', scope)
gc = gspread.authorize(credentials)
print("The following sheets are available")
for sheet in gc.openall():
    print("{} - {}".format(sheet.title, sheet.id))
workbook = gc.open(SPREADSHEET)
sheet = workbook.sheet1
i = 1
link = "bootup"
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
    c = player.get_length() / 1000
    now = datetime.datetime.now()
    cu = now.hour*60 + now.minute + 1 + ( now.second / 60 )
    cen = c/60 + cu
    pom = 1
    q = 1
    if c <= 420:
        while(q == 1):
            print(now," ",cu," ",cen)
            now = datetime.datetime.now()
            cu = now.hour*60 + now.minute + 1 + ( now.second / 60)
            if cu == 460 or cu == 510 or cu == 565 or cu == 620 or cu == 675 or cu == 730 or cu == 795 or cu == 860 or cu == 915 or cu == 965:
                if pom == 1:
                    player.pause()
                    print("Pause")
                    platts.set_media(ttsLM)
                    platts.play()
                    pom = 2
                    cen = cen + 45
            elif cu == 450 or cu == 505 or cu == 555 or cu == 610 or cu == 665 or cu == 720 or cu == 775 or cu == 840 or cu == 905 or cu == 960:
                if pom == 2:
                    platts.set_media(ttsPM)
                    platts.play()
                    player.play()
                    print("Play")
                    pom = 1
            if cu >= cen:
                q = 0
                print("Song Ended")
    else:
        print("Song Longer than 7 min")
        player.stop()

    del(media)

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
    print("Loop Completed")
