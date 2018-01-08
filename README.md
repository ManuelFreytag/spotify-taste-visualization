Create a simple stocks dashboard to observe the change in music taste

This project leverages the API provided by spotify.
I do not own any rights to the data nor am i allowed to 

To use any of the tools provided in this repository you will need to apply for a 

Also

Running
=======

note: Running this tools requires spotify developer credentials
You can apply for these credentials here: https://developer.spotify.com

Changes in main
---------------
Change credentials in the dataImport script to your own:


    credentials = {"client_id": **?**,
                   "client_secret":**?*}

change the username to the user of interest

    username = **?**

Execution of the programm
-------------------------
open the command window, change the directory to the location of the project
and use:

     bokeh serve spotify-taste-visualization
 
Then navigate to the URL in your browser:

     http://localhost:5006/spotify-taste-visualization

A new spotify log-in page will open and ask for your permissione
login and and allow your application the access to your data

you will get redirected to a new url
Copy and paste the url into your command window

you will get 

Choose stocks to compare in the drop down widgets, and make selections
on the plots to update the summary and histograms accordingly.
.. note::
    Running this example requires downloading sample data. See
    the included `README`_ for more information.

Explanation
=======

Explanation how to use it

Either saved songs or all songs at least in one playlist

Hover over song
Select x, y or circle size
Select points to see special time periode highlighted

TODO
====
Potential future enhancements:
- Adding filter possibilities
- Adding aggregated selection summary
- Adding data table of selection
- Adding differing aggregation time frames
