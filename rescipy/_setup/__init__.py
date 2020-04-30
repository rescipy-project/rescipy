def setup(theme = 'light_minimal',
          hv_cmap = 'afmhot',
          hv_frame_height = 500,
          hv_frame_width = 600,
          hv_tools=['hover']
          ):

    import pandas as pd
    import xarray as xr
    import nxarray as nxr
    import numpy as np
    import scipy
    import matplotlib.pyplot as plt
    import lmfit

    import holoviews as hv
    hv.extension('bokeh')
    hv.renderer('bokeh').theme = theme

    hv.opts.defaults(hv.opts.Image(cmap=hv_cmap,
                                data_aspect=1,
                                frame_height=hv_frame_height,
                                tools=hv_tools),
                    hv.opts.Curve(frame_height=hv_frame_height,
                                frame_width=hv_frame_width,
                                tools=hv_tools))

    import hvplot.xarray, hvplot.pandas

    from bokeh.io import output_notebook
    from bokeh.io import show
    from bokeh.plotting import figure
    from bokeh.plotting import curdoc
    output_notebook()
    curdoc().theme = theme

    import builtins

    builtins.pd = pd
    builtins.xr = xr
    builtins.nxr = nxr
    builtins.np = np
    builtins.scipy = scipy
    builtins.plt = plt
    builtins.lmfit = lmfit
    builtins.hv = hv
    builtins.show = show
    builtins.figure = figure
