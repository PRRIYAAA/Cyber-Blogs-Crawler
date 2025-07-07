from flask import Flask, render_template, jsonify
import praw
import datetime as dt

app = Flask(__name__)

# Reddit API credentials
reddit = praw.Reddit(
    client_id="rtXOfLssM8eIxYLsBZDmrg",
    client_secret="IgYACIeWAZa_bntF9lScHpcZzg6-Rw",
    user_agent="Scrapping_App"
)

# Subreddit and keywords
subreddit = reddit.subreddit("cybersecurity")

keywords = [
    "cybersecurity", "malware", "phishing", "ransomware", "data breach",
    "vulnerability", "exploit", "threat intelligence", "incident response",
    "penetration testing", "network security", "firewall",
    "encryption", "authentication", "access control",
    "zero trust", "compliance", "risk management", "APT", "OSINT",
    "CVE", "patch management", "cloud security", "API security",
    "IoT security", "cryptography", "bug bounty", "forensics",
    "red team", "blue team", "DevSecOps", "DLP", "insider threat",
    "social engineering", "zero-day", "DNS security", "SSL/TLS"
]

@app.route('/')
def home():
    return render_template('dashboard.html')

@app.route('/fetch_posts')

def fetch_posts():
    

    posts = []
    count = 0
    # Increase limit to 50 for more posts
    for idx, submission in enumerate(subreddit.new(limit=1500), start=1):
        title = submission.title.lower()
        found_keywords = [k for k in keywords if k in title]
        if found_keywords:
            count += 1
            posts.append({
                'title': f"{count}. {submission.title}",
                'url': submission.url,
                'score': submission.score,
                'keywords': found_keywords
            })

    return jsonify({'posts': posts})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)

