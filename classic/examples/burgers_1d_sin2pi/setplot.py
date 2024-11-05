 

""" 
Set up the plot figures, axes, and items to be done for each frame.

This module is imported by the plotting routines and then the
function setplot is called to set the plot parameters.
    
""" 
import numpy as np
import os
from pylab import plot, legend
if os.path.exists('_output_qref'):
    qref_dir = os.path.abspath('_output_qref')
else:
    qref_dir = None
    print ("No _output_qref found.  For reference solution: ")
    print ("   make .output -f Makefile_qref")


#--------------------------
def setplot(plotdata):
#--------------------------
    
    """ 
    Specify what is to be plotted at each frame.
    Input:  plotdata, an instance of clawpack.visclaw.data.ClawPlotData.
    Output: a modified version of plotdata.
    
    """ 

    plotdata.clearfigures()  # clear any old figures,axes,items data


    # Figure for q[0]
    plotfigure = plotdata.new_plotfigure(name='u[0]', figno=0)

    # Set up for axes in this figure:
    plotaxes = plotfigure.new_plotaxes(name='Solution')
    plotaxes.xlimits = 'auto'
    plotaxes.ylimits = 'auto'
    plotaxes.title = 'u(x,t)'

    # Set up for item on these axes:
    plotitem = plotaxes.new_plotitem(name='solution', plot_type='1d')
    plotitem.plot_var = 0
    plotitem.plotstyle = '-^'
    plotitem.color = 'g'
    plotitem.show = True       # show on plot?
        
    # Reference solution:
    if qref_dir:
        plotitem = plotaxes.new_plotitem(plot_type='1d')
        plotitem.outdir = qref_dir
        plotitem.plot_var = 0
        plotitem.plotstyle = '-'
        plotitem.color = 'k'
        plotitem.show = True       # show on plot?


    # Parameters used only when creating html and/or latex hardcopy
    # e.g., via clawpack.visclaw.frametools.printframes:
    plotdata.printfigs = True                # print figures
    plotdata.print_format = 'png'            # file format
    plotdata.print_framenos = 'all'          # list of frames to print
    plotdata.print_fignos = 'all'            # list of figures to print
    plotdata.html = True                     # create html files of plots?
    plotdata.html_homelink = '../README.html'   # pointer for top of index
    plotdata.latex = True                    # create latex file of plots?
    plotdata.latex_figsperline = 2           # layout of plots
    plotdata.latex_framesperline = 1         # layout of plots
    plotdata.latex_makepdf = False           # also run pdflatex?
    
    return plotdata
