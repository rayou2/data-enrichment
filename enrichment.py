## pip install pandas
import pandas as pd 

# load in the data 

sparcs = pd.read_csv('data/SPARCS_2015.csv', low_memory=False)
#cleaning column names
sparcs.columns = sparcs.columns.str.replace('[^A-Za-z0-9]+', '_')
#checking column names
sparcs.columns

atlas = pd.read_csv('data/NY_2015_ADI_9 Digit Zip Code_v3.1.csv',low_memory=False)
#check column names
atlas.columns

#choosing the data from neighborhood to enrich data with atlas in sparcs
sparcs_small = sparcs[['Zip_Code_3_digits', 'Gender', 'Length_of_Stay', 'Type_of_Admission', 'Total_Costs']]
print(sparcs_small.sample(10).to_markdown()) 

atlas_small = atlas[['ZIPID','GISJOIN', 'ADI_NATRANK', 'ADI_STATERNK']]
print(atlas_small.sample(10).to_markdown()) 

#merge data
combined_df = sparcs_small.merge(atlas_small, how='left', left_on='Zip_Code_3_digits', right_on='ZIPID')
combined_df = combined_df.drop(columns=['ZIPID'])
#check merged data columns 
combined_df.columns
#Drop duplicates based on zip code
combined_df_nodups = combined_df.drop_duplicates(subset=['Zip_Code_3_digits'])
#save merged data as a new csv
combined_df.to_csv('enriched/combined.csv')
