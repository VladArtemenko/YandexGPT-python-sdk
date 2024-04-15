from src.yandex_gpt.iam_getter import YandexApiGetterIAM, YandexApiGetterIAMCache
import os


oauth_token = os.getenv('YANDEX_OAUTH')


def test_getter_iam():
    getter_iam = YandexApiGetterIAM(oauth_token)
    token = getter_iam.get_iam_token()
    assert type(token) is str


def test_getter_iam_cached():
    getter_iam = YandexApiGetterIAMCache(oauth_token)
    token = getter_iam.get_iam_token()
    assert type(token) is str
