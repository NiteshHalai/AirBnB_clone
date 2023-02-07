#!/usr/bin/python3

from datetime import datetime
import uuid

"""
This is a BaseModel class
"""


class BaseModel:

    """
    This is a BaseModel class
    """
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
    
    def __str__(self):
        return 'dummy'

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self): 
        return 'dummy'


#!/usr/bin/python3

from datetime import datetime
import uuid

"""
This is a BaseModel class
"""


class BaseModel:

    """
    This is a BaseModel class
    """
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
    
    def __str__(self):
        return 'dummy'

    def save(self):
        self.updated_at = datetime.now()

    def to_dict(self): 
        return 'dummy'



my_model = BaseModel()
my_model.name = "My First Model"
my_model.my_number = 89
print(my_model)
my_model.save()
print(my_model)
my_model_json = my_model.to_dict()
print(my_model_json)
print("JSON of my_model:")
for key in my_model_json.keys():
    print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))
    
