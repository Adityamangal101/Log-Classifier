from sentence_transformers import SentenceTransformer
import joblib

# Load the sentence transformer model to compute log_message embedding
transformer_model=SentenceTransformer('all-MiniLM-L6-v2')

#Load the saved classification model
classifier_model=joblib.load('models/log_classifier.joblib')

def classify_with_bert(log_message):
   
    #Compute embeddings for the log message
    msg_embedding=transformer_model.encode(log_message)

    #Perform classification using the loaded model
    probablities= classifier_model.predict_proba([msg_embedding])[0]
    if max(probablities)>=0.5:
        predicted_class=classifier_model.predict([msg_embedding])[0]
    else:
        predicted_class="Unknown"

    # Return the predicted clas
    return predicted_class

if __name__=="__main__":
    print(classify_with_bert("Email server encountered a sending fault"))
    print(classify_with_bert("Account with ID 5351 created by User634."))
    print(classify_with_bert("Alert: brute force login attempt from 192.168.80.114 detected"))
    print(classify_with_bert("Denied access attempt on restricted account Account2682"))
    print(classify_with_bert("Hey How are you"))
    print(classify_with_bert("Email service affected by failed transmission"))
    print(classify_with_bert("Lead conversion failed for prospect ID 7842 due to missing contact information."))
    print(classify_with_bert("API endpoint 'getCustomerDetails' is deprecated and will be removed in version 3.2. Use 'fetchCustomerInfo' instead."))
