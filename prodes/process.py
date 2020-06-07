import pandas as pd
from collections import defaultdict
from dbfread import DBF

def process_gfw_data(gfw_data_path):
    """
    Processes GFW DBase file, usually named similar to "prodes2015merge.dbf"

    :param gfw_data_path: path to DBF file
    :returns: processed data by year in km2
    """
    year_area = defaultdict(int)

    for record in DBF(gfw_data_path):
        year = record['ano']
        area = record['areameters'] / 1e6
        
        year_area[year] += area

    return year_area

def process_multi_year_prodes_shp_file(data_path):
    """
    Processes PRODES DBase file, usually named similar 
    to "yearly_deforestation_2008_2018.dbf"

    :param data_path: path to DBF file
    :returns: processed data by year in km2
    """
    year_area = defaultdict(int)

    for record in DBF(data_path):
        year = str(int(record['ano']))
        year_area[year] += record['areakm']

    return year_area

def process_single_year_prodes_shp_file(data_path):
    """
    Processes single-year PRODES DBase file, usually named similar 
    to "yearly_deforestation_2019.dbf"

    :param data_path: path to DBF file
    :returns: area deforested that year in km2
    """
    area = 0
    for record in DBF(data_path):
        class_name = record['CLASS_NAME']

        # File contains NUVEM (clouds) and d20xx (e.g. d2019) for deforested data
        if class_name != 'NUVEM':
             area += record['aream2'] / 1e6

    return area

def process_combined_files(gfw_data, prodes_multi_year_data, single_year_data):
    """
    Combines data from GFW and PRODES sources.

    :param gfw_data: path to GFW DBF file
    :param prodes_multi_year_data: path to PRODES multi-year SHP DBF file
    :param single_year_data: dict of {year_string: path_to_single_year_file}
    :returns: combined processed data by year in km2
    """

    gfw_data = process_gfw_data(gfw_data)
    prodes_data = process_multi_year_prodes_shp_file(prodes_multi_year_data)
    single_years = {k: process_single_year_prodes_shp_file(v) for k, v in single_year_data.items()}
    
    # Preference PRODES raw over GFW
    return {**gfw_data, **prodes_data, **single_years}

def get_brazil_emissions_data(gcp_data):
    """
    Uses the data from the Global Carbon Project (2019) to extract brazilian emissions from 2000 onward

    :param gcp_data: path to GCP National xls file.
    :returns: carbon (million tons) emitted by Brazil 
    """
    nat_data = pd.read_excel(gcp_data, sheet_name=1, skiprows=16)
    year = nat_data.iloc[:, 0]
    emissions = nat_data['Brazil'] 

    return {str(y): e for y, e in zip(year, emissions) if y >= 2000}

def convert_deforested_to_carbon(deforested_data, basin_size_km2=7e6, carbon_in_basin=150e9):
    return {k: v * carbon_in_basin / basin_size_km2 for k, v in deforested_data.items()}
