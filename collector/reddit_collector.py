from __future__ import annotations
from typing import List,Dict,Any,Callable,Iterator
from reddit_config import get_reddit_client
from datetime import datetime
import json,os,time,random

reddit = get_reddit_client()

keyword = "iPhone 16"

def get_posts(
    keyword: str,
    subreddit: str = "all",
    limit: int = 1000,
    sort: str = "new",           # ("relevance", "hot", "top", "new", "comments")
    time_filter: str = "all"     # ("all", "day", "hour", "month", "week", "year")
) -> List[Dict[str,Any]]:
    
    results = reddit.subreddit(subreddit).search(
        query=keyword,
        limit=limit,
        sort=sort,
        time_filter=time_filter,
    )
    posts : List[Dict[str,Any]] = []

    for item in results:
        posts.append(
            {
                "id" : item.id,
                "keyword" : keyword,
                "title" : item.title or "",
                "selftext" : item.selftext or "",
                "subreddit" : getattr(item.subreddit, "display_name", ""),
                "subreddit": getattr(item.subreddit, "display_name", ""),
                "author": str(item.author) if getattr(item, "author", None) else "[deleted]",
                "score": int(getattr(item, "score", 0)),
                "num_comments": int(getattr(item, "num_comments", 0)),
                "created_utc": float(getattr(item, "created_utc", 0.0)),
                "url": getattr(item, "url", ""),
                "permalink": getattr(item, "permalink", ""),
                "fetched_at": datetime.utcnow().isoformat()
            }
        )
    
    return posts

posts = get_posts(keyword=keyword,limit=1000)

print(len(posts))

os.makedirs("data/raw", exist_ok=True)
filename = f"data/raw/{keyword.replace(' ', '_')}_posts.json"

with open(filename, "w", encoding="utf-8") as file:
    json.dump(posts, file, ensure_ascii=False, indent=2)