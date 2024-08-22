with open('input_file.txt','r') as ipf:#create input file 
    line=ipf.read()# read input file
    word=line.split() # split line into words to perform wordcount
    with open('output_file.txt','w') as opf:
        for i in word: # Here i have iterated through word variable where the split of words are returned 
            opf.write(i+':'+str(word.count(i))+'\n')      
opf=open('output_file.txt','r')
print(opf.read()) #print wordcount
