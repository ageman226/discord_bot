import os
import requests
import json
import pandas as pd
from dotenv import load_dotenv

load_dotenv()

# Important Parameters
APIHEADER = os.getenv("ANIMEHEADER")
KEY = os.getenv("KEY")
BOTTOKEN = os.getenv("BOTTOKEN")
params = {APIHEADER: KEY}

urlStart = "https://myanimelist.net/anime/"
apiStartAnime = "https://api.myanimelist.net/v2/anime"


# Searches anime using a query.
def searchAnime(query, limit=1, fields="synopsis"):
    """Searches the anime through myanimelist and returns based on the limit and t he fields

    Args:
        query (str): The string to query the search
        limit (int, optional): The amount of results to show. Defaults to 1.
        fields (str, optional): Fields to be included in the return. Defaults to "synopsis".

    Returns:
        JSON: Returns the data as JSON
    """
    # Requests using the API
    x = requests.get(
        f"{apiStartAnime}?q={query}&limit={limit}&fields={fields}", headers=params)
    # Gets the request and changes it to a json readable string
    jsonResult = x.json()
    data = jsonResult["data"]
    # Gets everything in the data of the json
    animeList = []
    for newData in data:
        id = newData["node"]["id"]
        title = newData["node"]["title"]
        image = newData["node"]["main_picture"]["large"]
        synopsis = newData["node"]["synopsis"]
        animeList.append({"id": id, "title": title, "image": image, "synopsis": synopsis})
    return animeList
    # Use Pandas to change the json into a table.
    # df = pd.json_normalize(dataD)
    # df = df.rename(columns={"node.id": "id",  "node.title": "Title",
    #                "node.main_picture.medium": "Medium Picture", "node.main_picture.large": "Large Picture"})
    # return json.loads(df.to_json(orient="records"))


def getAnimeDetails(anime_id, fields="synopsis"):
    x = requests.get(
        f"{apiStartAnime}/{anime_id}?fields={fields}", headers=params)
    jsonResult = x.json()
    return jsonResult


def getAnimeRankingsTop(ranking_type="airing", amount=10, field="title"):
    x = requests.get(
        f"{apiStartAnime}/ranking?ranking_type={ranking_type}&limit={amount}&fields={field}", headers=params)
    jsonData = x.json()
    rankings = []
    for data in jsonData["data"]:
        id = data["node"]["id"]
        image = data["node"]["main_picture"]["medium"]
        title = data["node"]["title"]
        rank = data["ranking"]["rank"]
        rankings.append({"id": id, "rank": rank, "title": title, "image": image})
    return rankings


def getAnimeRankingsGenre(ranking_type="airing", limit=5, field="title,genres"):
    x = requests.get(
        f"{apiStartAnime}/ranking?ranking_type={ranking_type}&limit={limit}&fields={field}", headers=params)
    jsonData = x.json()
    newData = jsonData["data"]
    genre = ""
    rankings = []
    for data in newData:
        id = data["node"]["id"]
        title = data["node"]["title"]
        rank = data["ranking"]["rank"]
        for genres in data["node"]["genres"]:
            genre += genres["name"] + " "
        rankings.append(
            {"id": id, "rank": rank, "title": title, "genres": genre})
        genre = ""
    return rankings
