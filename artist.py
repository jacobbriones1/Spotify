from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import numpy as np
import ast
import networkx as nx
import matplotlib.pyplot as plt


client_id = '6c1147793d114a87b17d1a6b4e40bf2a'
client_secret = 'a74e9be4fda4451ca43cca0c0d267027'

client_credentials_manager = SpotifyClientCredentials(client_id, client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


class Artist():
    def getArtistID(self, artistName):
        results = sp.search(q=artistName, type="artist")
        artistID = results['artists']['items'][0]['id']
        return artistID


    def __init__(self, artistName):
        self.artistName = artistName
        self.artistID = self.getArtistID(artistName)
        self.relArtistsIDs = self.getRelatedArtists(self.artistID)[0]
        self.relArtistsNames = self.getRelatedArtists(self.artistID)[1]
        self.nEdges = len(self.relArtistsNames)


    def getAlbumIDs(userID):
        names = np.array([])
        IDs = np.array([])
        results = sp.artist_albums(userID, album_type='album')
        albums = results['items']
        while results['next']:
            results = sp.next(results)
            albums.extend(results['items'])

        for album in albums:
            if names.__contains__(album['name']) is False:
                IDs = np.append(IDs, album['uri'])
                names = np.append(names, album['name'])

        return IDs, names

    def getAlbumTracks(albumID):
        results = sp.album_tracks(albumID)
        albumTrackIDs = []
        albumTrackNames = []
        tracks = results['items']
        while results['next']:
            results = sp.next(results)
            tracks.extend(results['items'])

        for track in tracks:

            albumTrackIDs = np.append(albumTrackIDs, track['id'])
            albumTrackNames = np.append(albumTrackNames, track['name'])
        print(albumTrackNames)

        return albumTrackIDs, albumTrackNames

    def getTrackFeatures(trackID):
        meta = sp.track(trackID)
        features = sp.audio_features(trackID)

        # meta
        name = meta['name']
        album = meta['album']['name']
        artist = meta['album']['artists'][0]['name']
        release_date = meta['album']['release_date']
        length = meta['duration_ms']
        popularity = meta['popularity']

        # features
        acousticness = features[0]['acousticness']
        danceability = features[0]['danceability']
        energy = features[0]['energy']
        instrumentalness = features[0]['instrumentalness']
        liveness = features[0]['liveness']
        loudness = features[0]['loudness']
        speechiness = features[0]['speechiness']
        tempo = features[0]['tempo']
        time_signature = features[0]['time_signature']

        track = [name, album, artist, release_date, length, popularity,
                 danceability, acousticness, danceability, energy,
                 instrumentalness, liveness, loudness,speechiness,
                 tempo, time_signature]

        return track

    def getRelatedArtists(self, artistID):
        relatedArtists = sp.artist_related_artists(artistID)
        relatedArtistID = []
        relatedArtistName = []

        for i in range(len(relatedArtists['artists'])):
            relatedArtistID = np.append(relatedArtistID,
                                        relatedArtists['artists'][i]['id'])
            relatedArtistName = np.append(relatedArtistName,
                                          relatedArtists['artists'][i]['name'])
        self.relArtistsID = relatedArtistID
        self.relArtistsNames = relatedArtistName

        return relatedArtistID, relatedArtistName

    def getVertices(self):
        nodes=np.array([])
        nodes = [self.relArtistsNames[i] for i in range(len(self.relArtistsNames))]
        nodes = np.append(nodes,self.artistName)
        return nodes

    def getEdges(self):
        
        edges = [(self.artistName,self.relArtistsNames[i]) 
                 for i in range(len(self.relArtistsNames))]
            
            
        return edges





