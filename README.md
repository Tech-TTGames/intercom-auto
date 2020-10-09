# intercom-auto
An program to automate music playing using Google Forms.
# Setup
First install VLC Media Player ensuring it is contained on PATH.
Clone the git and open it's location in command line.
Enter following lines to install required packages.
`pip install -r requirements.txt`
Open "config.json" file and edit it - choose auth file name and your spreadsheet name.
Open https://console.cloud.google.com/ and create a new project.
Open the API & Services tab. Enable both Google Sheets API and Google Drive API.
Then open the IAM & Admin tab further opening Service Acounts tab.
Press the create service account button and follow instructions. You don't need to give it any permissons.
After creating open the three dots menu and click "create key" generate it using the json-type file option.
Save it in the cloned repository under the name specified before.
Open your google forms and create a form named as in config ensuring that the first question is about the link.
Open the responses tab and click the google spreadsheat button creating your spreadsheet with answers.
Open the spreadsheet and click share and add the Service Account's mail to the list.
Open the internauto.py file and replace the 'Enter Sheet Name Here' Placeholder with the name of your sheet.
