# from github3 import login
from top_github_scraper import get_top_repo_urls
from top_github_scraper import get_top_repos
from top_github_scraper import get_top_users
import os
from dotenv import load_dotenv, find_dotenv

# load_dotenv(find_dotenv())

get_top_repo_urls(keyword="machine learning Lagos")

get_top_repo_urls(keyword="machine learning Nigeria")

get_top_repo_urls(keyword="machine learning Rwanda")


get_top_repos("machine learning Lagos")

get_top_repos("machine learning Nigeria")

get_top_repos("machine learning Rwanda")


get_top_users("machine learning Lagos")

get_top_users("machine learning Nigeria")

get_top_users("machine learning Rwanda")

