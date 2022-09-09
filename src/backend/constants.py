features = {'Material': ['SiO2', 'Ag', 'TiO2', 'PLGA', 'Pt', 'IronOxide', 'ZnO', 'Au',
        'CuO', 'MgO', 'Polystyrene', 'EudragitRL', 'ZrO2', 'C60', 'C70',
        'MWCNT', 'NiO', 'Ay', 'CeO2', 'Ce O2'],
 'Type': ['I', 'O', 'C', 0.0],
 'Shape': ['Sphere', 'Irregular', 'Iregular', 'Rod', 'Star', 'Nanotube',
        'Cubic', 'Round'],
 'Coat_Functional Group': ['None', 'PVP', 'Chitosan', 'Poloxamer', 'PVA', 'Citrate',
        'Liposome', 'Silica', 'OleicAcid', 'COOH', 'DPPC', 'NH2', 'CyA',
        'GSH', 'FA', 'Citrate-Lactose', 'Citrate-Oligonucleotide',
        'Dextran'],
 'Synthesis_Method': ['Commercial', 'Chemical Reduction',
        'Emulsion-Solvent Evaporation ', 'Sol-Gel Method',
        'Green Synthesis', 'Reverse Microemulsion',
        'Soft Templating Method', 'Precipitation'],
 'Cell type': ['RAW264.7', 'RAV264.7', 'KEC', 'A431', 'Calu-3', 'A549', 'HepG2',
        'NIH3T3', 'HEK293', 'THP-1', 'SHSY5Y', 'Caco-2', 'A2780', 'MCF-7',
        '16HBE', 'BALB/c3T3', 'NR8383', 'hMSC', 'AGS', '3T3-L1', 'HeLa',
        'PBMC', 'Jurkat', 'IMR90', 'CCL-110', 'RFPEC', 'HCT-116', 'VERO',
        'HDF', 'C6', 'L929', 'HUVEC', 'HaCat', 'TT1', 'Macrophages', 'AT2',
        'HT-1080'],
 'Human_Animal_cells': ['A', 'H'],
 'Cell_Source': ['Mouse', 'Human', 'Rat', 'Monkey', 'Mice'],
 'Cell-organ_tissue source': ['Ascites', 'Skin', 'Lung', 'Liver', 'Embryo', 'Kidney', 'Blood',
        'BoneMarrow', 'Colon', 'Ovary', 'Breast', 'RespiratoryTract',
        'Stomach', 'Cervix', 'FatPad', 'Brain',
        'SubcutaneousConnectiveTissue', 'Umbilical Vein',
        'Connective Tissue'],
 'Cell morphology': ['Monocyte/Macrophage', 'Epithelial', 'Fibroblast', 'Monocyte',
        'Macrophage', 'Spindle', 'Lymphoblast', 'Endothelial',
        'Keratinocyte'],
 'Cell age': ['Adult', 'Embryonic', 'Fetus'],
 'Cell line': ['L', 'P'],
 'Test': ['CellTiterBlue', 'XTT', 'LDH', 'Live/Dead', 'MTS', 'MTT', 'NRU',
        'AlamarBlue', 'CCK-8', 'WST-1', 'CellTiterGlo', 'CoulterCounter'],
 'Test indicator': ['AlamarBlue', 'TetrazoliumSalt', 'LDHrelease', 'PropidiumIodide',
        'CalceinAM', 'NeutralRed', 'LuciferaseEnzyme', 'TrypanBlue',
        'Impedance']}

features_values = {'Coat/Functional Group': ['None', 'PVP', 'Chitosan', 'Poloxamer', 'PVA', 'Citrate',
        'Liposome', 'Silica', 'OleicAcid', 'COOH', 'DPPC', 'NH2', 'FA',
        'Citrate-Lactose', 'Citrate-Oligonucleotide', 'Dextran'],
 'Concentration (ug/ml)': (0.028, 1500.0),
 'Material': ['SiO2', 'Ag', 'TiO2', 'PLGA', 'Pt', 'IronOxide', 'ZnO', 'Au',
        'CuO', 'MgO', 'Polystyrene', 'EudragitRL', 'ZrO2', 'C60', 'C70',
        'MWCNT', 'NiO', 'Ay', 'CeO2', 'Ce O2'], 
 'Shape': ['Sphere', 'Irregular', 'Iregular', 'Rod', 'Star', 'Nanotube',
        'Cubic', 'Round'], 
 'Time (hr)': (3.0, 96.0),
 'Size_in_Water (nm)': (7.0, 889.03),
 'Zeta_in_Water (mV)': (-73.8, 63.8),
 'Cell_Tissue': ['Ascites', 'Skin', 'Lung', 'Liver', 'Embryo', 'Kidney', 'Blood',
        'BoneMarrow', 'Colon', 'Ovary', 'Breast', 'RespiratoryTract',
        'Stomach', 'Cervix', 'FatPad', 'Brain',
        'SubcutaneousConnectiveTissue', 'Umbilical Vein',
        'Connective Tissue'], 
 'No_of_Cells (cells/well)': (2600.0, 350000.0),
 'Cell_Type': ['RAW264.7', 'RAV264.7', 'KEC', 'A431', 'Calu-3', 'A549', 'HepG2',
        'NIH3T3', 'HEK293', 'THP-1', 'SHSY5Y', 'Caco-2', 'A2780', 'MCF-7',
        '16HBE', 'NR8383', 'hMSC', 'AGS', '3T3-L1', 'HeLa', 'IMR90',
        'CCL-110', 'RFPEC', 'HCT-116', 'VERO', 'HDF', 'C6', 'L929',
        'HUVEC', 'HaCat', 'Macrophages', 'AT2', 'HT-1080'], 
 'Diameter (nm)': (4.0, 280.0),
 'Cell_Morphology': ['Monocyte/Macrophage', 'Epithelial', 'Fibroblast', 'Monocyte',
        'Macrophage', 'Spindle', 'Endothelial', 'Keratinocyte'],
 'Cell_Source': ['Mouse', 'Human', 'Rat', 'Monkey', 'Mice'], 
 'Cell_Age': ['Adult', 'Embryonic', 'Fetus'], 
 'Cell Line_Primary Cell': ['L', 'P']}

data_conf = {'coat_functional_froup': 'Coat/Functional Group',
 'concentration': 'Concentration (ug/ml)',
 'shape': 'Shape',
 'time': 'Time (hr)',
 'material': 'Material',
 'cell_tissue': 'Cell_Tissue',
 'size_in_water' :'Size_in_Water (nm)',
 'cell_motphology': 'Cell_Morphology',
 'cell_age': 'Cell_Age',
 'cell_line': 'Cell Line_Primary Cell',
 'cell_type': 'Cell_Type',
 'no_of_cells': 'No_of_Cells (cells/well)',
 'zeta_in_water': 'Zeta_in_Water (mV)',
 'diameter': 'Diameter (nm)',
 'cell_source': 'Cell_Source'}


{
  "coat_functional_froup": "PVP",
  "concentration": 1500.0,
  "shape": "Irregular",
  "time": 96.0,
  "material": "Ag",
  "cell_tissue": "Skin",
  "size_in_water": 889.0,
  "cell_motphology": "Epithelial",
  "cell_age": "Embryonic",
  "cell_line": "P",
  "cell_type": "RAV264.7",
  "no_of_cells": 350000.0,
  "zeta_in_water": 63.8,
  "diameter": 280.0,
  "cell_source": "Human"
}