import os

import camelot
import pandas as pd

pddf=input('Enter pdf path: ')
start_page=int(input('Enter starting page no.: '))
endpage=int(input('Enter End page no.: '))
#range b/w number of pages you want to extract
for i in range(start_page,endpage):
    print('checking page: '+str(i))
    #read pdf with path
    tables = camelot.read_pdf(str(pddf),pages=str(i))
    name=pddf.split('/')[-1].split('.')[0]
    isFile = os.path.isdir(str(name))
    if isFile == False:
        os.mkdir(str(name))
    table_list=[]
    if len(tables)>1:
        for ii in range(0,len(tables)):
            reportt=tables[ii].parsing_report
            print(reportt)
            if reportt['accuracy']>50:
                dff = tables[ii].df
                table_list.append(dff)

    elif len(tables)==1:
        reportt = tables[0].parsing_report

        if reportt['accuracy'] > 70:
            df2 = tables[0].df
            if len(df2)>5:
                df2.to_csv(str(name)+'/pageee'+str(i)+'.csv',index=False)

    if len(table_list)!=[]:
        if len(table_list)==1:
            table_list[0].to_csv(str(name)+'/pageee'+str(i)+'.csv',index=False)
        if len(table_list)>1:
            final_df = pd.concat(table_list, ignore_index=True)
            final_df.to_csv(str(name)+'/pageee' + str(i) + '.csv', index=False)
