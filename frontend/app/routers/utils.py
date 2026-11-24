

def set_cookies(response, tokens: dict):
    if 'access_token' in tokens:
        response.set_cookie(key='access_token', value=tokens['access_token'], expires=15 * 60)
        response.set_cookie(key='refresh_token', value=tokens['refresh_token'], expires=60 * 60)

def delete_cookies(response):
    response.delete_cookie('access_token')
    response.delete_cookie('refresh_token')
