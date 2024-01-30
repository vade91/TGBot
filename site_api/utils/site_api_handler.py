from typing import Dict

import requests


def _make_response(method: str, url: str, headers: Dict, params: Dict,
                   timeout: int, success=200):
    response = requests.request(
        method,
        url,
        headers=headers,
        params=params,
        timeout=timeout
    )

    status_code = response.status_code

    if status_code == success:
        return response

    return status_code


def _get_movie_data_by_id(method: str, url: str, headers: Dict, params: Dict, movie_id: int,
                          timeout: int, func=_make_response):
    url = "{0}top{1}".format(url, movie_id)

    response = func(method, url, headers=headers, params=params, timeout=timeout)

    return response


class SiteApiInterface():

    @staticmethod
    def get_movie_data_by_id():
        return _get_movie_data_by_id



if __name__ == "__main__":
    _make_response()
    _get_movie_data_by_id()

    SiteApiInterface()
