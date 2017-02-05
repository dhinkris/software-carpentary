import matplotlib.pyplot as plt
import pandas as pd
import sys

input_file=sys.argv[1]
col=sys.argv[2]
df=pd.read_csv(input_file,sep='\t')
plt.hist(df[col])
plt.show()