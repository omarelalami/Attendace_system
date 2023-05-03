# Set the base image
FROM python:3.10

# Set the working directory in the container
WORKDIR /app

# Copy the `requirements.txt` file to the container
COPY requirements.txt .

# Upgrade pip and install the Python dependencies
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code to the container
COPY . .

# Specify the command to run the application
CMD ["python", "main.py"]
