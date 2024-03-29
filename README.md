# Certificate-Generator-and-Auto-Email

## Q. How to use this application?
  You can create a .exe from the python file through tools available on the internet to skip all the steps. The generated .exe is frequently flagged as a "Trojan" and won't run on most windows computers. Thus it is advised to follow these steps: 

  1. Download and install Python - https://www.python.org/downloads/
  2. Open CMD / Terminal as administrator at the directory this application is downloaded.
  3. Type - *pip install -r requirements.txt*. If this does not work, type - *pip install tk fpdf email smtplib*.
  4. Open *GUICertiGen.py* and run if you have an IDE installed. Otherwise, run - *python GUICertiGen.py*. If it does not work, run - *python3 GUICertiGen.py*
  5. Repeat step 4 any time you want to use the application again.

Please note :
  1. The code has not yet been surrounded with try catch statements in all fields. The GUI might crash on bad input.
  
  2. There are a few features that are shown but not yet implemented:
    1. Different Font style
    2. Add image to certificate
    
## Q. What does "column" mean?
=> It is the column number in your csv file under which your name and email data is stored.
  for eg, 
  userData.csv contains > age,college,event,name,email
  Here, name = 4 and email = 5

## Q. What does "X", "Y", "Size", "Color" mean?
=> X and Y denotes the coordinates where your respective field will be placed. Currently, the name will be added "from" the coordinates specified, and not "on" the coordinates specified, i.e. "Hello World" at X = 20 and Y = 10 will set the 'H' in Hello world to (20,10) and not the center of the string to (20,10).
   Color should be specified in Hex and it is not necessary to put "#" in the field.
   
## Q. How to generate sender password for auto email?
> => Steps to generate password for Gmail account. (other email providers might have similar steps, please look for a tutorial on Youtube)
>>      1. Login to your account
>>      2. Go to https://myaccount.google.com/
>>      3. Go to "App Passwords" and not "Passwords". If you cannot find App Passwords, go to step Extra 1 and continue.
>>      4. Click on "Select App" > "Other" and name it whatever you want, and then do the same for "Select Device" if asked.
>>      5. Click on "Generate".
>>      6. You will be shown a 16 digit password.
>>         -> This is your password that you will enter in the Certificate Generator and Auto Email. 
>>         -> Store the password somewhere as it can be deleted later but never recovered. Do not share it with anyone. 
>>         -> If you forget/misplace the password, you should delete it and generate a new one.
      
>>      Extra 1. Your web link looks like this => https://myaccount.google.com/u/1/?tab=kk.
>>               Replace the link to https://myaccount.google.com/u/1/apppasswords
                          
