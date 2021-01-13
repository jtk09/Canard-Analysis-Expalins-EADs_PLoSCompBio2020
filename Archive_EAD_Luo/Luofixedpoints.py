# Clear directory - remove junk from previous runs and start fresh
clean()
name = "Luofixedpoints"
delete(name)

# Continue up to gCa ([6]) = 0.112 

l = load(e=name,c="constants",ICP=[6], UZSTOP={6: 0.112})
#r = merge(run(l) + run(l,DS='-'))
r = run(l)
#sv(r,name)

l = load(r('UZ1'),ICP=[3], DS='-', UZR={3: -4}, STOP=['UZ3'])
#r = merge(run(l) + run(l,DS='-'))
r = run(l)
#sv(r,name)

# Grab the first Hopf bifurcation and continue the periodic orbit
hr1=run(r('HB1'),IPS=2,ISW=-1,ICP=[3,11],UZSTOP={11:200000.},ISP=4,ILP=1) #ISP=2
ap(hr1,name)

# Grab the second Hopf bifurcation and continue the periodic orbit
#hr2=run(r('HB2'),IPS=2,ISW=-1,ICP=[2,11],UZSTOP={11:120000},NMX=2000,ISP=4,ILP=1) #ISP=2
#ap(hr2,name)

# Continue period-doubling bifurcation
#pd1 = run(h('PD1'),NTST=750,ISW=-1, STOP=['UZ1'])
#ap(pd1,name)

#pd2 = run(pd1('PD1'),NTST=1000, ISW=-1)
#ap(pd2,name)

#pd3 = run(pd2('PD1'),NTST=1250, ISW=-1, DSMAX=0.05)
#ap(pd3,name)

#pd4 = run(pd3('PD1'),NTST=1500, ISW=-1, DSMAX=0.05)
#ap(pd4,name)

#p2 = load(e="L1s2mmo",c="L1s2mmo",ICP=[2,11],IPS=2,NMX=1000,ISP=4,ILP=0)
#pd2 = run(p2,DS='-')
#ap(pd2,name)

#Continue locus of shiftd LP2
t = load(r('LP2'),ICP=[3,4],ISW=2, UZSTOP={3:[-7.5, 0], 4:[0, 7.5]})
t1 = merge(run(t) + run(t, DS='-'))
sv(t1,name)

#loadbd(name).writeRawFilename('2LP1')

# Compute locus of Hopf in two parameters
h = load(r('HB1'), ICP=[3,4], ISW=2, DSMAX=0.1, UZR={3:[-4, 0], 4:[0, 4]}, STOP=['UZ1'])
# Continue from this label in two parameters
h2 = merge(run(h) + run(h, DS='-'))
ap(h2,name)

# Compute locus of SNP in two parameters
#s = load(hr1('LP1'),ICP=[3,4], ISW=2, ISP=1, UZSTOP={3:[-7.5, 0], 4:[0, 7.5]}) #no detection of folds
# Continue from this label in two parameters
#s1 = run(s)
#sp = merge(run(s1) + run(s1,DS='-'))
#sv(sp,name)

#loadbd(name).writeRawFilename('2Hopf_C025')
#bifdiag=loadbd(name).toArray()

# Compute locus of Homoclinic orbit in two parameters
ho = load(hr1('UZ3'), ICP=[3,4], ISP=0, NTST=2000, JAC=0, UZSTOP={3:[-4, 0], 4:[0, 4]},NMX=1000)
# Continue from this label in two parameters
h3 = merge(run(ho)+run(ho,DS='-'))
ap(h3,name)

#loadbd(name).writeRawFilename('hopf_locus')
#loadbd(name)(11).writeRawFilename('unstable_periodic2')
#loadbd(name)(13).writeRawFilename('unstable_periodic3')
plot(name,stability=1,use_labels=0,use_symbols=1)
wait()

delete(name)
clean()
