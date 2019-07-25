# deltaVinaXGB
This is a machine-learning based protein-ligand scoring function.
### Setup
Create environment
```
make Makefile create_environment
source activate DXG
make Makefile requirements
```
You still need to install rdkit(version >= 2018.03.2) and obabel, these two packages can be easily installed using anaconda

```
conda install -c rdkit rdkit
conda install -c openbabel openbabel
```
Note: if pandas/numpy can't be imported after installing rdkit, just run the make Makefile requirements command again. <br>

To prepare pdbqt files for calculating Vina scores, mgltools(version == 1.5.6) should be installed. It can be downloaded from http://mgltools.scripps.edu/downloads. <br>
If you also want to obtain deltaVinaRF predicted scores, R(version >= 3.3.1) and its randomForest library should be installed.<br>

Install source code
```
python setup.py install
```
Before running model, remember change the python, R, obabel, mgl tools paths into your own directorys in Feature/software_path_mac.py or Feature/software_path_linux.py file. <br>

### Data
Before calculating scores, three inputfiles are needed:<br>
pdbid_ligand.mol2/sdf         --> ligand structure file<br>
pdbid_protein.pdb             --> protein structure file<br>
pdbid_protein_all.pdb         --> protein with water molecules structure file<br>

### Usage 

Run model

Check all options 
```
python run_DXGB.py --help
```
Run test example
```
python run_DXGB.py --runfeatures --average
```
--runfeatures flag is for feature calculation, default is to calculate all features.<br>
--average flag is for ensemble predictions from 10 models.<br>
The predicted scores for different structures of Vina, and deltaVinaXGB will be saved in outfile (default is score.csv) in datadir.<br>
If you want to get deltaVinaRF scores as well, add --runrf. <br>

Note:
1) Ligand structure should includes both atom and bond information, such as mol2 and sdf. Be careful when using mol2 file as input format, some atom types are not recognized in RDKit (O.co2 for O in C-PO32- group). 
2) Using different version of RDKit, the ligand stability features can be slightly different.
3) Abbrevations: RW --> receptor water; BW --> bridging water

### Reference
1. Wang, C.; Zhang, Y. K., Improving Scoring-Docking-Screening Powers of Protein-Ligand Scoring Functions using Random Forest. J. Comput. Chem. 2017, 38, 169-177. https://doi.org/10.1002/jcc.24667




