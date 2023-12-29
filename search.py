from googleapiclient.discovery import build

api_key = 'AIzaSyAyh0L1ib80S1ezQs-onDhAsvH1ZDDUjoI'

channel_search = input("Please you please enter the channel that you would like to look up?")

def get_channel_id(name):
    youtube = build('youtube', 'v3', developerKey=api_key)
    request = youtube.channels().list(
        part = 'contentDetails',
        forUsername = name
    )
    response = request.execute()

    channel_id = response['items'][0]['id']

    return channel_id

