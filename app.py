from api import get_user_activity


def main():
    print("Enter command:")
    print("github-activity <username>")

    input_username = input().strip()

    if input_username.startswith("github-activity"):
        username = input_username.replace("github-activity", "").strip()

        if not username or len(username) == 0:
            print("Please provide a GitHub username.")
            return

        get_user_activity(username)


if __name__ == "__main__":
    main()
