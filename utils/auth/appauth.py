import requests as r
import logging
import json

def readCreds(filename:str):
    with open(filename,"r") as file:
       f = json.load(file)
    return {
        "clientId": f['web']['client_id'],
        "secret": f['web']['client_secret'],
        "redirect":f['web']['redirect_uris'],
        "tokenuri": f['web']['token_uri']
    }

def authUrl(url: str, clientId: str, redirectUrl: list, scope: str, accessType: str):
    return f"{url}?client_id={clientId}&redirect_uri={redirectUrl[0]}&response_type=code&scope={scope}&accessType={accessType}"

def exchangeUrl(url: str, clientId: str, clientSecret: str, redirectUrl: list, code: str):
    return f"{url}?code={code}&client_id={clientId}&client_secret={clientSecret}&redirect_uri={redirectUrl[0]}&grant_type=authorization_code"


# Authorization Url
def authreq(url:str) -> dict:
   try:
       f = readCreds("clientcreds.json")
       clientId = f['clientId']
       redirectUrl = f['redirect']
       # https://developers.google.com/identity/protocols/oauth2/scopes#oauth2
       scope = "https://www.googleapis.com/auth/userinfo.email%20https://www.googleapis.com/auth/userinfo.profile"
       accessType = "online"
       resp = r.get(authUrl(url,clientId,redirectUrl,scope,accessType))

       print(authUrl(url,clientId,redirectUrl,scope,accessType))
       return {
            "status": resp.status_code,
            "requesturl": authUrl(url,clientId,redirectUrl,scope,accessType)
       }

   except Exception as err:
       logging.fatal(f"AuthReqError: {err}")
       return {
           "status": 400
       }

# Token Exchange
def authexchange(code: str):
    f = readCreds("clientcreds.json")
    clientId = f['clientId']
    clientSecret = f['secret']
    redirectUrl = f['redirect']
    xresp = r.post(exchangeUrl("https://oauth2.googleapis.com/token",clientId,clientSecret,redirectUrl,code))
    accesstoken = xresp.json()
    return {
         "status": 200,
         "accesstoken": accesstoken.get("access_token")
    }

# User Profile
def authuserProfile(token: str):
    userinfo = r.get("https://www.googleapis.com/oauth2/v2/userinfo",headers={
        "Authorization": f"Bearer {token}"
    })
    return userinfo.json()
