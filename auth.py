from google.oauth2 import service_account
from google.auth.transport.requests import AuthorizedSession
import  os

# Define the required scopes
scopes = [
  "https://www.googleapis.com/auth/userinfo.email",
  "https://www.googleapis.com/auth/firebase.database"
]

print(os.environ.get('serviceAccountKey'))

# Authenticate a credential with the service account
credentials = service_account.Credentials.from_service_account_file(
    os.environ.get('serviceAccountKey'), scopes=scopes)

# Use the credentials object to authenticate a Requests session.
authed_session = AuthorizedSession(credentials)
response = authed_session.get(
    "https://maen-try-firebase-default-rtdb.firebaseio.com/example")

# Or, use the token directly, as described in the "Authenticate with an
# access token" section below. (not recommended)
# request = google.auth.transport.requests.Request()
# credentials.refresh(request)
# access_token = credentials.token
