from config_data import config

from site_api.utils.site_api_handler import SiteApiInterface

headers = {
    "X-RapidAPI-Key": config.RAPID_API_KEY,
    "X-RapidAPI-Host": "imdb-top-100-movies.p.rapidapi.com"
}

params = {"fragment": "true", "json": "true"}

url = r'https://imdb-top-100-movies.p.rapidapi.com/'

api_host = "imdb-top-100-movies.p.rapidapi.com"

site_api = SiteApiInterface()

if __name__ == '__main__':
    site_api()
