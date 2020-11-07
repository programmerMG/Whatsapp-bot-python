# Whatsapp Python Bot
![alt text](https://botsociety.io/blog/wp-content/uploads/2018/09/image-1-e1554854547722.png)
A simple python bot for personal use which I like.

You can refer to my youtube video for more information about it (still not uploaded but will do in some time)


## BOT ACCOUNT

Make your account here https://www.twilio.com/

### Linking the bot account to your whatsapp

1. Go to this link https://www.twilio.com/console/sms/whatsapp/learn and save the number that is shown there.
2. Send the code diplayed there on this number from your whatsapp number 
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

## Running the code

In command promt you just have to run python main.py.

You will ge a local host url which only u can access.
You can convert it by using ngrok which you have already installed

Open one more command prompt without quiting the previous one.
In command prompt type ngrok http 5000 (mostly it is 5000. You can type yours .It is the last 4 digit of local host url also called port number)
Copy the link given by it and go to the site which I told above to save for future.
In the box (WHEN A MESSAGE COMES IN) box write that url and put /sms at back.
![alt text](https://lh4.googleusercontent.com/9BG6Mh-oFziIPwaaKi8ssePvb6m7A09JDy1hZnQ2aISDeteurqwU6ldoxjbb7jUWIvohTDr2FsX8pFZlBjrL=w1366-h645)

The last step is to click on save.
After clicking save your procedure is completed and it is the time to test the bot by sending messages to it







