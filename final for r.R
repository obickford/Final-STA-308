#############
##
## Olivia Bickford
## May 8, 2022
##
## This is the R final for STA 308. 
## By taking the unemployment data from March 2021 to March 2022, census regions and the 
##   state maps data I found the mean and standard deviation for the differences
##   in state unemployment from March of 2021 to March of 2022. Using this I found 
##   the coefficient of variation for each census region which includes Northeast, 
##   Midwest, South, and West. 
##


## load data
census_data <- read.csv("censusRegions.csv")
unemployment_data <- read.csv("marchStateUnemployment.csv") 
state_mapping_data <- read.csv("state_abb_codes.csv")

library(tidyverse) #load package

updated_cenus_data <- census_data %>%
  slice(-28)  ##update data to get rid of D.C

updated_statedF <- merge(state_mapping_data, unemployment_data) ## merge two data sets with state name

merged_regions_data <- merge(updated_statedF, updated_cenus_data,
                     by.x= 'Code', by.y= 'State') ## take combined data and merge with state code

cenus_regions_data <- merged_regions_data %>% 
  group_by(State) %>% # group by state first to find difference in rates 
  mutate(difference_in_rates = March_21 - March_22) %>% #set up difference rate variable 
  group_by(Region) %>%  # after the new variable group by the region to...
  summarise (mean_of_diff = mean(difference_in_rates), ##find the mean difference 
             sd_of_diff = sd(difference_in_rates), ## find the standard deviation of these means
             CoV_ofdiff = (sd_of_diff/mean_of_diff)*100) #coefficient of variation using previous variable above

