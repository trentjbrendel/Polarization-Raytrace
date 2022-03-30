import numpy as np
import polutils as pol
import matplotlib.pyplot as plt

# Test the AOI map
n1 = 1.6146
n2 = 1
pth = '/Users/trent/OneDrive/Documents/GitHub/Polarization-Raytrace/test_prt_data.txt'
#pth = '/Users/trent/Documents/GitHub/Polarization-Raytrace/test_prt_data.txt'
#pth = '/Users/jashcraft/Desktop/prt-data/test_prt_data.txt'

def GenAOIMap(fn,n1,n2):

    aoi,x,y = pol.ConvertBatchRayData(pth,n1,n2)
    ts,tp = pol.FresnelCoefficients(aoi,n1,n2)
    D = (ts**2 - tp**2)/(ts**2 + tp**2)

    plt.figure(figsize=[14,7])
    plt.subplot(121)
    plt.title('Angles of Incidence [deg]')
    plt.scatter(x,y,c=aoi,alpha=0.7)
    plt.colorbar()
    plt.subplot(122)
    plt.title('Diattenuation')
    plt.scatter(x,y,c=D,alpha=0.7)
    plt.colorbar()
    plt.show()

GenAOIMap(pth,n1,n2)