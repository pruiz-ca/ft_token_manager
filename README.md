# Installation
Install dependencies with `pipenv install`

Run with `pipenv run python3 server.py`

# Routes
`/token/access` -> exchange the webflow auth code for a token

`/token/refresh` -> exchange a refresh_token for a token

# Returns
The same object returned by intra
```
{
"access_token":"42804d1f2480c240f94d8f24b45b318e4bf42e742f0c06a42c6f4242787af42d",
"token_type":"bearer",
"expires_in":7200,
"scope":"public",
"created_at":1443451918
}
```
