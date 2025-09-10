# README.md

# GitHub Activity CLI Tool

A simple Python command-line tool to fetch and display a GitHub user's recent public activity, including commits, issues, pull requests, stars, and more.

This project is based on the 
This project is based on the [roadmap.sh GitHub User Activity](https://roadmap.sh/projects/github-user-activity).


---

## Features

- Fetch recent GitHub activity for a given username
- Display activity in a human-readable format:
  ```
  - Pushed 3 commits to marin-mohanadas/Task-Tracker
  - Opened a new issue in marin-mohanadas/GitHub-User-Activity
  - Starred marin-mohanadas/tic-tac-toe
  ```
- Supports:
  - Push events
  - Issues
  - Pull requests
  - Issue comments
  - Repository creation
  - Stars (WatchEvent)

---

## Requirements

- Python 3.7+
- `requests` library

Install dependencies:

```bash
pip install requests
```

Also, include the requirements file for pip installation:
```bash
pip install -r requirements.txt
```

---

## Usage

Run the script and type your GitHub username:

```bash
python app.py
```

Example input:

```
github-activity marin-mohanadas
```

Example output:

```
Output:
- Pushed 2 commits to marin-mohanadas/Task-Tracker
- Opened a new issue in marin-mohanadas/GitHub-User-Activity
- Starred marin-mohanadas/tic-tac-toe
```

---

## Project Structure

```
github-activity/
│
├── app.py           # Entry point (CLI)
├── api.py           # GitHub API interaction
├── events.py        # Event formatting utility
├── requirements.txt # Python dependencies
├── README.md        # Project documentation
```

---

## Notes

- Only fetches **public events** visible via GitHub API
- GitHub API is rate-limited: 60 requests/hour for unauthenticated users
- For higher limits, use a **personal access token** and extend the API class

---

## License

MIT License

