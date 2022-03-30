#%%
import numpy as np
import matplotlib.pyplot as plt
import polutils as pol

# Test the PRT Computation
n1 = 1.4358 + 1j*9.4953 # Aluminum
n2 = 1
# pth = '/Users/jashcraft/Desktop/prt-data/test_prt_data.txt'
# pth = '/Users/jashcraft/Desktop/prt-data/Webb_Parabola_ray_data.txt'
# pth = 'C:/Users/trent/OneDrive/Documents/GitHub/Polarization-Raytrace/test_prt_data_primary.txt'
# pth = 'C:/Users/trent/OneDrive/Documents/GitHub/Polarization-Raytrace/test_prt_data_secondary.txt'
pth = 'C:/Users/trent/OneDrive/Documents/GitHub/Polarization-Raytrace/test_prt_data_folding.txt'

aoi,x,y,kin,kout,norm = pol.ConvertBatchRayData(pth,n1,n2,mode='reflection')
ts,tp = pol.FresnelCoefficients(aoi,n1,n2)
Pmat = np.zeros([3,3,kin.shape[1]],dtype='complex128')
Jmat = np.zeros([3,3,kin.shape[1]],dtype='complex128')

for i in range(kin.shape[1]):

    Pmat[:,:,i],Jmat[:,:,i] = pol.ConstructPRTMatrix(
        kin[:,i],
        kout[:,i],
        norm[:,i],
        aoi[i],
        n1,
        n2,
        mode='reflection')

fig,axs = plt.subplots(figsize=[9,9],nrows=3,ncols=3)
plt.suptitle('|PRT Matrix| for M2 Surface in Folded Cassegrain')
for j in range(3):
    for k in range(3):
        ax = axs[j,k]
        ax.set_title('P{j}{k}'.format(j=j,k=k))
        sca = ax.scatter(x,y,c=np.abs(Pmat[j,k,:]))
        ax.axes.xaxis.set_visible(False)
        ax.axes.yaxis.set_visible(False)
        ax.set(aspect = 'equal')
        fig.colorbar(sca,ax=ax,shrink=0.8)

fig,axs = plt.subplots(figsize=[9,9],nrows=3,ncols=3)
plt.suptitle('Arg(PRT Matrix) for M2 Surface in Folded Cassegrain')
for j in range(3):
    for k in range(3):
        ax = axs[j,k]
        ax.set_title('P{j}{k}'.format(j=j,k=k))
        sca = ax.scatter(x,y,c=np.angle(Pmat[j,k,:]))
        ax.axes.xaxis.set_visible(False)
        ax.axes.yaxis.set_visible(False)
        ax.set(aspect = 'equal')
        fig.colorbar(sca,ax=ax,shrink=0.8)
plt.show()

# fig,axs = plt.subplots(figsize=[9,3],ncols=3)
# plt.suptitle('E field')
# tit = ['x','y','z']
# for l in range(3):
#     ax = axs[l]
#     ax.set_title('E{}'.format(tit[l]))
#     sca = ax.scatter(x,y,c=np.abs(Pmat[l,0,:]+Pmat[l,1,:]+Pmat[l,2,:]))
#     fig.colorbar(sca,ax=ax)
# plt.show()

# fig,axs = plt.subplots(figsize=[9,9],nrows=3,ncols=3)
# plt.suptitle('|Jones Matrix| for Surface in Webb Parabola')
# for j in range(3):
#     for k in range(3):
#         ax = axs[j,k]
#         ax.set_title('J{j}{k}'.format(j=j,k=k))
#         sca = ax.scatter(x,y,c=np.abs(Jmat[j,k,:]))
#         fig.colorbar(sca,ax=ax)
# plt.show()

# fig,axs = plt.subplots(figsize=[9,9],nrows=3,ncols=3)
# plt.suptitle('Arg{Jones Matrix} for Surface in Webb Parabola')
# for j in range(3):
#     for k in range(3):
#         ax = axs[j,k]
#         ax.set_title('J{j}{k}'.format(j=j,k=k))
#         sca = ax.scatter(x,y,c=np.angle(Jmat[j,k,:]))
#         fig.colorbar(sca,ax=ax)
# plt.show()

# Compute Diattenuation and Retardance
# print(Jmat)
# rs_amp = np.abs(Jmat[0,0,:])
# rp_amp = np.abs(Jmat[1,1,:])
# rs_ang = np.angle(Jmat[0,0,:])
# rp_ang = np.angle(Jmat[1,1,:])

# D = (rs_amp**2 - rp_amp**2)/(rs_amp**2 + rp_amp**2)
# R = rs_ang-rp_ang-np.pi

# plt.figure(figsize=[21,7])
# plt.subplot(121)
# plt.title('Diattenuation')
# plt.scatter(x,y,c=D,alpha=1,vmax=1e-3)
# plt.colorbar()

# plt.subplot(122)
# plt.title('Retardance')
# plt.scatter(x,y,c=R)
# plt.colorbar()

# plt.show()



# %%
