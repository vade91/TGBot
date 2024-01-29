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
    url = "{0}/{1}/date".format(url, movie_id)

    response = func(method, url, headers=headers, params=params, timeout=timeout)

    return response


def _get_math_fact(method: str, url: str, headers: Dict, params: Dict,
                   number: int, timeout: int, func=_make_response):
    url = "{0}/{1}/math".format(url, number)

    response = func(method, url, headers=headers, params=params,
                    timeout=timeout)

    return response


class SiteApiInterface():

    @staticmethod
    def get_movie_data_by_id():
        return _get_movie_data_by_id

    @staticmethod
    def get_top_100_movies_list():
        return _get_math_fact

    @staticmethod
    def get_series_data_by_id():
        return _get_math_fact

    @staticmethod
    def get_top_100_series_list():
        return _get_math_fact


if __name__ == "__main__":
    _make_response()
    _get_math_fact()
    _get_date_fact()

    SiteApiInterface()
