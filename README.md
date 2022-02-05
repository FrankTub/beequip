# Getting Started
Download latest [anaconda version](https://docs.anaconda.com/anaconda/install/windows/) and install this.

Open anaconda prompt and run  

``` bash
conda install -c anaconda flask
conda install pandas
conda install -c conda-forge flask-restful
conda install numpy
conda update --all
conda uninstall numpy
conda install numpy
conda install -c anaconda mkl-service
conda install pandas
```

Found out later that debugging in vsc resulted in error due to missing the conda location in `PATH` windows variable. Add following paths:
```bash
%USERPROFILE%\Anaconda3\Library\bin
%USERPROFILE%\Anaconda3\Scripts
%USERPROFILE%\Anaconda3\condabin
```

Follow along with [example](https://realpython.com/api-integration-in-python/).