import os
import glob
import pandas as pd
import sys
from pathlib import Path

# DETECT THE POSITION OF MUTATIONS
run = pd.read_csv('run_1.csv', sep='\t')
artic = pd.read_csv('artic_ncov.csv', sep=',')

# print(run)
# print(artic)

pos_run = [i for i in run['POS']]
pos_start_artic = [i for i in artic['POS_START']]
pos_end_artic = [i for i in artic['POS_END']]
strand = [i for i in artic['STRAND']]

# print(pos_run)
# print(pos_start_artic)
# print(pos_end_artic)

for j,k,l in zip(pos_start_artic, pos_end_artic, strand):
    for i in pos_run:
        if i in range(j, k, 1):
            with open('run_1_mutation.txt', 'a') as f:
                f.writelines('There is a mutation here: ' +str(i)+
                      ', located inside: '+str(j)+'-'+str(k) +', Primer Name: '+ str(l) + '\n')


# MAIN ANALYSIS OF VCF FILES

data = pd.read_csv('run_1.csv', sep='\t')

run_main = {'CHROM':[i for i in data['CHROM']],
                    'POS':[i for i in data['POS']],
                   'ID':[i for i in data['ID']],
                    'REF':[i for i in data['REF']],
                   'ALT':[i for i in data['ALT']],}
main_data = pd.DataFrame(run_main)


#EVERY BARCODE IN EVERY RUN
barcode = []
for i in list(data):
   if 'barcode' in i:
      barcode.append(i)

# print(list(data))
#
run_barcode = {}

for i,j in zip(data, barcode):
   run_barcode[j] = [i for i in data[j]]

df_barcode = pd.DataFrame(run_barcode)

print(main_data)
print(df_barcode)

final_data = pd.concat([main_data, df_barcode], axis=1)
print(final_data)

final_data.to_excel('run_1.xlsx', index=False)

#COMBINE ALL CSV INTO ONE SINGLE EXCEL FILE

# extension = 'csv'
# all_filenames = [i for i in glob.glob("./final_data_mutation_nsp1/*.csv")]
#
# writer = pd.ExcelWriter('FRAMESHIFT_FINAL_DATA_FULL_BARCODE_3.xlsx')
# for i in all_filenames:
#      txt = Path(i).read_text()
#      txt = txt.replace(',', '.')
#
#      text_file = open(i, "w")
#      text_file.write(txt)
#      text_file.close()
#
#      print(i[27:])
#      df = pd.read_csv(i, sep=';', encoding='utf-8')
#      df.to_excel(writer, sheet_name=os.path.splitext(i[27:])[0], index=False)
# writer.save()





