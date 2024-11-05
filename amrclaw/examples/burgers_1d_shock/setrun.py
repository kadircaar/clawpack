""" 
Module to set up run time parameters for Clawpack.

The values set in the function setrun are then written out to data files
that will be read in by the Fortran code.
    
""" 
import os 
import numpy as np

#------------------------------
def setrun(claw_pkg='amrclaw'):
#------------------------------
    
    """ 
    Define the parameters used for running Clawpack.

    INPUT:
        claw_pkg expected to be "classic" for this setrun.

    OUTPUT:
        rundata - object of class ClawRunData 
    
    """ 
    from clawpack.clawutil import data
    
    assert claw_pkg.lower() == 'amrclaw',  "Expected claw_pkg = 'amrclaw!"

    num_dim=1
    rundata = data.ClawRunData(claw_pkg, num_dim)

    #------------------------------------------------------------------
    # Problem-specific parameters to be written to setprob.data:
    #------------------------------------------------------------------

    # MUST BE ADDED BY USER IF DESIRED !!
    #probdata = rundata.new_UserData(name='probdata',fname='setprob.data')
    # For example:
    #probdata.add_param('u',     1.0,  'advection velocity')
    
    #------------------------------------------------------------------
    # Standard Clawpack parameters to be written to claw.data:
    #------------------------------------------------------------------

    clawdata = rundata.clawdata  # initialized when rundata instantiated

    # ---------------
    # Spatial domain:
    # ---------------

    # Number of space dimensions:
    clawdata.num_dim = num_dim
    
    # Lower and upper edge of computational domain:
    clawdata.lower[0] = -0.200000e+00         # xlower
    clawdata.upper[0] = 1.00000e+00          # xupper

    # Number of grid cells:
    clawdata.num_cells[0] = 20                #mx
    
    

    # ---------------
    # Size of system:
    # ---------------

    # Number of equations in the system:
    clawdata.num_eqn = 1

    # Number of auxiliary variables in the aux array (initialized in setaux)
    clawdata.num_aux = 0
    
    # Index of aux array corresponding to capacity function, if there is one:
    clawdata.capa_index = 0
    
    
    
    # -------------
    # Initial time:
    # -------------

    clawdata.t0 = 0.0
    
    # Restart from checkpoint file of a previous run?
    # If restarting, t0 above should be from original run, and the
    # restart_file 'fort.qNNNN' specified below should be in 
    # the OUTDIR indicated in Makefile.

    clawdata.restart = False               # True to restart from prior results
    clawdata.restart_file = 'fort.q0006'   # File to use for restart data
    
    # -------------
    # Output times:
    #--------------

    # Specify at what times the results should be written to fort.q files.
    # Note that the time integration stops after the final output time.
    # The solution at initial time t0 is always written in addition.

    clawdata.output_style = 1

    if clawdata.output_style==1:
        # Output nout frames at equally spaced times up to tfinal:
        clawdata.num_output_times = 10
        clawdata.tfinal = 1.000000
        clawdata.output_t0 = True # output at initial (or restart) time?

    
    elif clawdata.outstyle == 2:
        # Specify a list of output times.  
        clawdata.output_times =  [0.1, 0.15]   # used if outstyle == 2


    elif clawdata.outstyle == 3:
        # Output every iout timesteps with a total of ntot time steps:
        clawdata.output_step_interval = 1
        clawdata.total_steps = 5
        clawdata.output_t0 = True
    

    clawdata.output_format = 'ascii'      # 'ascii' is only option currently


    clawdata.output_q_components = 'all'   # could be list such as [True,True]
    clawdata.output_aux_components = 'none'  # could be list
    clawdata.output_aux_onlyonce = True    # output aux arrays only at t0


    # ---------------------------------------------------
    # Verbosity of messages to screen during integration:  
    # ---------------------------------------------------

    # The current t, dt, and cfl will be printed every time step
    # at AMR levels <= verbosity.  Set verbosity = 0 for no printing.
    #   (E.g. verbosity == 2 means print only on levels 1 and 2.)
    clawdata.verbosity = 0
    
    

    # --------------
    # Time stepping:
    # --------------

    # if dt_variable==1: variable time steps used based on cfl_desired,
    # if dt_variable==0: fixed time steps dt = dt_initial will always be used.
    clawdata.dt_variable = True
    
    # Initial time step for variable dt.  
    # If dt_variable==0 then dt=dt_initial for all steps:
    clawdata.dt_initial = 1.000000
    
    # Max time step to be allowed if variable dt used:
    clawdata.dt_max = 1
    
    # Desired Courant number if variable dt used, and max to allow without 
    # retaking step with a smaller dt:
    clawdata.cfl_desired = 0.9
    clawdata.cfl_max = 1.0
    
    # Maximum number of time steps to allow between output times:
    clawdata.steps_max = 500

    
    

    # ------------------
    # Method to be used:
    # ------------------

    # Order of accuracy:  1 => Godunov,  2 => Lax-Wendroff plus limiters
    clawdata.order = 1
    
    # Number of waves in the Riemann solution:
    clawdata.num_waves = 1
    
     # List of limiters to use for each wave family:
    # Required:  len(limiter) == num_waves
    # Some options:
    #   0 or 'none'     ==> no limiter (Lax-Wendroff)
    #   1 or 'minmod'   ==> minmod
    #   2 or 'superbee' ==> superbee
    #   3 or 'vanleer'  ==> van Leer
    #   4 or 'mc'       ==> MC limiter
    clawdata.limiter = [0]
    
    # Source terms splitting:
    #   src_split == 0  => no source term (src routine never called)
    #   src_split == 1  => Godunov (1st order) splitting used, 
    #   src_split == 2  => Strang (2nd order) splitting used,  not recommended.
   

    clawdata.use_fwaves = False    # True ==> use f-wave version of algorithms
    
    # Source terms splitting:
    #   src_split == 0 or 'none'    ==> no source term (src routine never called)
    #   src_split == 1 or 'godunov' ==> Godunov (1st order) splitting used, 
    #   src_split == 2 or 'strang'  ==> Strang (2nd order) splitting used,  not recommended.



    clawdata.source_split = 0
    
    
    # --------------------
    # Boundary conditions:
    # --------------------

    # Number of ghost cells (usually 2)
    clawdata.num_ghost = 2
    
    # Choice of BCs at xlower and xupper:
    #   0 => user specified (must modify bcN.f to use this option)
    #   1 => extrapolation (non-reflecting outflow)
    #   2 => periodic (must specify this at both boundaries)
    #   3 => solid wall for systems where q(2) is normal velocity
    
    clawdata.bc_lower[0] = 'extrap'
    clawdata.bc_upper[0] = 'extrap'
    
    # ---------------
    # Gauges:
    # ---------------
    rundata.gaugedata.gauges = []
    # for gauges append lines of the form  [gaugeno, x, t1, t2]
    rundata.gaugedata.gauges.append([0, 0.1, 0 , 1e9])
    rundata.gaugedata.gauges.append([1, 0.5, 0 , 1e9])
    
    # --------------
    # Checkpointing:
    # --------------
    
    # Specify when checkpoint files should be created that can be
    # used to restart a computation.
    
    clawdata.checkpt_style = 0
    
    if clawdata.checkpt_style == 0:
        # Do not checkpoint at all
        pass
    
    elif clawdata.checkpt_style == 1:
        # Checkpoint only at tfinal.
        pass
    
    elif clawdata.checkpt_style == 2:
        # Specify a list of checkpoint times.
        clawdata.checkpt_times = [0.1,0.15]
    
    elif clawdata.checkpt_style == 3:
        # Checkpoint every checkpt_interval timesteps (on Level 1)
        # and at the final time.
        clawdata.checkpt_interval = 5
    
    # ---------------
    # AMR parameters:
    # ---------------
    
    amrdata = rundata.amrdata

    # max number of refinement levels:
    amrdata.amr_levels_max = 3
    
    # List of refinement ratios at each level (length at least amr_level_max-1)
    amrdata.refinement_ratios_x = [2, 4]
    amrdata.refinement_ratios_t = [2, 4]
    
    
    # Specify type of each aux variable in clawdata.auxtype.
    # This must be a list of length num_aux, each element of which is one of:
    #   'center',  'capacity', or 'xleft'  (see documentation).
    amrdata.aux_type = []
    
    
    # Flag for refinement based on Richardson error estimater:
    amrdata.flag_richardson = False    # use Richardson?
    amrdata.flag_richardson_tol = 0.01e+00  # Richardson tolerance
    
    # Flag for refinement using routine flag2refine:
    amrdata.flag2refine = True      # use this?
    amrdata.flag2refine_tol = 0.4 # tolerance used in this routine
    # User can modify flag2refine to change the criterion for flagging.
    # Default: check maximum absolute difference of first component of q
    # between a cell and each of its neighbors.
    
    # steps to take on each level L between regriddings of level L+1:
    amrdata.regrid_interval = 1
    
    # width of buffer zone around flagged points:
    # (typically the same as regrid_interval so waves don't escape):
    amrdata.regrid_buffer_width  = 2
    
    # clustering alg. cutoff for (# flagged pts) / (total # of cells refined)
    # (closer to 1.0 => more small grids may be needed to cover flagged cells)
    amrdata.clustering_cutoff = 0.7
    
    # print info about each regridding up to this level:
    amrdata.verbosity_regrid = 0
    
    
    # ---------------
    # Regions:
    # ---------------
    rundata.regiondata.regions = []
    # to specify regions of refinement append lines of the form
    #  [minlevel,maxlevel,t1,t2,x1,x2]
    
    
    #  ----- For developers -----
    # Toggle debugging print statements:
    amrdata.dprint = False      # print domain flags
    amrdata.eprint = False      # print err est flags
    amrdata.edebug = False      # even more err est flags
    amrdata.gprint = False      # grid bisection/clustering
    amrdata.nprint = False      # proper nesting output
    amrdata.pprint = False      # proj. of tagged points
    amrdata.rprint = False      # print regridding summary
    amrdata.sprint = False      # space/memory output
    amrdata.tprint = False      # time step reporting each level
    amrdata.uprint = False      # update/upbnd reporting
    
    return rundata
    # end of function setrun
    # ----------------------


if __name__ == '__main__':
    # Set up run-time parameters and write all data files.
    import sys
    rundata = setrun(*sys.argv[1:])
    rundata.write()
    
