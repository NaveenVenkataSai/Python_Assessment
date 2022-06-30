import pandas as p

file1=p.read_csv("./data/factbook-2.csv",sep=';')
file1=file1.iloc[1:]
file2=p.read_csv("./data/factbook.csv",sep=';')
file2=file2.iloc[1:]


out=p.concat([file2,file1])

out.drop_duplicates(ignore_index=True)
out.to_csv('./temp/temp.csv')

temp_out=p.read_csv('./temp/temp.csv')
temp_out.fillna(0.00,inplace=True)
temp_out['group_by_key']=temp_out['Country'].str[0]
temp_out=temp_out.drop(columns=['Country'])
temp_out=temp_out.loc[:, ~temp_out.columns.str.contains('^Unnamed')]

group_out=temp_out.groupby('group_by_key').mean()
group_out.to_csv('./output/output.csv')
p.read_csv('./output/output.csv')






