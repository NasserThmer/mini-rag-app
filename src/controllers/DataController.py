from .BaseController import BaseController
from fastapi  import UploadFile

class DataController(BaseController):
    def __init__(self):
        super().__init__()
        self.size_scale = 1024 * 1024
    def validate_upload_file(self, file : UploadFile):
        if file.content_type not in self.app_settings.FILE_ALLOWED_TYPES:
            # raise ValueError(f"File type {file.content_type} is not allowed.")
            return False
        if file.size > self.app_settings.FILE_MAX_SIZE * self.size_scale:
            # raise ValueError(f"File size {file.size} exceeds the maximum allowed size of {self.app_settings.FILE_MAX_SIZE}.")
            return False
        
        return True
