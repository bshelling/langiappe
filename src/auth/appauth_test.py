from appauth import authreq,authUrl,exchangeUrl

"""
    The url is incorrect 403 Status
"""
def test_authreq_status403():
    status_code = 403
    url = "http://test.com"
    assert authreq(url)['status'] == status_code


"""
    The url is incorrect 403 Status
"""
def test_authreq_status200():
    status_code = 200
    url = "https://accounts.google.com/o/oauth2/v2/auth"
    assert authreq(url)['status'] == status_code

"""
    Structure the auth url correctly
"""
def test_authUrl():

    url = "https://test.com"
    clientId = "clientId"
    redirect = ["https://test.com"]
    scope = "code"
    accessType = "testingType"


    assert authUrl(url,clientId,redirect,scope,accessType) == f"{url}?client_id={clientId}&redirect_uri={redirect[0]}&response_type=code&scope={scope}&accessType={accessType}"

"""
    Exchange code for token
"""
def test_authexUrl():
    url = "https://oauth2.googleapis.com/token"
    clientId = "clientId"
    clientSecret = "clientSecret"
    code = "clientcode"
    redirectUrl = ["https://test.com"]

    assert exchangeUrl(url,clientId,clientSecret,redirectUrl,code) == f"{url}?code={code}&client_id={clientId}&client_secret={clientSecret}&redirect_uri={redirectUrl[0]}&grant_type=authorization_code"
