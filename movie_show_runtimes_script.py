import requests
import json 

# API key
api_key = None
# TMDB Base API URL
tmdb_url = "https://api.themoviedb.org/3"
# Searh Endpoint (See Docs for /discover and /find)
search_endpt = '/search'
# Searching for a Movie or TV show (includes suggested searches)
movie_suggestions = '/movie?'
show_suggestions = '/tv?'
# Querying Specific Movie or Show by ID
movie_id_query = '/movie/'
show_id_query = '/tv/'

def search_movie(movie_str):
    req_url = tmdb_url + search_endpt + movie_suggestions + "api_key=" + api_key + "&query=" + movie_str.replace(" ", "+")
    resp = requests.get(req_url)
    resp_content = json.loads(resp.text)
    return resp_content["results"][0]["id"]

def movie_runtime_by_id(movie_id):
    req_url2 = tmdb_url + movie_id_query + str(movie_id) + "?api_key=" + api_key
    resp2 = requests.get(req_url2)
    resp2_content = json.loads(resp2.text)
    print(resp2_content["original_title"] + "'s runtime is " + str(resp2_content["runtime"]) + " minutes.")


def search_show(show_str):
    req_url = tmdb_url + search_endpt + show_suggestions + "api_key=" + api_key + "&query=" + show_str.replace(" ", "+")
    resp = requests.get(req_url)
    resp_content = json.loads(resp.text)
    return resp_content["results"][0]["id"]

def show_runtime_by_id(show_id):
    req_url = tmdb_url + show_id_query + str(show_id) + "?api_key=" + api_key
    resp = requests.get(req_url)
    resp_content = json.loads(resp.text)
    show_runtime = resp_content["number_of_episodes"] * sum(resp_content["episode_run_time"])
    print(resp_content["name"] + "'s runtime is " + str(show_runtime) + " minutes.")

movie_runtime_by_id(search_movie("Rise of Skywalker"))
show_runtime_by_id(search_show("Westworld"))


# Requirements from TMDB if we want API access

# You shall use the TMDb logo to identify your use of the TMDb APIs.
# You shall place the following notice prominently on your application: "This product uses the TMDb API but is not endorsed or certified by TMDb."
# Any use of the TMDb logo in your application shall be less prominent than the logo or mark that primarily describes the application 
# and your use of the TMDb logo shall not imply any endorsement by TMDb.