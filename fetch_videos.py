name: Fetch YouTube Videos

on:
  schedule:
    - cron: '0 */2 * * *'
  workflow_dispatch:

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
