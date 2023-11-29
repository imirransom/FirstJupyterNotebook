import pandas as pd

df = pd.read_csv('museums.csv', low_memory=False)


def desMuseumType(mtype):
    s = df[df['Museum Type'] == mtype]
    print(f'Result for {mtype}')
    print('revenue ${:,.2f}'.format(s['Revenue'].mean()))
    print('income ${:,.2f}'.format(s['Income'].mean()))


l = df['Museum Type'].unique().tolist()
for m in l:
    desMuseumType(m)
