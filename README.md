# Whatsapp Python Bot
![whatsapp](https://twilio-cms-prod.s3.amazonaws.com/images/uDU_MWBJHg-z8j5Jzymi03iLb6dQC_iUsBF1qtRxPfzyPx.width-808.jpg)

A simple python bot which I like.

This will run only when your pc/laptop is turned on
To run this 24/7 refer to my second repo on which I am still working

## BOT ACCOUNT

Make your account here https://www.twilio.com/

### Linking the bot account to your whatsapp

1. Go to this link https://www.twilio.com/console/sms/whatsapp/learn and save the number that is shown there.

![code and number](https://i.ibb.co/VtwSPQq/first.png)

2. Send the code displayed there on this number from your whatsapp number 
3. Follow the further steps and when you reach the last page of the steps save the site for future steps

Now you have to move on to coding part



Download this as zip folder or just use clone the repo

Clone Repo:
```
git clone https://github.com/pro-mitanshu/Whatsapp-bot-python.git
cd Whatsapp-bot-python
````
## Required Things

### Python modules
You have install these modules using pip
```
flask
twilio
requests
```

You can also easily install them by opening command prompt and writing pip install -r requirements.txt

### NGROK
Download ngrok from here https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-windows-amd64.zip 
Exctract that ngrok.exe file and place it in the whatsapp-bot-python folder among other files

Your directly should look like this now

![directory](https://i.ibb.co/L14DSqC/dir.png)


## Running the code

In command promt you just have to run python main.py.(Every time you open the command prompt, open it in that same folder as of whatsapp bot)

![main.py](https://i.ibb.co/NFvjZ3t/black.png)

You will ge a local host url which only you can access.
You can convert it by using ngrok which you have already installed

Open one more command prompt without quiting the previous one.
In command prompt type ngrok http 5000 (mostly it is 5000. It is the last 4 digit of local host url also called port number)
![ngrok](https://i.ibb.co/nn48Fcq/ngrokf.jpg)

Copy the link given by it and go to the site which I told above to save for future.
In the box (WHEN A MESSAGE COMES IN) box write that url and put /sms at back.

![box](https://i.ibb.co/8mQRNRk/box.png)

The last step is to click on save.
After clicking save your procedure is completed and it is the time to test the bot by sending messages to it

# 
I have done absolute basics and if you want some more commands to work with, refer extra.py

#
IF THIS HELPS YOU DO STAR IT



