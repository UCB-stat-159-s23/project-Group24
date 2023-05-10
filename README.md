# The Effect of COVID-19 on U.S. Mobility: An Analysis of Google Community Mobility Reports
Binder: [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/UCB-stat-159-s23/project-Group24.git/HEAD?labpath=main.ipynb)
Jupyter Book: [Link](https://ucb-stat-159-s23.github.io/project-Group24/main.html)

## Abstract
This study investigates the impact of the COVID-19 pandemic on mobility patterns in the United States using Google Community Mobility Reports. The research employs descriptive statistics, time-series analysis, and regression models to analyze the data. In order to understand the mechanism of epidemic spread on the community mobility, we modelled the demand-service relationship using the DQQ model which analyze disruptions and recoveries in complex systems in different contexts. The model can help decision-makers and practitioners develop strategies to mitigate the impact of disruptions, improve the resilience of systems, and enhance the recovery process. Furthermore, the model can be used to evaluate the effectiveness of different policies and interventions aimed at minimizing disruptions and accelerating the recovery process. The analysis results indicate significant changes in mobility patterns during the pandemic, with notable variations across different regions and sectors. The findings have implications for policymakers and future research on the long-term consequences of the pandemic on human mobility.

## Contributions
* Correlation Analysis
* Spatiotemporal Trends Analysis
* Policy and Cases Dependency Analysis
* Social Productivity-Related Mobility Trends
* Mechanism Analysis based on Demand Modeling by proposing the [Double Quadratic Queue (DQQ)](https://github.com/UCB-stat-159-s23/project-Group24/blob/main/Appendix%20A%20-%20DQQ.pdf) Model.

## Installation

This project includes the Makefile support, which can be easily installed by:
`make env`

## File structure
* `data` - Dataset of Google Community Mobility Reports
* `figures` - Figures generated from the analysis
  * `figures/dqq_outputs` - Figures generated from the DQQ model
  *  `figures/illustrations` - Illustration figures for the narrative notebook
* `output` - Output files from the DQQ analysis
* `tools` - Tools used for the analysis
* `main.ipynb` - Narrative notebook
* `main.html`, `_config.yml`, `_toc.yml`, `logo.png` - Required files for the Jupyter Book auto build
...and other files for the integrity and environment setup
