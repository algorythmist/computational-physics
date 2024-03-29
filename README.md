# Computational Physics Explorations

## Notebooks

[Ordinary Differential Equaltions](odes.ipynb) - Solutions to Physics problems by ODEs

[Introduction to Quantum Mechanics - Griffiths](../road2reality/QM/griffith.ipynb) - Some visualization from this book


## Setup

### Virtual Environment

>> mkdir venv
>>
>> python -m venv venv
>>
>> source venv\Scripts\activate
>>
>> pip install -r requirements.txt
>>
>> pip install git+https://github.com/matplotlib/basemap.git 
>>
>> ipython kernel install --name "computational-physics" --user
>>
>>jupyter notebook

### Anaconda Environment

>> conda activate computational-physics
>>
>> conda install --file requirements.txt
>>
>> ipython kernel install --name "computational-physics" --user
>>
>> jupyter nbextension enable --py widgetsnbextension
>>
>> conda install -c conda-forge jupyter_contrib_nbextensions

### Start Jupyter

The first time, install the jupyter kernel

```commandline
ipython kernel install --name "differential-geometry" --user
```

Then start the notebook

```commandline
jupyter notebook
