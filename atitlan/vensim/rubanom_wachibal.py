import xarray as xr
import os
from atitlan.vensim.utils import DIR_RES
import json

res = {}
for wj in os.listdir(DIR_RES):
    rubi, ext = os.path.splitext(os.path.split(wj)[1])
    if ext == '.json':
        with open(os.path.join(DIR_RES, wj), 'r', encoding='utf8') as w:
            res[rubi] = xr.DataArray.from_dict(json.load(w))

input()