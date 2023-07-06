import os
import pandas as pd

final_data = []
columns = ['Image', 'Name', 'Status', 'Disease Name']

for folder in os.listdir('augimg'):
    f, s = folder.split('___')
    
    for images in os.listdir(f'augimg/{folder}'):
        if images.find('.webp') == -1:
            dic = {}
            dic['Image'] = f'augimg/{folder}/{images}'
            dic['Name'] = f
            if s != 'healthy':
                dic['Status'] = 'diseased'
                dic['Disease Name'] = s
            else:
                dic['Status'] = s
                dic['Disease Name'] = 'no disease found'
            final_data.append(dic)


df = pd.DataFrame(data=final_data, columns=columns)
df.to_csv("final-data.csv", index=False)