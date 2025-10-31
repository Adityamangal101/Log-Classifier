import pandas as pd
from fastapi import FastAPI, UploadFile, HTTPException
from fastapi.responses import FileResponse

from src.classify import classify

import logging
from datetime import datetime
import os

# Ensure logs directory exists
os.makedirs("logs", exist_ok=True)

# Configure logging to file
logging.basicConfig(
    filename=f"logs/app_{datetime.now().strftime('%Y%m%d')}.log",
    level=logging.INFO,
    format='[%(levelname)s] %(asctime)s - %(message)s',
)

# Optional: also print to console
console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter('[%(levelname)s] %(asctime)s - %(message)s')
console.setFormatter(formatter)
logging.getLogger().addHandler(console)

app=FastAPI()

@app.post("/classify")
async def classify_logs(file: UploadFile):
    logging.info(f"Received file: {file.filename}")

    if not file.filename.endswith('.csv'):
        logging.error("Invalid file type uploaded.")
        raise HTTPException(status_code=400,detail="File must be a csv.")

    try:
        # Read the uploaded csv
        df=pd.read_csv(file.file)
        logging.info(f"CSV loaded successfully with {len(df)} rows.")

        if "source" not in df.columns or "log_message" not in df.columns:
            logging.warning("Missing required columns in CSV.")
            raise HTTPException(status_code=400,detail="Csv must have 'source' and 'log_message' columns.")

        # Perform classification
        df["target_label"]=classify(list(zip(df['source'],df['log_message'])))

        # Save the modified file
        output_file='testing/new_output.csv'
        df.to_csv(output_file,index=False)
        logging.info(f"Classification completed. File saved to {output_file}")
        return FileResponse(output_file,media_type='test/csv')
    except Exception as e:
        logging.exception("Error occurred during classification:")
        raise HTTPException(status_code=500, detail=str(e))
    
        
