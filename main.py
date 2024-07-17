import os
import asyncio

from add_regularExpressions import regex_rule
from src.componnents.data_validate import validate_dataframe, save_invalid_rows
import uvicorn
from fastapi import FastAPI, File, UploadFile, Request
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import pandas as pd
import io
import uuid  # generator random error names

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


# upload route
@app.post("/upload")
async def upload_file(request: Request, file: UploadFile = File(...)):
    try:
        if file.filename == '':
            return templates.TemplateResponse("index.html", {"request": request, "error": "No file selected"})

        content = await file.read()
        df = pd.read_excel(io.BytesIO(content))

        # Exp Regs
        regex_rules = regex_rule

        valid_rows, invalid_rows, first_row_types, error_columns = validate_dataframe(df, regex_rules)

        if not invalid_rows.empty:
            # generate name for error file
            error_file_name = f"invalid_rows_{uuid.uuid4()}.xlsx"
            error_file_path = os.path.join("static", "uploads", error_file_name)
            save_invalid_rows(invalid_rows, error_file_path, df, first_row_types, error_columns)

            error_file_url = f"/static/uploads/{error_file_name}"

            # delete after 15 sec
            asyncio.create_task(schedule_file_deletion(error_file_path))

            return templates.TemplateResponse("index.html", {
                "request": request,
                "error": "Invalid rows found.",
                "error_file_url": error_file_url
            })

        return templates.TemplateResponse("index.html", {
            "request": request,
            "success_message": "The Excel file is correct."
        })

    except Exception as ex:
        return templates.TemplateResponse("index.html", {
            "request": request,
            "error": f"Error processing the file: {ex}"
        })

# Function to schedule the deletion of a file after 15 seconds
async def schedule_file_deletion(file_path):
    await asyncio.sleep(15)
    try:
        os.remove(file_path)
        print(f"Deleted file: {file_path}")
    except Exception as e:
        print(f"Error deleting file {file_path}: {e}")

# run main
if __name__ == "__main__":
    try:
        uvicorn.run(app, host="localhost", port=8000)
    except KeyboardInterrupt:
        print("Server shutdown requested, stopping...")