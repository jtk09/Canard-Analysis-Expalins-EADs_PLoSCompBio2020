# Clear directory - remove junk from previous runs and start fresh
clean()
name = "desing"
delete(name)

l = load(e=name,c="constants", UZSTOP={2: [-4.0, 4.0]})
r = merge(run(l) + run(l,DS='-'))
#r = run(l)
sv(r,name)

# Continue the FSNII
#fsnii=run(r('BP1'),IPS=2,ISW=-1,ICP=[2,3],ISP=4,ILP=0) #ISP=2
#ap(hr1,name)

#loadbd(name).writeRawFilename('hopf_locus')
#loadbd(name)(11).writeRawFilename('unstable_periodic2')
#loadbd(name)(13).writeRawFilename('unstable_periodic3')
plot(name,stability=1,use_labels=0,use_symbols=1)
wait()

delete(name)
clean()
