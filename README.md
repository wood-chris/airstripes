# Instructions

The data in the Excel file shows the concentration of particulate matter air pollution (PM2.5) in cities around the world. Very few historical observations of PM2.5 exist before the year 2000 so instead we use data produced from a mix of computer model simulations and satellite observations.

## Install anaconda

1. Visit https://www.anaconda.com/products/individual in your web browser.
2. Download the Anaconda Python 3 installer for macOS. These instructions assume that you use the graphical installer .pkg file.
3. Follow the Anaconda Python 3 installation instructions. Make sure that the install location is set to “Install only for me” so Anaconda will install its files locally, relative to your home directory. Installing the software for all users tends to create problems in the long run and should be avoided.

## Make sure environment is activated

1. Clone this repo: `git clone git@github.com:wood-chris/airstripes.git`
2. `cd` into the repo
3. check that the conda _base_ environment is activated (does the prompt include `(base)`)? If not, run `conda activate base`

## Playing with the code

1. Running the python code for the barchart should just work!

```
python bar_race_chart_with_plotly.py
```

  This should open a graph in your web-browser (and generate a file called `racechart.html`)

  This graph is interactive - click the play button below the graph. 

2. Do you understand (at a high level, not necessarily every line) the code? Can you change the behaviour of the code by changing bits of it?
3. Can you change what the graph looks like? All the possible arguments for a `plotly` bar chart are documented at https://plotly.com/python-api-reference/generated/plotly.express.bar.html
4. Could you think of a different way of visualising the data? You might get inspiration at https://plotly.com/python/ (clicking an image will show you the code used to generate that graph)

## Another plotting library

1. `matplotlib` is another plotting library in python, but doesn't support animated graphs. It has some examples at https://matplotlib.org/stable/gallery/index
2. Can you create a graph using `matplotlib` instead of `plotly`?
