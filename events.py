class Events:

    def __init__(self, event):
        self.event = event

    def format_event(self):
        event_type = self.event.get("type")
        repo_name = self.event.get("repo", {}).get("name", "Unknown Repo")
        payload = self.event.get("payload", {})

        if event_type == "PushEvent":
            commits = payload.get("commits", [])
            count = len(commits)
            return f"Pushed {count} commits to {repo_name}"

        elif event_type == "IssuesEvent":
            action = payload.get("action")
            return f"{action.capitalize()} an issue in {repo_name}"

        elif event_type == "PullRequestEvent":
            action = payload.get("action")
            return f"{action.capitalize()} a pull request in {repo_name}"

        elif event_type == "IssueCommentEvent":
            return f"Commented on an issue in {repo_name}"

        elif event_type == "CreateEvent":
            ref_type = payload.get("ref_type", "repository")
            return f"Created a new {ref_type} in {repo_name}"

        elif event_type == "WatchEvent":
            return f"Starred {repo_name}"

        else:
            return f"{event_type} on {repo_name}"
