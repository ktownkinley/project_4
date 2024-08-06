from pymongo import MongoClient
import gridfs
import os

folder_path = 'C:\\Users\\mckin\\Documents\\chest_xray_data\\chest_xray\\train\\PNEUMONIA'

# Establish connection to MongoDB
client = MongoClient('') #redacted
db = client['xraydb']

# Create a GridFS object
fs = gridfs.GridFS(db, "pneumonia")

# List all files in the folder
for index, filename in enumerate(os.listdir(folder_path)):
    if index > 250:
        print("Hit 250 images!")
        break
    file_path = os.path.join(folder_path, filename)
    # Check if it's a file (not a directory)
    if os.path.isfile(file_path):
        print(f"Processing file: {filename}")
        # Open the image file in binary mode and store it in GridFS
        with open(file_path, 'rb') as file:
            fs.put(file, filename=filename)
        print(f"Image {index} stored successfully!")
        print(f"{round(((index / 250)*100), 2)}% complete!")
