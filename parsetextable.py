import numpy as np

def parsetextable(tablein,ecolumns):
    size1=tablein.shape
    nrows, ncolumns, necolumns = size1[0], size1[1], len(ecolumns)
    temparray=np.zeros((nrows,necolumns*3))
    for i in range (0,necolumns):
        for j in range (0,nrows):
            temp=tablein[j,ecolumns[i]]
            temp=temp.translate(None, '$ {}_^')#remove special characters
            if 'pm' in temp:
                temp2=temp.split('\pm')
                temparray[j,i*3]=np.float(temp2[0])
                temparray[j,i*3+1],temparray[j,i*3+2]=np.float(temp2[1]),np.float(temp2[1])
            elif '+' in temp:
                temp2=temp.split('-')
                gruh=len(temp2)
                if gruh == 3:
                    temp2[0]='-'+temp2[1]
                    temp2[1]=temp2[2]
                if not '+' in temp2[0]:
                    temparray[j,i*3]=np.float(temp2[0])
                    temp3=temp2[1].split('+')
                    temparray[j,i*3+1]=np.float(temp3[0])
                    temparray[j,i*3+2]=np.float(temp3[1])
                else:
                    temparray[j,i*3+2]=np.float(temp2[1])
                    temp3=temp2[0].split('+')
                    temparray[j,i*3]=np.float(temp3[0])
                    temparray[j,i*3+1]=np.float(temp3[1])
            elif '<' in temp:
                temp=temp.translate(None, '<')
                temparray[j,i*3]=np.float(temp)
                temparray[j,i*3+2]=np.float(temp)
            elif temp != '':
                temparray[j,i*3]=np.float(temp)

    return temparray
 
