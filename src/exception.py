import sys
from src.logger import logging

def error_message_details(error,error_detail:sys):
    _,_,exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    line_number = exc_tb.tb_lineno
    error_message = f"Error occured in script: [{file_name}] at line number: [{line_number}] error message: [{str(error)}]"
    return error_message

class CustomException(Exception):
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_message_details(error_message,error_detail)

    def __str__(self):
        return self.error_message
    

"""
The above code defines a custom exception class `CustomException` that inherits from the built-in `Exception` class.
It includes a method `error_message_details` that extracts details about the error, such as the file name and line number where the error occurred, and formats this information into a string.
The `__str__` method is overridden to return the formatted error message when the exception is printed.
This custom exception can be used throughout the application to provide more detailed error messages for debugging purposes.
"""