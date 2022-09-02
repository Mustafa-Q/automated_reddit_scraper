# automated_reddit_scraper
A script that automatically scrapes and emails you the day's top Reddit posts. Getting this script to function requires some setting up, as detailed below. 

## Setting up the Gmail API 
Install these libraries via Command Prompt:
```
$ pip3 install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
```
We need a token to connect to Gmail's API, which we can get from the Google APIs' dashboard.

Enable the Gmail API [here.](https://console.cloud.google.com/apis/library/gmail.googleapis.com)

Head to the Create Credentials button:
![Screenshot 2022-08-31 193058](https://user-images.githubusercontent.com/62267192/187802559-e36b7458-0f2f-4c08-a702-3225dc9cd4a1.png)

Select the OAuth client ID from the dropdown menu, and you'll then be asked  to this page: 
![create-oauth-client-id](https://user-images.githubusercontent.com/62267192/187802796-c33c3c5e-5f4b-4e94-a4c8-d8a6c2941be2.png)

Select Desktop App and you should see something like this:

