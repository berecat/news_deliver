# NewsCatcher

## Description
Simple project that delivers news to Discord server using a Discord bot and [NewsCatcher API](https://newscatcherapi.com/).

## Requirements
Discord bot API KEY and administrative rights to your Discord server
NewsCatcher API KEY

## Project Setup
```
git clone git@github.com:berecat/news_deliver.git
cd news_deliver
```
Create virtual environment
```
source /path/to/virtualenv/bin/activate
pip3 install -r requirements.txt
```
Create .env file and write:
```
DISCORD_TOKEN="*insert_your_discord_token*"
NEWS_API_TOKEN="*insert_your_newscatcher_token*"
```
## Run Program
```
python3 main.py
```
