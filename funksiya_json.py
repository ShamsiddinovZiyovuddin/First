import json
import os

def create_data(data:None,file_name:str,status:str):
    with open(f"{file_name}",f"{status}") as file:
        if status=="r":
         x=json.load(file)
         return x
        else:
            if os.path.exists(file_name):
                with open(file_name, status) as file:
                    x=json.dump(data,file,indent=4)
                return "ok"
