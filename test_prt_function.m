%% Run a Matlab Raytrace
addpath('ZOS-API-samples');
fn = '\FoldedCassegrain.zmx';
hx = 0;
hy = 0;
surface = 3;
nrays = 51;

[ xData,yData,zData,lData,mData,nData,l2Data,m2Data,n2Data,n1,n2 ] = MATLAB_BatchRayTrace_ReadPRTData(surface,nrays,hx,hy,fn);

%% Write the data to a text file that python can interpret
xData = xData';
yData = yData';
zData = zData';

lData = lData';
mData = mData';
nData = nData';

l2Data = l2Data';
m2Data = m2Data';
n2Data = n2Data';
% Create a table with the data and variable names
T = table(xData,yData,zData,lData,mData,nData,l2Data,m2Data,n2Data);
%,...
%     'ColumnNames',...
%     { 'xData','yData','zData','lData','mData','nData','l2Data','m2Data','n2Data','n1','n2'} );

% Write data to text file
writetable(T, 'test_prt_data_secondary.txt');

%% Show the Intercept on surface

% figure(1)
% subplot(131)
%     hold on
%     title('Ray Intercepts')
%     scatter(xData,yData)
%     xlabel('distance [mm]')
%     hold off
% subplot(132)
%     hold on
%     title('Ray Angles')
%     scatter(lData,mData)
%     xlabel('Slope')
%     hold off
% subplot(133)
%     hold on
%     title('Ray Intercepts')
%     scatter(l2Data,m2Data)
%     xlabel('Slope')
%     hold off
    