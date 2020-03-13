ABOUT

This is a search engine with only pages from the ICS domain.
This project was created using Python, Flask, and React.

LIBRARIES USED

LXML:
    Used to get the etree root of a webpage

SnowballStemmer
    Used as a stemmer for terms

Heapq
    Used to efficiently sort our webpage results based on our rank function

networkx
    Used to create a digraph of links used in page rank


CONFIGURATION

How to run the program:

Step 1:
    Go into the directory of the project, then call "export FLASK_APP=App.py",
    then call "flask run" in order to start the index server.

Step 2:
    Go into the directory of the React project, and install any dependencies that might be missing,
    ex. Bootstrap by running "npm install". Then, run "npm start" in terminal, which will turn on the web app
    of the search engine.

Step 3:
    This will run on localhost:3000, so if it does not open up a tab of the application, go in the url and type
    localhost:3000 to run the program.

Step 4:
    At this point both servers should be running, the user will now be able to search any query on the search engine.


FILES

App.py:
    This is the Flask server which gives an API call to the front-end, which can display the results of the queries.

Html_Reader.py:

    Read_file():
        This function parses through an etree root object which is able to retrieve the text from a webpage.
        We tokenize this page, and add the word and posting to our inverted index, accordingly.

    read_master_for_id():
        This function opens the master inverted index, and adds a tfidf score for each posting, and
        an idf for each word.

Indexer.py:

    get_all_files():
        This function takes the index in memory and writes to partial inverted indexes,
        creating a new partial inverted index once it reaches 1000 pages.

merge.py:

    merge_total():
        This function merges all of the partial indexes into one master index.txt file.

Pagerank.py:

    This file goes through all the DEV files and gives a pagerank for each url/doc_id.

Posting.py:

    This is a module with a class Posting, that has the following attributes: doc_id, tfidf, and importance, and a __str__ method

Query.py:

    retrieve_query():
        This function accepts a query as a parameter and parses through the master index file and returns the top results,
        based on the query.

    rank():
        This function returns a score based on a combination of pagerank, cosine score, and where the query appears in the
        webpage, ex. Title, Bold, Link etc.

Url.py:

    This module parses through the json object in the DEV folder, returning an etree.root object to parse through in
    Html_reader.py.


