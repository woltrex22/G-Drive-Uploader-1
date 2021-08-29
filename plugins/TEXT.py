

# Here is Your Drive Folder Name You can Replace it with Your Desire name(Optional)
drive_folder_name = "GDriveUploaderBot"


# Enter Your Mega email And Pass (Required)
MEGA_EMAIL = "empty@gmail.com"
MEGA_PASSWORD = "empty@gmaail.com"


START = """Hi {}
 - I am Drive Uploader Bot .
 - Please Authorise To use me .
 - By using /auth
        
 - For more info /help
 - Third-Party Website
 - Support Added /update
 - For Bot Updates

<b>You want your own bot?</b>
Watch this <a href="https://www.google.com">Tutorial</a> Video
        """
        
HELP = """   <b>AUTHORISE BOT</b> 
 - Use  /auth Command Generate
 - Your Google Drive Token And 
 - Send It To Bot 
 
<b>You Wanna Change Your Login 
Account ?</b> \n
 - You Can Use /revoke 
   command   
         
<b>What I Can Do With This Bot? </b>
 - You Can Upload Any Internet
   Files On Your google
   Drive Account.

<b> Links Supported By Bot</b>
 - Direct Links 
 - Openload links 
   [Max Speed 500 KBps 🙁]
 - Dropbox links 
 - Mega links

<b>You want your own bot?</b>
Watch this <a href="https://www.google.com">Tutorial</a> Video
              
        """
DP_DOWNLOAD = "Dropbox Link !! Downloading Started ..."
OL_DOWNLOAD = "Openload Link !! Downloading Started ..."
PROCESSING = "Processing Your Request ...!!"
DOWN_TWO = True
DOWNLOAD = "Downloading Started ..."
DOWN_MEGA = "Downloading Started..."
DOWN_COMPLETE = "Downloading complete !!"
NOT_AUTH = "You Are Not Authorised To Using this Bot \n\n Please Authorise Me Using /auth"
REVOKE_FAIL = "You Are Already UnAuthorised \n. Please Use /auth To Authorise"
AUTH_SUCC = "Authorised Successfully  !! \n\n Now Send me A direct Link 🙂"
ALREADY_AUTH = "You Are Already Authorised ! \n\n Wanna Change Drive Account? \n\n Use /revoke \n\nYou want your own bot? \n Watch this <b><a href="">Tutorial</a></b> Video "
AUTH_URL = '''
Generate And Copy Your
Google Drive Token
Send It To Me
<a href ="{}">Generate Token</a>
'''
UPLOADING = "Download Complete !! \n Uploading Your file"
REVOKE_TOK = " Your Token is Revoked Successfully !! \n\n Use /auth To Re-Authorise Your Drive Acc. "
# DOWN_PATH = "Downloads\\" #windows path
DOWN_PATH = "Downloads/"  # Linux path
DOWNLOAD_URL = "Your File Uploaded Successfully \n\n <b>Filename</b> : {} \n\n <b> Size</b> : {} MB \n\n <b>Download</b> {}"
AUTH_ERROR = """
AUTH Error !! 
Please  Send Me a  valid Token 
           or 
Re - Authorise Me /auth
For more info /help
"""
OPENLOAD = True
DROPBOX = True
MEGA = True


UPDATE = """ <b> Update  on  27.07.2019</b>
 - MEGA LINK added
 - Error Handling Improved
         """
