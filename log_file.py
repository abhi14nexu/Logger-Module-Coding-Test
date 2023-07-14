import os
from datetime import datetime

class LogFile:
    def __init__(self, log_directory: str):
        self.log_directory = log_directory
        self.current_log_file = None
        self.open_log_file()
    
    def open_log_file(self) -> None:
        current_date = datetime.now().strftime("%Y-%m-%d")
        file_name = f"log_{current_date}.txt"
        file_path = os.path.join(self.log_directory, file_name)
        self.current_log_file = open(file_path, "a")
    
    def write(self, message: str) -> None:
        self.current_log_file.write(message + "\n")
    
    def flush(self) -> None:
        self.current_log_file.flush()
    
    def create_new_file(self) -> None:
        self.current_log_file.close()
        self.open_log_file()
    
    def check_midnight_rollover(self) -> bool:
        current_date = datetime.now().strftime("%Y-%m-%d")
        file_date = datetime.strptime(current_date, "%Y-%m-%d")
        return file_date.date() != datetime.strptime(self.get_current_log_file_name(), "%Y-%m-%d").date()
    
    def get_current_log_file_name(self) -> str:
        return os.path.basename(self.current_log_file.name)
