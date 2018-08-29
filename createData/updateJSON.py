import pandas as pd
import json
import uuid
import sys, getopt
import os
import zipfile

def zipdir(path, ziph):
    # ziph is zipfile handle
    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file))
            
def main(argv):
    try:
        botname = sys.argv[1]
    except:
        print('Please provide the bot name as input parameter')
        sys.exit(2)
    inputpath = 'input/' + botname + '/intents/'
    outputpath = 'output/' + botname + '/intents/'
    
    pathToFile = 'input/' + botname + '_IntentList.csv'
    df = pd.read_csv(pathToFile, encoding='utf-8-sig', delimiter=';') #encoding is utf-8-sig
    #df.loc[:, 'UUID'] = 1
    #df.loc[:, 'UUID'] = df.groupby("name").UUID.transform(lambda g: uuid.uuid4())
    
    #looping over the existing intents from intentList.csv and read the according training sets from text files
    for index, row in df.iterrows():
        name = row['name']
        trainingFile = open('input/' + botname + '_Training/trainingInput' + name + '.txt', 'r')
        trainSet = [line for line in trainingFile.readlines()] 
    
        answer = row['answer_de']
    
    #    with open('input/Messebot/intents/request.' + name + '.json') as f:
    #        topdict = json.load(f)
    #    messagedict = {"type": 0, "lang": "de", "speech": answer}
    #    responsedict['messages'] = [messagedict]
    #   
    #    topdict['name'] = 'request.' + name
    #    topdict['auto'] = 'true'
    #    topdict['responses'] = [responsedict]
    #   
    #    #mydict['id'] = uuid
    
    
#        with open(inputpath + 'request.' + name + '.json') as f:
#            data = json.load(f)
#        tempdict = dict(data)
#        tempdict.update(topdict)
#        
#        with open(outputpath + 'request.' + name + '.json', 'w', encoding='utf-8-sig') as f:
#            json.dump(tempdict, f, indent=4, ensure_ascii=False)
    
        with open(inputpath + 'request.' + name + '_usersays_de.json', 'r', encoding='utf-8-sig') as f:
            traindata = json.load(f)
        for sent in trainSet:
            traindata.append({"data": [{"text": sent}]})
        with open(outputpath + 'request.' + name + '_usersays_de.json', 'w', encoding='utf-8-sig') as f:
            json.dump(traindata, f, indent=4, ensure_ascii=False)
            
    zipf = zipfile.ZipFile(botname + '.zip', 'w', zipfile.ZIP_DEFLATED)
    zipdir('output/' + botname, zipf)
    zipf.close()
    print('Files are updated for ' + str(sys.argv[1]) )
        
if __name__ == "__main__":
   main(sys.argv[1:])      
        
        
        
        
        
        