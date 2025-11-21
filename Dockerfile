# Use an official Python runtime as a parent image change version if needed
FROM python:3.10 

# Set the working directory in the container
WORKDIR /code

# Copy requirements file to the workingdir
COPY ./requirements.txt /code/requirements.txt

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

#Copy the current directory contents into the container at /code
COPY ./app /code/app

#Expose port 8000 for the app
EXPOSE 8000

# Run the application
# app.server:app should be changed according to your main file and app instance name
# here I am running uvicorn server from app/server.py file and the FastAPI instance is named app (see app/server.py)
CMD ["uvicorn", "app.server:app", "--host", "0.0.0.0", "--port", "8000"]

