import os
import sys
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, parent_dir)

# Import modules
from utils.auth.appauth import authexchange, authreq, authuserProfile

app = FastAPI()
# ----------------------
# Authentication
# ----------------------
@app.get("/")
def root():
    return {"version": 1}

@app.get("/auth")
def authenticate():
    res = authreq("https://accounts.google.com/o/oauth2/v2/auth")
    return RedirectResponse(url=res["requesturl"])

@app.get("/verify")
def verify(code: str):
    token = authexchange(code)
    user = authuserProfile(token["accesstoken"])
    return user
