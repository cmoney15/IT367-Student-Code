# Use the official Python image as the base image
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app
# ^ originally said this: zzzWORKDIR /app

# Copy the application files to the container
COPY . /app
# ^ was commented out for some reason 

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port that Flask will use
EXPOSE 5000
# ^ originally said this: EXPOSE 4567

# Define the command to run the Flask application
CMD ["python", "app.py"]
# ^ originally had the below 2 lines: 
    
#RRRCMD ["python", "app.py"]
#asCMD ["python", "app.py"]


