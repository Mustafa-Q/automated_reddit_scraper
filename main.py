# emails
import os
import pickle

# Gmail API utils
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# for encoding/decoding messages in base64
from base64 import urlsafe_b64decode, urlsafe_b64encode

# for dealing with attachement MIME types
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# for showing when the email was sent 
import datetime

# for scraping Reddit
import praw

# for executing the code at a certain time everyday 
import schedule
import time

# defining "now" which is when the email is going to be sent, which is needed for the subject
now = datetime.datetime.now()

# request perms to send email
SCOPES = ['https://mail.google.com/']
our_email = 'YOUR-EMAIL'

# reads and saves the credentials.json to the token.pickle once your Google account has been authenticated
# saving the token is necessary in order to not have to authenticate the account again after running the code a second time
def gmail_authenticate():
    creds = None
    # the file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first time
    if os.path.exists("token.pickle"):
        with open("token.pickle", "rb") as token:
            creds = pickle.load(token)
    # if there are no (valid) credentials availablle, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # save the credentials for the next run
        with open("token.pickle", "wb") as token:
            pickle.dump(creds, token)
    return build('gmail', 'v1', credentials=creds)

# get the Gmail API service
service = gmail_authenticate()

# connecting our Reddit account by creating a praw instance, in this case being a read-only instance 
reddit = praw.Reddit(client_id= "YOUR-REDDIT-CLIENT-ID", client_secret= "YOUR-REDDIT-CLIENT-SECRET", user_agent= "YOUR-USER-AGENT-NAME")

# we're looking for the hot posts on r/all
subreddit = reddit.subreddit("all")
scraped_posts = subreddit.hot()

# scraping the posts' titles and inserted URLs and copying the info onto a text file
def scraping():
    f = open("posts.txt", 'w', encoding="utf-8")
    for post in scraped_posts:
        f.write(str(post.title) + "\n")
        f.write(str(post.url) + "\n")
        f.write("-----\n")
scraping()

# customizing the email's subject such that it matches the date it's sent
subject = "Top News Stories from Reddit" + " " + str(now.day) + "-" + str(now.month) + "-" + str(now.year)

# copy the info from the text file
a = open("posts.txt", 'r', encoding="utf-8")
info = a.read()

# takes the message parameters and builds the email accordingly
def build_message(destination, obj, body):
    message = MIMEText(body)
    message['to'] = destination
    message['from'] = our_email
    message['subject'] = obj
    return {'raw': urlsafe_b64encode(message.as_bytes()).decode()}

# using the Google Mail API to send a message with the build_message() parameters
def send_message(service, destination, obj, body):
    return service.users().messages().send(
      userId="me",
      body=build_message(destination, obj, body)
    ).execute()

# scheduling the email to be sent everyday at 9pm
schedule.every().day.at("17:00").do(send_message, service, "YOUR EMAIL", subject, info)
