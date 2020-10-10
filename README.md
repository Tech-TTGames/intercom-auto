# intercom-auto
An program to automate music playing using Google Forms.
# Setup
First install VLC Media Player ensuring it is contained on PATH.<br/>
Clone the git and open it's location in command line.<br/>
Enter following lines to install required packages:<br/>
`pip install -r requirements.txt`<br/>
Open "config.json" file and edit it - choose auth file name and your spreadsheet name.<br/>
Open https://console.cloud.google.com/ and create a new project.<br/>
Open the API & Services tab. Enable both Google Sheets API and Google Drive API.<br/>
Then open the IAM & Admin tab further opening Service Acounts tab.<br/>
Press the create service account button and follow instructions. You don't need to give it any permissons.<br/>
After creating open the three dots menu and click "create key" generate it using the json-type file option.<br/>
Save it in the cloned repository under the name specified before.<br/>
Open your google forms and create a form named as in config ensuring that the first question is about the link.<br/>
Open the responses tab and click the google spreadsheat button creating your spreadsheet with answers.<br/>
Open the spreadsheet and click share and add the Service Account's mail to the list.<br/>
Open the internauto.py file and replace the 'Enter Sheet Name Here' Placeholder with the name of your sheet.<br/>
<p xmlns:dct="http://purl.org/dc/terms/" xmlns:cc="http://creativecommons.org/ns#" class="license-text"><a rel="cc:attributionURL" property="dct:title" href="github.com/Tech-TTGames/intercom-auto">Automated Intercom Radio</a> by <span property="cc:attributionName">Tomasz Gębarski & Jan Przebor</span> is licensed under <a rel="license" href="https://creativecommons.org/licenses/by-sa/4.0">CC BY-SA 4.0<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1" /><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1" /><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/sa.svg?ref=chooser-v1" /></a></p>
