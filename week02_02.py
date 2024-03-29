X = [0.17955991, 0.61722035, 0.33185536, 0.23592062, 0.1457398 ,
       0.0474971 , 0.94077841, 0.78114903, 0.6214102 , 0.16870644,
       0.89671188, 0.75286452, 0.31367868, 0.46383938, 0.47599363,
       0.78450372, 0.89880818, 0.77603778, 0.91687474, 0.58306898,
       0.90199105, 0.09824119, 0.63376855, 0.4147054 , 0.87463022,
       0.04165703, 0.71023643, 0.45445708, 0.27535538, 0.25996538,
       0.2792521 , 0.19239299, 0.94726163, 0.19869134, 0.96550543,
       0.76058706, 0.03780031, 0.70013937, 0.44862605, 0.93740636,
       0.56581566, 0.20293273, 0.44892578, 0.57317476, 0.73838422,
       0.18444714, 0.81160181, 0.17480397, 0.61692721, 0.76625995,
       0.03375545, 0.59790204, 0.61053263, 0.68063884, 0.28975517,
       0.6356523 , 0.66379426, 0.28592362, 0.74736263, 0.72896733,
       0.34943388, 0.64784724, 0.91787496, 0.75825783, 0.5189811 ,
       0.99484771, 0.05878952, 0.10193666, 0.65399761, 0.15486421,
       0.61894556, 0.44865217, 0.03426223, 0.14499959, 0.35727112,
       0.92958883, 0.69717072, 0.5616376 , 0.78133459, 0.26200548,
       0.17766772, 0.5694754 , 0.87330397, 0.1086454 , 0.05280223,
       0.84114367, 0.15060094, 0.09547866, 0.45311556, 0.76870276,
       0.79729114, 0.88657391, 0.84212597, 0.51460417, 0.78690699,
       0.47661947, 0.41250934, 0.50699549, 0.85170806, 0.99891709]
Y = [ -0.495878,  -0.725783,  -0.111255,  -3.432718,  -0.330728,
        -1.082825,  -3.261594,  -0.22332 ,  -0.379242,  -2.426704,
        -0.221821,  -1.051987,  -0.607764,  -0.236026,  -8.489959,
        -3.25925 ,  -1.779456,  -1.408726,  -0.027012, -10.203199,
        -0.822759,  -0.027903,  -0.377149,  -1.710108,  -3.482763,
        -2.154184,  -1.349111,  -5.666033,  -0.702836,  -2.842242,
        -0.508901,  -2.437712,  -0.747111,  -0.442274,  -5.165725,
        -1.281973,  -6.766941,  -1.532131,  -1.337748,  -0.531392,
        -0.837851,  -1.06509 ,  -1.21995 ,  -1.424004,  -0.260687,
        -0.727738,  -0.15295 ,  -6.676196,  -1.726793,  -1.558525,
        -0.981184,  -1.035687,  -6.327734,  -0.529742,  -0.939837,
        -0.240315,  -1.533203,  -0.549144,  -1.099864,  -1.063127,
        -0.146878,  -1.649751,  -2.261392,  -1.039409,  -1.996601,
        -0.332549,  -3.296153,  -1.987091,  -4.255115,  -2.152886,
        -0.079665,  -0.387485,  -0.012368,  -0.375251,  -5.197246,
        -1.320408,  -1.725657,  -0.148417,  -5.602131,  -0.033301,
        -1.975537,  -1.329412,  -1.457322,  -0.895005,  -3.363692,
        -6.951246,  -1.979744,  -4.992033,  -0.698439,  -1.024305,
        -0.34995 ,  -2.025887,  -0.896251,  -0.162775,  -0.912357,
        -1.607859,  -1.768943,  -0.135767,  -3.955297,  -3.82706 ]

# 함수 #

def find_n_nearest_value(X, Y, new_x, k):
    import math

    if k == 0:
        return print('The k is not zero!!')

    else:

        NX=list() #new_x와 X의 값 사이의 거리를 담을 리스트
        NY=list() #Y의 값을 새로 담을 리스트 

        for i in range (len(X)):
            distance=math.sqrt((new_x - X[i])**2)
            NX.append(distance)
            NY.append(Y[i])
            
        for i in range (len(NX)-1):
            for j in range (len(NX)-1-i):
                if NX[j] > NX[j+1]:
                    NX[j], NX[j+1] = NX[j+1], NX[j]
                    NY[j], NY[j+1] = NY[j+1], NY[j]
                    
        pred_y=0
        for i in range (k):
            pred_y+=NY[i]
            
    return round(pred_y / k, 3)


# 메인 #

print("if new_x=0.5 and k=3, then pred_y = ", find_n_nearest_value(X, Y, .5, 3))
print("if new_x=0.5 and k=7, then pred_y = ", find_n_nearest_value(X, Y, .5, 7))
print("if new_x=0.5 and k=0, then pred_y = ", find_n_nearest_value(X, Y, .5, 0))

