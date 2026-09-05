"""Reproduce the Week 1 numerical results using only Python's standard library."""
from pathlib import Path
import math
import csv

root = Path(__file__).resolve().parent
columns = ['Simulation','Maximum roll (degrees)','RMS roll (degrees)','Settling time (seconds)','Completed oscillations']
time = [20*i/999 for i in range(1000)]
rows=[]
for name,a,b,w in [('Baseline',10,.15,2),('Experiment A',20,.15,2),('Experiment B',10,.40,2),('Experiment C',10,.15,3)]:
    y=[a*math.exp(-b*t)*math.cos(w*t) for t in time]
    outside=[i for i,x in enumerate(y) if abs(x)>1]
    settling=0 if not outside else (math.nan if outside[-1]==999 else time[outside[-1]+1])
    crossings=sum((y[i]<0)!=(y[i+1]<0) for i in range(999))
    rows.append([name,f'{max(map(abs,y)):.2f}',f'{math.sqrt(sum(x*x for x in y)/len(y)):.2f}',f'{settling:.2f}',str(crossings//2)])
with (root/'results/week1_results_original.csv').open() as f:
    original=list(csv.reader(f))
assert [columns]+rows == original, 'Results differ from the original CSV'
with (root/'results/week1_results.csv').open('w',newline='') as f:
    writer=csv.writer(f);writer.writerow(columns);writer.writerows(rows)
for row in rows:print(', '.join(row))
print('PASS: all 16 numerical values match the original Week 1 CSV.')
