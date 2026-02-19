name: Fetch YouTube Videos

on:
  schedule:
    - cron: '0 */2 * * *'  # every 2 hours
  workflow_dispatch:         # lets you run it manually too

jobs:
  fetch:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3

      - name: Set up Python
        uses: actions/setup-python@v4
        with:
          python-version: '3.11'

      - name: Install dependencies
        run: pip install requests

      - name: Run fetch script
        env:
          YOUTUBE_API_KEY: ${{ secrets.YOUTUBE_API_KEY }}
        run: python fetch_videos.py

      - name: Commit updated data
        run: |
          git config user.name "github-actions"
          git config user.email "actions@github.com"
          git add data/videos.json
          git diff --staged --quiet || git commit -m "Update video data"
          git push
```

Commit this file. Then go to **Actions** tab in GitHub and manually trigger it once to confirm it works. You should see `data/videos.json` get populated with real YouTube data.

---

## Step 6: Make Your JSON Publicly Accessible

Since your repo is public, your JSON file is already accessible at a URL like:
```
https://raw.githubusercontent.com/YOUR_USERNAME/kpop-feed/main/data/videos.json
