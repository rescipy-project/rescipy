=====
Usage
=====

After installation, you can simply import rescipy with:

.. code-block:: python
    
    import rescipy

To setup your environment type:

.. code-block:: python
    
    rescipy.setup()

This function will apply some custom settings to plots and will conveniently import useful packages into your namespace, namely:

* pandas as pd
* xarray as xr
* nxarray as nxr
* numpy as np
* scipy
* matplotlib.pyplot as plt
* lmfit
* holoviews as hv
* show and figure from bokeh
* hvplot.xarray and hvplot.pandas
