import scrapper as sc
import pandas as pd
df = sc.get_jobs("data scientist", 15, False)
print(df)