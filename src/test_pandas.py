import pandas as pd
import pprint as pp

# リスト
List = [[1,2],[3,4]]
pp.pprint("Case List:")
pp.pprint(pd.DataFrame(List,columns=['x','y']))

# 辞書
Dic = [{'x':1, 'y':2},{'x':3, 'y':4}]
pp.pprint("Case Dictionary:")
pp.pprint(pd.DataFrame(Dic))

