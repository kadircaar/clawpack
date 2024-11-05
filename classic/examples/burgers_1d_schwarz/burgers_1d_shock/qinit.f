 
c
c
c =========================================================
       subroutine qinit(meqn,mbc,mx,xlower,dx,q,maux,aux)
c =========================================================
c
c     # Set initial conditions for q.
c
c
      implicit double precision (a-h,o-z)
      dimension q(meqn,1-mbc:mx+mbc)
      dimension aux(maux,1-mbc:mx+mbc)
      common /comsrc/ mu
      common /comic / r
c
c
      ql = 1.d0
      qr = 0.d0
      
      do 150 i=1,mx
c        # left and right edge of i'th cell:
         xl = xlower + (i-1)*dx
         r= xl+2.d0

         if (r .lt. -20.d0) then
             tanhr=-1.d0
           else if (r .gt. 20.d0) then
             tanhr = 1.d0
           else
c            #  xl < 0 < xr and the cell average is weighted combo of ql,qr
             tanhr = (dexp(r) - dexp(-r)) / (dexp(r) + dexp(-r))
           endif
         q(1,i) = 0.5d0*(1-tanhr)
  150    continue
c
      return
      end
