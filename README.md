Firstly I created venv 
Then created database connection and schema
After that built database with models.py and after that to get and post data in tables I created crud.py and main.py file to create instance decorator for get and post to give and fetch columns to database and run the FastAPI application server with
uvicorn task.main:app --reload
After that I connect it with TablePlus to vreate database using database connection from database.py file.
