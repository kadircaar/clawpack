      subroutine setprob
      implicit double precision (a-h,o-z)
      character*12 fname
      common /comsrc/ mu
      common /comic / m
      common /comic / r
      iunit = 7
      fname = 'setprob.data'
c
c     # Set the viscosity coefficient for the viscous source term
c     # eps is passed to src1.f in comsrc and also used in qinit.
c
      call opendatafile(iunit, fname)
      read(7,*) mu
      read(7,*) m
      return
      end
