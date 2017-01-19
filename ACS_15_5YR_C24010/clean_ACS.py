import pandas as pd

df_input = pd.read_csv('ACS_15_5YR_C24010_with_ann.csv')

census_tracts = []
counts = []
for index, row in df_input.iterrows():
	if index != 0:
		counts.append(int(row['HD01_VD43']))
		county_code = row['GEO.id2'][3:5]
		tract_code = row['GEO.id2'][5:]
		if county_code == '61':
			census_tracts.append('1' + tract_code)
		if county_code == '05':
			census_tracts.append('2' + tract_code)
		if county_code == '47':
			census_tracts.append('3' + tract_code)
		if county_code == '81':
			census_tracts.append('4' + tract_code)

df_output = pd.DataFrame({'census_tract':census_tracts, 'count':counts})
df_output.to_csv('stem_women.csv', index=False)