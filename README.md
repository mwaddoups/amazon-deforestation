# amazon-deforestation

Code for processing PRODES and GFW data, for my post on Medium.

The notebook Plotting Notebook shows how to replicate the figures - but you will require access to the following data
- [GFW PRODES Deforestation](http://data.globalforestwatch.org/datasets/4160f715e12d46a98c989bdbe7e5f4d6_1)
  - This is a processed dataset combining PRODES data up to 2015. Choose the direct download option.
- [PRODES Raw Data](http://www.dpi.inpe.br/prodesdigital/dadosn/mosaicos/)
  - This is where the raw data for various years is stored. At time of writing, I used the 2018 `PDigital2000_2018_AMZ_shp.zip` file and the 2019 `PDigital_2019_AMZ_shp.zip` file.

To replicate, clone thi repo, download and unzip these files and then update the relative paths in the notebook. There is limited documentation in the code under `prodes/`.

