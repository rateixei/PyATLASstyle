# PyATLASstyle
Matplotlib/pyplot ATLAS style

## Usage

```bash
mkdir my_project
cd my_project
git clone https://github.com/rateixei/PyATLASstyle.git .
mkdir my_code
cd my_code
touch my_python_code.py #Copy code below
python my_python_code.py
```

my_python_code.py:
```python
import numpy as np
import matplotlib as mtp
import matplotlib.pyplot as plt
import sys
sys.path.insert(0, "../PyATLASstyle/")
import PyATLASstyle as pas

pas.applyATLASstyle(mtp)

s = np.random.normal(90, 10, 100)

plt.figure(figsize=(8,6))
fig, ax = plt.subplots()
n, b, _ = ax.hist(s, bins=50, range=(50, 140), label='Gaussian', histtype='step')
ax.legend()
ax.set_ylabel("Entries", horizontalalignment='right', y=1.0)
ax.set_xlabel("Jet mass [GeV]", horizontalalignment='right', x=1.0)
ax.set_ylim(0, max(n)*1.3)
pas.makeATLAStag(ax, fig, first_tag="Internal Simulation", second_tag=r"$\sqrt{s}$ = 13 TeV, $t\bar{t}$ non-hadronic")
fig.savefig("fig.pdf")
```
