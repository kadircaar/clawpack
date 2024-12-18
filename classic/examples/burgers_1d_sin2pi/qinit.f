
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
c
c
      pi2 = 8.d0*datan(1.0d0)  !# = 2 * pi

      do 150 i=1,mx
      xcell = xlower + (i-0.5d0)*dx
         q(1,i) = 0.5d0 + dsin(pi2*xcell)
  150    continue
c
      return
      end
