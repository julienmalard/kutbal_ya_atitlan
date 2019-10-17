from tinamit.envolt.mds.pysd import ModeloPySD
import os
import json
from atitlan.vensim.utils import DIR_RES

dir_ = os.path.split(__file__)[0]
mod = ModeloPySD(os.path.join(dir_, 'ajlanik_kutbal.mdl'))

res = mod.simular(100)

os.makedirs(DIR_RES, exist_ok=True)

if __name__ == '__main__':
    for r in res:
        with open(os.path.join('res', str(r) + '.json'), 'w', encoding='utf8') as d:
            json.dump(r.vals.to_dict(), d)

