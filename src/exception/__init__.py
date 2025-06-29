import sys
import logging

def error_message_detail(error: Exception, error_detail: sys) -> str:
    """
    Extracts detailed error information including file name, line numberm and the error message.

    :param error: The exception that occurred.
    :param error_detail: The sys module to access traceback details.
    :return: A formatted error message string.
    """

    # Extract traceback details (exception information)
    _, _, exc_tb = error_detail.exc_info()
    
    # Get the filename where the execption occurred
    filename = exc_tb.tb_frame.f_code.co_filename

    # Create a formatted error message string with filename, line number and the actual error
    line_num = exc_tb.tb_lineno
    error_msg = f"Error occurred in python script: [{filename}] at line number [{line_num}]: {str(error)}"

    # Log error for better tracking
    logging.error(error_msg)

    return error_msg

class myException(Exception):
    """
    Custom exception class for handling errors in the US visa application.
    """
    def __init__(self, error_message:str, error_detail: sys):
        """
        Initializes the USvisaException with a detailed error message.

        :param error_message: A string describing the error.
        :param error_detail: The sys module to access traceback details.
        """
        # Call the base class constructor with the error message
        super().__init__(error_message)

        # Format the detailed error message using the error_message_detail function
        self.error_message = error_message_detail(error_message, error_detail)

    def __str__(self) -> str:
        """
        Returns the string representation of the error message.
        """
        return self.error_message