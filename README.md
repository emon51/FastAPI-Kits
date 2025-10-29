# FastAPI-Kits

## If we get an error while to activate virtualenv
- When we type: ``` ... myenv\Scripts\activate ``` 
**Error:**
...\myenv\Scripts\activate cannot be loaded because running scripts is disabled on this system. For more information, see about_Execution_Policies at https:/go.microsoft.com/fwlink/?LinkID=135170. At line:1 char:1 + myenv/Scripts/activate + CategoryInfo : SecurityError: (:) [], PSSecurityException + FullyQualifiedErrorId : UnauthorizedAccess

- Solution: ```Set-ExecutionPolicy RemoteSigned -Scope CurrentUser```

# What is an HTTP Header?
An HTTP header is a part of an HTTP request or response that carries additional information about the request or response as a dictionary.
- For Example
```
{
  "host": "example.com",
  "user-agent": "Mozilla/5.0",
  "accept": "application/json",
  "authorization": "Bearer abc123token",
  "content-type": "application/json",
  "origin": "https://myapp.com",
  "referer": "https://google.com",
  "cookie": "sessionid=xyz",
  "accept-language": "en-US,en;q=0.9"
}

```
Authorization: tells who is sending (authentication info)
Content-Type: tells the format of data (json)

- Show All HTTP Headers
```
from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/show-headers")
async def show_headers(request: Request):
    # Get all headers as a dictionary-like object
    all_headers = request.headers

    # Convert to a normal dictionary (for easier reading)
    headers_dict = dict(all_headers)

    # Print in the terminal (optional)
    print(headers_dict)

    # Return them as JSON response
    return {"headers": headers_dict}
```
# Synchronous Vs Asynchronous (programming execution styles):
- Synchronous means tasks run one after another - each must finish before the next starts.
- Asynchronous means tasks run together/concurrently - while one waits, others keep working.
- In short: Sync = blocking, Async = non-blocking.
- Sync and async: these tell how the server runs your code.
