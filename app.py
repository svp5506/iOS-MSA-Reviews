import pandas as pd
import numpy as np
import json
import datetime
from app_store_scraper import AppStore

# # Define your proxy settings
# proxies = {
#     'http': 'http://your_proxy_here',
#     'https': 'https://your_proxy_here'
# }

MSA_iOS = AppStore(
    country='us',
    app_name='my-spectrum',
    app_id='942608209',
    # proxies=proxies  # Pass the proxies parameter
)

MSA_iOS.review(after=datetime.datetime(2023, 7, 31), sleep=1)

MSA_iOSdf = pd.DataFrame(np.array(MSA_iOS.reviews), columns=['review'])
MSA_iOSdf2 = MSA_iOSdf.join(pd.DataFrame(MSA_iOSdf.pop('review').tolist()))

df = MSA_iOSdf2.developerResponse
devdf = pd.json_normalize(df)

devdf['index'] = devdf.index
MSA_iOSdf2['index'] = MSA_iOSdf2.index
combined = devdf.merge(MSA_iOSdf2, how='outer', right_on='index', left_on='index')
combined.rename(
    columns={
        'body': 'dev response',
        'modified': 'dev response date',
        'date': 'review date',
        'title': 'review title'
    },
    inplace=True
)
combinedReorder = combined.iloc[:, [3, 0, 2, 1, 4, 9, 6, 7, 8, 10, 5]]

combinedFinal = combinedReorder.drop(columns=["developerResponse", "index"])
combinedFinal.to_csv('MSA_iOS_Reviews_New_2.csv')
