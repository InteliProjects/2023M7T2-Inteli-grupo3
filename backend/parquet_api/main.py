from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import FileResponse, JSONResponse
import boto3
from typing import List
from fastapi.middleware.cors import CORSMiddleware
from tempfile import NamedTemporaryFile
 
app = FastAPI()
 
# Configurando o CORS
app.add_middleware(
  CORSMiddleware,
  allow_origins=["*"],  # Ou substitua "*" pelas origens permitidas (por exemplo, ["https://seusite.com"])
  allow_credentials=True,
  allow_methods=["*"],  # Ou substitua "*" pelos métodos permitidos (por exemplo, ["GET", "POST"])
  allow_headers=["*"],
)
 
# Configuração do cliente S3
s3 = boto3.client(
    's3',
    region_name='us-east-1'
)
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table = dynamodb.Table('raw_parquet_size')
bucket_name = 'parquets'
 
@app.post("/upload/")
async def upload_files(files: List[UploadFile]):
    try:
        og_item = table.get_item(Key={'id': '0'})
        last_size = int(og_item['Item']['last_size'])
        for file in files:
            s3.upload_fileobj(file.file, bucket_name, file.filename)
            last_size += 1
        if last_size > 4:
            last_size = 0

        table.update_item(
            Key={'id': '0'},
             UpdateExpression='SET last_size = :last_size',
        ExpressionAttributeValues={
            ':last_size': last_size
        }
)

        return JSONResponse(content={"message": "Files uploaded successfully"})
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)
 
@app.get("/download/{file_name}")
async def download_file(file_name: str):
    try:
        # Faz o download do arquivo do S3
        response = s3.get_object(Bucket=bucket_name, Key=file_name)
        data = response['Body'].read()
        with NamedTemporaryFile(delete=False) as temp_file:
           temp_file.write(data)
           temp_file.seek(0)
           return FileResponse(temp_file.name,
                media_type='application/octet-stream', 
                headers={
                    'Content-Disposition': f'attachment; filename={temp_file.name}'
                    }
           )
    except Exception as e:
        return {"error": str(e)}
    
@app.get("/list/")
async def list_objects():
    try:
        # Lista todos os objetos no bucket
        response = s3.list_objects(Bucket=bucket_name)
        objects = [obj['Key'] for obj in response.get('Contents', [])]
        return {"objects": objects}
    except Exception as e:
        return {"error": str(e)}
 
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)