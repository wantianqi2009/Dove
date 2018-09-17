# Dove
QE vcrelax&amp;phonon

Phonon 流程：
一. 结构
1. cell parameter
2. atomic position
3. pseudo potential
4. burai 编出scf.in 和 example.in
二. scftest
1.复制scftest文件夹
2.更改scf.in 参数
  主要包括：
 （1） cell parameter
  (2)  atomic position
  (3)  pseudo potential(注意赝势带来的倍数关系，在creatinput.py中23行更改）
  (4)  nat 和 ntyp
3.更改kpoint
4.运行creatinput.py
5.提交两个job文件
6.运行plot.py(如有报错，检查是否收敛）
三. vcrelax
1.复制vcrelax文件夹
2.更改example.in 参数
  主要包括：
  （1） cell parameter
   (2) atomic position
   (3) pseudo potential
   (4) 合适的ecut（注意倍数）和合适kpoint
3.更改vclocation
  主要包括：
  (1) 压强范围
  (2) scfnp格点
4.编写合适的ph.in(nq格点在phonon.py45行更改）
5.运行vcinput.py
6.提交jobLDA.sh(注意并行任务个数和核数的关系）
7.运行phonon.py
8.提交jobscf.sh
