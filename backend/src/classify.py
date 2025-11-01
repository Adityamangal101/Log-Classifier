from src.processor_regex import classify_with_regex
from src.processor_ML import classify_with_bert
from src.processor_llm import classify_with_llm
import pandas as pd

def classify(logs):
    labels=[]
    for source, log_msg in logs:
        label=classify_log(source,log_msg)
        labels.append(label)

    return labels

def classify_log(source,log_msg):
    if source=="LegacyCRM":
        label=classify_with_llm(log_msg)
        return label
    else:
        label=classify_with_regex(log_msg)
        if label is None:
            label=classify_with_bert(log_msg)
            return label
        else:
            return label
        
def classify_csv(input_file):
    df=pd.read_csv(input_file)
    #Perform classification
    df["target_label"]= classify(zip(df["source"],df['log_message']))
       
    df.to_csv("Outputs/output.csv",index=False)

if __name__=="__main__":
    classify_csv('testing/test.csv')