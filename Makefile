## Makefile to build JupyterBook for this repository

## env: creates and configures the environment.
## html: build the JupyterBook normally (calling jupyterbook build .). Note this build can only be viewed if the repository is cloned locally, or with the VNC desktop on the Hub.
## all: execute notebooks
## clean: clean up the figures
## help: display descriptions

.PHONY : env
env :
	source /srv/conda/etc/profile.d/conda.sh
	conda env create -f environment.yml 
	conda activate final project
	conda install ipykernel
	python -m ipykernel install --user --name final project

.PHONY : html
html: 
	jupyter-book build . 

.PHONY: all
all:
	jupyterbook execute *.ipynb

.PHONY : clean
clean:
	rm -rf figures/*

.PHONY : help
help : Makefile
	@sed -n 's/^##//p' $<