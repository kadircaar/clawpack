 

""" 
Set up the plot figures, axes, and items to be done for each frame.

This module is imported by the plotting routines and then the
function setplot is called to set the plot parameters.
    
""" 

import numpy as np
import os



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
    if plotdata is None:
        from clawpack.visclaw.data import ClawPlotData
        plotdata = ClawPlotData() 
    plotdata.clearfigures()  # clear any old figures,axes,items data


    # Figure for q[0]
    plotfigure = plotdata.new_plotfigure(name='u[0]', figno=0)

    # Set up for axes in this figure:
    plotaxes = plotfigure.new_plotaxes(name='Solution')
    plotaxes.xlimits = [0,1]
    plotaxes.ylimits = 'auto'
    plotaxes.title = 'u(x,t)'

    
    plotitem = plotaxes.new_plotitem(name='solution', plot_type='1d_plot')
    plotitem.plot_var = 0
    plotitem.amr_color = ['g','b','r']
    plotitem.amr_plotstyle = ['^-','s-','o-']
    plotitem.amr_data_show = [1,1,1]
    plotitem.amr_kwargs = [{'markersize':5},{'markersize':4},{'markersize':3}]
     

    def plot_addtrue_with_legend(current_data):
        plotitem = plotaxes.new_plotitem(plot_type='1d_plot')
        plotitem.outdir = qref_dir
        plotitem.plot_var = 0
        plotitem.color = ['g','b','r']
        plotitem.plotstyle = ['^-','s-','o-']
        plotitem.kwargs = [{'markersize':3},{'markersize':3},{'markersize':3}]
        plotitem.show = True       # show on plot?

        try:
            from clawpack.visclaw import legend_tools
            labels = ['Level 1','Level 2', 'Level 3','Reference solution']
            legend_tools.add_legend(labels, colors=['g','b','r','g'],
                        markers=['^','s','o',''], linestyles=['','','','-'],
                        loc='upper right')
        except:
            legend(loc='upper right')

        plotaxes.afteraxes = plot_addtrue_with_legend


    # ------------------------------------------
    # Figure with each level plotted separately:

    plotfigure = plotdata.new_plotfigure(name='By AMR Level', figno=2)
    plotfigure.kwargs = {'figsize':(8,10)}
        

    for level in range(1,4):
    # Set up plot for this level:
        plotaxes = plotfigure.new_plotaxes()
        plotaxes.axescmd = 'subplot(3,1,%i)' % level
        plotaxes.xlimits = 'auto'
        plotaxes.ylimits = 'auto'
        plotaxes.title = 'Level %s' % level
        
    
        plotitem = plotaxes.new_plotitem(plot_type='1d_plot')
        plotitem.plot_var = 0
        plotitem.amr_color = ['g','b','r']
        plotitem.amr_plotstyle = ['^-','s-','o-']
        plotitem.amr_data_show = [0,0,0]
        plotitem.amr_data_show[level-1] = 1  # show only one level

    #-----------------------------------------
    # Figures for gauges
    #-----------------------------------------
    plotfigure = plotdata.new_plotfigure(name='q', figno=300, \
                                     type='each_gauge')
    plotfigure.clf_each_gauge = True

    plotaxes = plotfigure.new_plotaxes()
    plotaxes.xlimits = 'auto'
    plotaxes.ylimits = 'auto'
    plotaxes.title = 'Solution'
    plotitem = plotaxes.new_plotitem(plot_type='1d_plot')
    plotitem.plot_var = 0
    plotitem.plotstyle = 'b-'

    # Parameters used only when creating html and/or latex hardcopy
    # e.g., via clawpack.visclaw.frametools.printframes:

    plotdata.printfigs = True                # print figures
    plotdata.print_format = 'png'            # file format
    plotdata.print_framenos = 'all'          # list of frames to print    
    plotdata.print_fignos = 'all'            # list of figures to print                                                                         
    plotdata.html = True                     # create html files of plots?
    plotdata.html_homelink = '../README.html'
    plotdata.latex = True                    # create latex file of plots?
    plotdata.latex_figsperline = 2           # layout of plots
    plotdata.latex_framesperline = 1         # layout of plots
    plotdata.latex_makepdf = False           # also run pdflatex?

    return plotdata
