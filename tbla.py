import csv
import tabula

#convert them into CSV
df1 = tabula.convert_into("file1.pdf","file1.csv", output_format="csv",pages='all')
df2 = tabula.convert_into("file2.pdf","file2.csv", output_format="csv",pages='all')

# compare the two dataframes and create a third dataframe with the differences
diff = df1 != df2
df3 = df1[diff]

# write the third dataframe to a CSV file
df3.to_csv('output.csv', index=False)
