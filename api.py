import requests
from events import Events


def get_user_activity(username: str):
    url = f"https://api.github.com/users/{username}/events"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        if not data:
            print(f"No recent activity found for {username}.")
            return

        print(f"Recent activity for {username}:\nOutput:")

        for item in data:
            # formatter = Events(item.get("type"))
            message = Events(item).format_event()
            print("-", message)

    else:
        try:
            error_message = response.json().get("message", "")
        except Exception:
            error_message = ""
        print(f"Error {response.status_code}: {error_message}")
