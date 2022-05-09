# -*- coding: utf-8 -*-
"""
Created on Wed May  4 14:56:00 2022

@author: livib

This is the Python code for the Final midterm.
By taking the unemployment data from March 2021 to March 2022, census regions and the 
state maps data I found the mean and standard deviation for the differences in state unemployment
from March of 2021 to March of 2022. Using this I found the coefficient of variation
for each census region which includes Northeast, Midwest, South, and West. 

"""

import pandas as pd

## load csv files 
census_data = pd.read_csv("C:\\Users\\livib\\OneDrive\\STA 308\\Final-STA-308\\censusRegions.csv")
unemployment_data = pd.read_csv("C:\\Users\\livib\\OneDrive\\STA 308\\Final-STA-308\\marchStateUnemployment.csv")
state_mapping_data = pd.read_csv("C:\\Users\\livib\\OneDrive\\STA 308\\Final-STA-308\\state_abb_codes.csv")

updated_cenus_data = census_data[census_data.State != "DC"] ## remove DC

updated_stateDF = state_mapping_data.merge(unemployment_data) # merge data frames togehter

merged_regions_data = updated_stateDF.merge( ## take updated frame and merged with cenus data by code and state
    updated_cenus_data, left_on="Code", right_on="State").drop('State_y', 1) ## drop the second state column

diff_in_rates = merged_regions_data.assign( ##make difference variable by using assign and subtracting the two variables
    difference_in_rates = merged_regions_data.March_21-merged_regions_data.March_22)


mean_of_diff = diff_in_rates.groupby('Region')['difference_in_rates'].agg('mean').to_frame()
## group by Region and use aggregate for the mean and turn into data frame
sd_of_diff = diff_in_rates.groupby('Region')['difference_in_rates'].agg('std').to_frame()
## do the same as above but for the standard deviation and turn into data frame

merged_stats = mean_of_diff.merge(sd_of_diff, left_on="Region", right_on="Region")
## merge the two data frames with the mean and standard deviation

final_cenus_stats = merged_stats.assign(Cov_diff = (sd_of_diff/mean_of_diff)*100)
## make new variable with the merged dataframe for the coefficient of variation

final_cenus_stats = final_cenus_stats.rename(columns = {'difference_in_rates_x' : 'mean_of_diff', 'difference_in_rates_y' : 'sd_of_diff'})
## change column names 

final_cenus_stats
## final 4x3 dataframe 
