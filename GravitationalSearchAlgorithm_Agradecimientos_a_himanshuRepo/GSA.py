# -*- coding: utf-8 -*-
import random
import numpy
import math
from solution import solution
import time
import massCalculation
import gConstant
import gField
import move

def GSA(objf, lb, ub, dim, PopSize, iters):
    ElitistCheck = 1
    Rpower = 1
     
    s = solution()
    
    vel = numpy.zeros((PopSize, dim))
    fit = numpy.zeros(PopSize)
    M = numpy.zeros(PopSize)
    gBest = numpy.zeros(dim)
    gBestScore = float("inf")
    
    pos = numpy.random.uniform(0, 1, (PopSize, dim)) * (ub - lb) + lb
    
    convergence_curve = numpy.zeros(iters)
    
    print("GSA is optimizing \"" + objf.__name__ + "\"")    
    
    timerStart = time.time() 
    s.startTime = time.strftime("%Y-%m-%d-%H-%M-%S")
    
    for l in range(0, iters):
        for i in range(0, PopSize):
            pos[i,:] = numpy.clip(pos[i,:], lb, ub)
            fitness = objf(pos[i,:])
            fit[i] = fitness

            if gBestScore > fitness:
                gBestScore = fitness
                gBest = pos[i,:].copy()
                s.best = gBestScore
                s.bestIndividual = gBest.copy()
        
        # Guardar fitness inicial en la primera iteración
        if l == 0:
            s.initialFitness = fit.copy()

        M = massCalculation.massCalculation(fit, PopSize, M)
        G = gConstant.gConstant(l, iters)        
        acc = gField.gField(PopSize, dim, pos, M, l, iters, G, ElitistCheck, Rpower)
        pos, vel = move.move(PopSize, dim, pos, vel, acc)
        
        convergence_curve[l] = gBestScore
      
        if (l % 1 == 0):
            print(['At iteration ' + str(l + 1) + ' the best fitness is ' + str(gBestScore)])
    
    # Guardar fitness final
    s.finalFitness = fit.copy()

    timerEnd = time.time()  
    s.endTime = time.strftime("%Y-%m-%d-%H-%M-%S")
    s.executionTime = timerEnd - timerStart
    s.convergence = convergence_curve
    s.Algorithm = "GSA"
    s.objectivefunc = objf.__name__

    return s
