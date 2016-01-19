import pylab as P

def plotAB(dataA,dataB):
    """Draw two data lines on two axes"""
    P.clf()

    f=P.figure(figsize=(8,5)) 
    ax1 = f.add_subplot(111)
    ax2 = ax1.twinx()
    xA = range(len(dataA))
    lA=ax1.plot(xA,dataA,color="blue", ls="-")
    xB = range(len(dataB))
    lA=ax2.plot(xB,dataB,color="green", ls="--")

    #xs=range(0,121,20)
    #ax1.set_xticks(xs)
    #ys=[0, 20000, 40000, 60000]
    #ax1.set_yticks(ys)
    #ax1.set_yticklabels(["0","20,000","40,000","60,000"]) 

    ax1.get_xaxis().tick_bottom()
    ax1.get_yaxis().set_tick_params(direction='out')
    ax2.get_yaxis().set_tick_params(direction='out')
    ax1.get_xaxis().set_tick_params(direction='out')
    ax1.spines['top'].set_visible(False)
    ax2.spines['top'].set_visible(False)

def testAB():
    A=20*P.random(50)
    B=30+10*P.random(52)
    plotAB(A,B)
