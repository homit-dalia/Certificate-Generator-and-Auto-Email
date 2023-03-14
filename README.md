# Certificate-Generator-and-Auto-Email

Please note :
  1. The code has not yet been surrounded with try catch statements in all fields. The GUI might crash on bad input.
  
  2. There are a few features that are shown but not yet implemented:
    1. Different Font style
    2. Add image to certificate
    
What does "column" mean?
=> It is the column number in your csv file under which your name and email data is stored.
  for eg, 
          userData.csv contains > age,college,event,name,email
          name = 4
          email = 5

What does "X", "Y", "Size", "Color" mean?
=> X and Y denotes the coordinates where your respective field will be placed. Currently, the name will be added "from" the coordinates specified, and not "on" the coordinates specified, i.e. "Hello World" at X = 20 and Y = 10 will set the 'H' in Hello world to (20,10) and not the center of the string to (20,10).
   Color should be specified in Hex and it is not necessary to put "#" in the field.
   
How to generate sender password for auto email?
Password shows up as wrong.
=> Steps to generate password for Gmail account. (other email providers might have similar steps, please look for a tutorial on Youtube)
      1. Login to your account
      2. Go to https://myaccount.google.com/
      3. Go to "App Passwords" and not "Passwords". If you cannot find App Passwords, go to step Extra 1 and continue.
      4. Click on "Select App" > "Other" and name it whatever you want, and then do the same for "Select Device" if asked.
      5. Click on "Generate".
      6. You will be shown a 16 digit password.
         This is your password that you will enter in the Certificate Generator and Auto Email. Store the password somewhere as it can be deleted later but never be recovered. Do not share it with anyone. If you forget/misplace the password, you should delete it and generate a new one.
      
      Extra 1. Your web link looks like this => https://myaccount.google.com/u/1/?tab=kk.
               Replace the link to https://myaccount.google.com/u/1/apppasswords
                          
