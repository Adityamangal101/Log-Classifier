from dotenv import load_dotenv
from groq import Groq
load_dotenv()

groq=Groq()
def classify_with_llm(log_msg):
    prompt=f'''Classify the log message into one of these categories:
               (1) Workflow Error, (2) Deprecation Warning.
                If you can't figure out a category , return "Unclassified".
                Only return The category name, no preamble.
                log message: {log_msg}'''
    chat_completion = groq.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ]
        
    )

    return chat_completion.choices[0].message.content

if __name__=="__main__":
   print( classify_with_llm("Hello how are you"))
   print( classify_with_llm("Lead conversion failed for prospect ID 7842 due to missing contact information."))
   print( classify_with_llm("API endpoint 'getCustomerDetails' is deprecated and will be removed in version 3.2. Use 'fetchCustomerInfo' instead."))
   print( classify_with_llm("The 'ExportToCSV' feature is outdated. Please migrate to 'ExportToXLSX' by the end of Q3."))
   print( classify_with_llm("nova.osapi_compute.wsgi.server [req-b9718cd8-f65e-49cc-8349-6cf7122af137 "))
   print( classify_with_llm("File data_6169.csv uploaded successfully by user User953."))
   print( classify_with_llm("The 'ExportToCSV' feature is outdated. Please migrate to 'ExportToXLSX' by the end of Q3."))