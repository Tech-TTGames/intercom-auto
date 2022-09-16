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
# Compatibility
We can confirm that our script and all dependecies are working on:
- Windows 10 1909 x64; Python 3.7.0 and newer
