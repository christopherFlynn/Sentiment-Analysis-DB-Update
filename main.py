from sentiment_analysis.analyzer import analyze_subreddit
import json
import os

def save_results(sentiments, post_data, path="sentiment_data/sentiment_data.json"):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w') as f:
        json.dump({"sentiments": sentiments, "posts": post_data}, f)

def main():
    sentiments, post_data = analyze_subreddit()
    save_results(sentiments, post_data)
    print(f"Analysis complete! {sentiments}")

if __name__ == "__main__":
    main()