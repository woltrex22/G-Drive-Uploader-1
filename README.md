[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/) [![Open Source Love svg1](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)

# Google Drive Uploader Bot
Here Is Live Version Of Bot  [Gdriveupme_bot](http://telegram.dog/Jdndjdjsjensiejebot)



# Update (30 May 2020)

- Teamdrive Support added 


`Teamdrive is not for users You have to hardcode it ,`
`Wait for V2 bot This Bot don't have active development I will add User Specfic Teamdrive option`

# How can You Add Teamdrive
-  Replace `TEAMDRIVE_FOLDER_ID` and `TEAMDRIVE_ID` in [creds.py](./creds.py) 


### What Is this ?

   A Telegram Bot Written In Python 

 ### what can it do ?

 It Can Upload Your Direct and Supported links into Google Drive.

 ### How Can We use It 
  - First authorise Bot Using `/auth` command Generate a Key and send it To bot .
  - Now You can Send Supported Link To Bot.

## Supported Links : 
 - Direct Link
 - Mega.nz Link
 - openload link (not avalibe anymore)
 - Dropbox Link

## Requirements
  - [Google Drive api Credential](https://console.cloud.google.com/apis/credentials) (Others type)  `Required`
  - Telegram Bot Token (Using BotFather)  `Required`
  - Openload ftp login and Key  `optional`
  - Mega Email and Password  `Optional`

 ` If You  wanna Change Openload Api and Mega Email Password You Can Change it From Given Path`
   - Mega => Plugins > TEXT.py
   - Openload  => Plugins > dlopenload.py

## Setup Your Own Bot
```
1. Create Your  [Google Drive api Credential](https://console.cloud.google.com/apis/credentials) (other type) and Download  Its json

2. Paste it In Bot Root Directroy  and Rename it "client_secrets.json"

3. Replace Your Bot Token in  [creds.py file](./creds.py)

4. Your Bot is Ready to Host. 
```
### Deploy to Heroku
<p><a href="https://heroku.com/deploy"> <img src="https://www.herokucdn.com/deploy/button.svg" alt="Deploy to Heroku" /></a></p>

### Credits
  - [Aryanvikash](https://github.com/aryanvikash/Google-Drive-Uploader) - Forked this repo
