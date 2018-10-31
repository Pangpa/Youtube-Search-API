import argparse
import json
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


# Set DEVELOPER_KEY to the API key value from the APIs & auth > Registered apps
DEVELOPER_KEY = 'AIzaSyCy2L3acHIt0OUQw6NB-F1n8wDYPRA3wbY'
YOUTUBE_API_SERVICE_NAME = 'youtube'
YOUTUBE_API_VERSION = 'v3'

def youtube_search(query,max_results = 25):
  youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)

  # Call the search.list method to retrieve results matching the specified
  # query term.
  search_response = youtube.search().list(
    q=query,
    part='id,snippet',
    maxResults=max_results
  ).execute()
 
  videos = []
  channels = []
  playlists = []
  #print (json.dumps(search_response, sort_keys=True, indent=4))
  # Add each result to the appropriate list, and then display the lists of
  # matching videos, channels, and playlists.
  #for result in search_response.get('items',[]):
      #print(result['id'])
      #break
  
  for search_result in search_response.get('items', []):
    if search_result['id']['kind'] == 'youtube#video':
      videos.append('%s (%s)' % (search_result['snippet']['title'],
                                 search_result['id']['videoId']))
    elif search_result['id']['kind'] == 'youtube#channel':
      channels.append('%s (%s)' % (search_result['snippet']['title'],
                                   search_result['id']['channelId']))
    elif search_result['id']['kind'] == 'youtube#playlist':
      playlists.append('%s (%s)' % (search_result['snippet']['title'],
                                    search_result['id']['playlistId']))

  d = {} 
  for result in search_response.get('items',[]):
      d[result['snippet']['title']] = [result['snippet']['publishedAt'], result['snippet']['thumbnails']['medium'],result['id']['videoId']]
  #print(d)
  return d
  #print ('Videos:\n', videos)
  #print ('Channels:\n', channels)
  #print ('Playlists:\n', playlists)

