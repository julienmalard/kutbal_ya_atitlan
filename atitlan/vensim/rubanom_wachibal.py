import xarray as xr
import os
from atitlan.vensim.utils import DIR_RES
import json
import matplotlib.pyplot as plt

res = {}
for wj in os.listdir(DIR_RES):
    rubi, ext = os.path.splitext(os.path.split(wj)[1])
    if ext == '.json':
        with open(os.path.join(DIR_RES, wj), 'r', encoding='utf8') as w:
            res[rubi] = xr.DataArray.from_dict(json.load(w))

DIR_WCHBL = os.path.join(DIR_RES, 'wchbl')
os.makedirs(DIR_WCHBL, exist_ok=True)

for rtl, ajl in res.items():
    plt.plot(ajl, label=rtl)
    # if rtl != 'Runoff' and 'Runoff' in res:
    #     plt.plot(res['Runoff'], label='Runoff')
    plt.title(rtl)
    plt.legend()

    plt.savefig(os.path.join(DIR_WCHBL, rtl + '.png'))
    plt.clf()
