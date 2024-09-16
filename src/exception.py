class DataIngestionError(Exception):
    
    def __init__(self, message: str):
        self.msg = message
    
    def __str__(self):
        return self.msg


class DataTransformationError(Exception):
    
    def __init__(self, message: str):
        self.msg = message
    
    def __str__(self):
        return self.msg