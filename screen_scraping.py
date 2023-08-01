import json
import re

import pandas as pd
import requests

url = "https://www.instat.gov.al/en/sdgs/no-poverty/12-by-2030-reduce-at-least-by-half-the-proportion-of-men-women-and-children-of-all-ages-living-in-poverty-in-all-its-dimensions-according-to-national-definitions/121-proportion-of-population-living-below-the-national-poverty-line-by-sex-and-age/"

html_text = requests.get(url).text

# for map data:
# map_data = re.search(r"mapData=(.*?);<", html_text).group(1)
# print(map_data)

graph_data = re.search(r"graphsDataJson=(.*?);<", html_text).group(1)
graph_data = json.loads(graph_data)

df = pd.DataFrame(graph_data[0]["indicatorDataValues"])
print(df)
