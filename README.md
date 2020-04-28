# WATsite_on-the-fly

This repo contains the demo code for our manuscript [On-the-fly Prediction of Protein Hydration Densities and Free Energies using Deep Learning](https://arxiv.org/abs/2001.02201) authored by Ahmadreza Ghanbarpour, Amr H. Mahmoud and Markus A. Lill. 

This demo contains the code for the grid-to-grid mapping approach, the first approach using U-Nets for water occupancy grid prediction.

- Data folder: 1adl contains the grid files for 1ADL pdb.
- Watsite_on-the-fly-demo.ipynb is the jupyter notebook containing the code for models, preprocessing and prediction.
- weights folder contains the weights file for the Inception and baseline U-Net models.
- WriteDx.py script may be used to generate DX files for visualization with pymol. Note: This script generates DX files with the origin set to (0, 0, 0). To correctly visualize the grids on the protein, correct origin coordinates should be entered manually in the DX files.
