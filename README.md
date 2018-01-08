# Spotify taste visualization
![alt text](https://user-images.githubusercontent.com/18704685/34679733-278631ce-f497-11e7-9ccc-0d6d54f3ced8.PNG)
## Introduction
Create a simple dashboard to observe the change in music taste

This project leverages the API provided by spotify.
I am not allowed to copy/distribute any data nor able to share my developer credentials.

Whoever whants to use or enhance this code can apply for credentials here: https://developer.spotify.com


## Running
### Changes in main
Change credentials in the dataImport script to your own:


    credentials = {"client_id": **?**,
                   "client_secret":**?*}

change the username to the user of interest

    username = **?**

### Execution of the programm

open the command window, change the directory to the location of the project
and use:

    bokeh serve spotify-taste-visualization
 
Then navigate to the URL in your browser:

    http://localhost:5006/spotify-taste-visualization

A new spotify login page will open and ask for your permission.
Login and and allow your application the access to your data.

You will get redirected to a new url. Copy and paste the url into your command window.
The application is now running. Refresh the local ``http://localhost:5006/spotify-taste-visualization`` and start using the dashboard.

# Explanation
## Basic functionality

The dashboard visualizes the music library of the user. It consists of two main graphs. One is a scatter-plot of multiple song features with changing point sizes depending on a third feature.

The user can decide between two data collection methods:
1) All saved songs by a user  ``getData(credentials, username, saved = True)`` (default)
2) All songs that are at least in one playlist ``getData(credentials, username, saved = False)``

Some potential selections are:  
**x/y:**
- danceability
- loudness
- accusticness
- instrumentalness
- energy

**size**:
- None
- loudness
- duration in ms

## Advanced functionality
Both graphs are connected to the same data. Therefore, selection datapoints in one graph highlights and selects the connected datapoints in the other graph. This allowes for a more specific inspection, depending on the periode of interest.

![alt text](https://user-images.githubusercontent.com/18704685/34679732-276eaa40-f497-11e7-9019-3c4af382c3c0.PNG)

Additionally certain patterns might be confusing or some features are not explanatory. Therefore, this dashboard allowes to hover over a specific data-point to optain additional information to what song this point corresponds.

![alt text](https://user-images.githubusercontent.com/18704685/34679735-279ea31c-f497-11e7-9f9b-7ac1ad88020b.PNG)

## TODO
Potential future enhancements:
- Adding filter possibilities
- Adding aggregated selection summary
- Adding data table of selection
- Adding differing aggregation time frames
