# automated_reddit_scraper
A script that automatically scrapes and emails you the day's top Reddit posts. Getting this script to function requires some setting up, as detailed below. 

## Setting up the Gmail API 
Install these libraries via Command Prompt:
```
$ pip3 install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
```
We need a token to connect to Gmail's API, which we can get from the Google APIs' dashboard.

Enable the Gmail API [here.](https://console.cloud.google.com/apis/library/gmail.googleapis.com)

Click the Create Credentials button:
![Screenshot 2022-08-31 193058](https://user-images.githubusercontent.com/62267192/187802559-e36b7458-0f2f-4c08-a702-3225dc9cd4a1.png)

Select the OAuth client ID from the dropdown menu, and you'll then be sent to this page: 
![Screenshot 2022-09-03 135019](https://user-images.githubusercontent.com/62267192/188282501-948da64f-7859-4ed8-b143-dc159a9e62e0.png)

Click the "Configure Consent Screen" button, select the "External" option, and hit the "Create" button. You should then see an app registration page. For the purposes of this script, you only need to fill out the app name (with whatever you want), the user support email (with whatever email you're creating the API with), and the developer contact information (best to go with the same email). On the next page (and the one after that), just hit the "Save and Continue" button. Keep in mind that all you've done thus far is create the consent screen. 

Head back to the "Credentials" page, click the Create Credentials button, and select the OAuth client ID from the dropdown menu. Your application type is the "Desktop app." From there you should see something like this: 

![Screenshot 2022-09-03 135954](https://user-images.githubusercontent.com/62267192/188282814-dfe77491-7363-4eb4-931a-3f0f9c434516.png)

Click on DOWNLOAD JSON and, if necessary, rename the file to credentials.json and put it in the current directory of the project.

## Setting up the Reddit API
Running the following in Command Prompt:
```
pip install praw
```

We then need to create a new Reddit app [here](https://www.reddit.com/prefs/apps). Click on "are you a developer? create an app…"
![image](https://user-images.githubusercontent.com/62267192/188283104-33b1afbe-65d7-40ef-9d21-e4dde6dd4cd9.png)

A form like this will pop up:
![Screenshot 2022-09-03 141030](https://user-images.githubusercontent.com/62267192/188283160-c4a74aee-249e-4da5-9fb8-41de0ab08424.png)

Feel free to fill the details as you wish, but make sure to put "http://localhost:8080" in the "redirect uri" box. Click on “create app”. This will give you access to the client_id, secret, and user_agent - all of which are necessary to implement the API:

![image](https://user-images.githubusercontent.com/62267192/188283256-35f4c274-f7ee-44da-8dc1-6c058dac3784.png)


