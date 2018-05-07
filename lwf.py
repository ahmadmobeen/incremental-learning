import experiment
import plotter
import json
import numpy as np
import os
folders = ['plots/scaling/']
experimentCon = []
for folder in folders:
    files = os.listdir(folder)
    experiments= []
    for f in files:
        print (f)
        if ".DS" in f:
            continue
        with open(folder+f) as json_data:
            d = json.load(json_data)
            tempDic = json.loads(d)
            e = experiment.experiment(None, None,None)
            e.__dict__ = tempDic
            experiments.append(e)
    experimentCon.append(experiments)

counter=0
myPlotter = plotter.Plotter()
legend = ["iCaRL with Herding", "iCaRL no Herding"]
for e in experimentCon:
    ncm = []
    tc = []
    x = []
    ic = []
    inmc = []
    for ex in e:
        x = ex.results['Trained Classifier'][0]
        ncm.append(ex.results['Trained Classifier Scaled'][1])
        ic.append(ex.results['Trained Classifier'][1])
        inmc.append(ex.results['Ideal NMC'][1])
    ncmStd = np.std(ncm, axis=0)
    tcStd = np.std(tc, axis=0)

    iinmc = np.std(inmc, axis=0)
    iic = np.std(ic, axis=0)
    ncm = np.mean(ncm,axis=0)
    inmc = np.mean(inmc, axis=0)
    ic = np.mean(ic,axis=0)
    tc = np.mean(tc, axis=0)
    myPlotter.plot(x, ncm, legend=legend[counter]+" with NCM", error=ncmStd)
    myPlotter.plot(x, inmc, legend=legend[counter]+" with TC", error=iinmc)
    myPlotter.plot(x, ic, legend=legend[counter] + " with TC", error=iic)
    counter+=1

myPlotter.save_fig("../tempLWF", 11)

