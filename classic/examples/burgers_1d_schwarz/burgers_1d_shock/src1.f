c
c
c =========================================================
      subroutine src1(meqn,mbc,mx,xlower,dx,q,maux,aux,t,dt)
c =========================================================
      implicit none
      integer, intent(inout) :: meqn,mbc,mx,maux
      double precision, intent(inout) :: xlower,dx,t,dt

      integer :: i

      double precision, intent(inout) :: q(meqn,1-mbc:mx+mbc)
      double precision, intent(inout) :: aux(maux,1-mbc:mx+mbc)
      double precision :: mu
      common /comsrc/ mu
    
      do i=1,mx
       q(1,i)=q(1,i)/(1.d0+mu*dt*q(1,i))
      end do
    
      return
      end
