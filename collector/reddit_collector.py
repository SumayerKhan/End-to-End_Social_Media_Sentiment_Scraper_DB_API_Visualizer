# This is the Reddit collector entry point
# Loads environment variables from .env at project root
# Creates a Reddit client using the credentials

import os

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError as e:
    raise ImportError(
        "python-dotenv is not installed to the current environment."
    ) from e


try:
    import praw
except ImportError as e:
    raise ImportError(
        "praw is not installed to the current environment"
    )

def get_reddit_client() -> "praw.Reddit":
    R_client_id = os.getenv("REDDIT_CLIENT_ID")
    R_client_secret = os.getenv("REDDIT_CLIENT_SECRET")
    R_user_agent = os.getenv("REDDIT_USER_AGENT")

    if not all([R_client_id,R_client_secret,R_user_agent]):
        raise RuntimeError(
            "Missing Reddit credentials. Ensure .env has all the credentials."
        )
    
    return praw.Reddit(
        client_id = R_client_id,
        client_secret = R_client_secret,
        user_agent = R_user_agent
        )


if __name__ == "__main__":
    reddit = get_reddit_client()
    # Sanity check
    try:
        print("Reddit client initialized. Read-only: ", reddit.read_only)
    except Exception as e:
        raise SystemExit(
            f"Failed to initialize Reddit client: {e}"
        )