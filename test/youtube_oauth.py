# token.pickle stores the user's credentials from previously successful logins
#!/usr/bin/env python3
import google.auth
import google.auth.transport.requests
#import google.oauth2.credentials
from googleapiclient.errors import HttpError
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import pickle
import pprint
import sys
import json
import os

home_directory = os.path.expanduser( '~' )
print( home_directory )
token_file = home_directory + "/yb/token.pickle"
client_secrets_file = home_directory + "/yb/client_secrets.json"
token_pickle_file = home_directory + "/yb/token.pickle"
credentials = None
if os.path.exists(token_file):
    print('Loading Credentials From File...')
    with open(token_file, 'rb') as token:
        credentials = pickle.load(token)





# If there are no valid credentials available, then either refresh the token or log in.
if not credentials or not credentials.valid:
    if credentials and credentials.expired and credentials.refresh_token:
        print('Refreshing Access Token...')
        credentials.refresh(Request())
    else:
        print('Fetching New Tokens...')
        flow = InstalledAppFlow.from_client_secrets_file(
            client_secrets_file,
            scopes=[
                'https://www.googleapis.com/auth/youtube.readonly',
                'https://www.googleapis.com/auth/youtube.channel-memberships.creator',
                'https://www.googleapis.com/auth/youtube.force-ssl',
                'https://www.googleapis.com/auth/youtube'
            ]
        )

        flow.run_local_server(port=8080, prompt='consent',
                              authorization_prompt_message='')
        credentials = flow.credentials

        # Save the credentials for the next run
        with open(token_pickle_file, 'wb') as f:
            print('Saving Credentials for Future Use...')
            pickle.dump(credentials, f)

youtube = build("youtube","v3", credentials=credentials)

if 1:
    request = youtube.playlistItems().list(
        part="status",
        playlistId="PLN5nQTzxyimOMcvGHBcmWzfAv9ROFow6_",
        maxResults=2
    )
    response = request.execute()
    pprint.pprint(response)

    request = youtube.playlistItems().list(
        part="status",
        playlistId="LL3vyXU6vIGI3s_I63Mk_chA",
        maxResults=2
    )
    response = request.execute()

    pprint.pprint(response)
if 0:
    try:
        print("get playlists ")
        request = youtube.playlists().list(
            part="snippet,contentDetails",
            mine=True
        )
        response = request.execute()
        pprint.pprint(response)
    except Exception as ex:
        print("get playlists exception")
        pprint.pprint(ex)
    pprint.pprint(response)

if True:
    try:
        print("get members ")
        request = youtube.members().list(
            part="snippet"
        )
        response = request.execute()
        pprint.pprint(response)
    except Exception as ex:
        print("get members exception")
        pprint.pprint(ex)

if True:
    try:
        print("get member_ships_level")
        request = youtube.membershipsLevels().list(
            part="snippet,id"
        )
        response = request.execute()
        pprint.pprint(response)
    except Exception as ex:
        print("get member_ships_level exception")
        pprint.pprint(ex)