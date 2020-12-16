import scrape as sc 
import pandas as pd 

path = "C:\Program Files (x86)\chromedriver"

df = sc.get_jobs('data scientist',550, False, path,15)

df.to_csv('glassdoor_jobs.csv', index = False)