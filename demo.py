# # below code is to check the logging config
# from src.logger import logging

# logging.debug("This is a debug message.")
# logging.info("This is an info message.")
# logging.warning("This is a warning message.")
# logging.error("This is an error message.")
# logging.critical("This is a critical message.")

# # below code is to check the exception config
# from src.logger import logging
# from src.exception import myException
# import sys

# try:
#     a = 1+'Z'
# except Exception as e:
#     logging.info(e)
#     raise myException(e, sys) from e

from src.pipeline.training_pipeline import TrainPipeline

pipeline = TrainPipeline()
pipeline.run_pipeline()