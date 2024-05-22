import logging
import pandas as pd
import time 
import os

# get time 
current_time = time.strftime("%Y%m%d%H%M%S", time.localtime())

# Configure logger name and level (adjust as needed)
logger_name = __name__  # Use the module name as the logger name
log_level = logging.INFO

# write log in to folder

log_dir = "./logs"  # Replace with your desired directory
# Create the directory if it doesn't exist
os.makedirs(log_dir, exist_ok=True)

log_file = os.path.join(log_dir, f'{current_time}_app.log')

# log_format = ('\n'
#               '================================================================\n'
#               '%(asctime)s - %(levelname)s - %(name)s - [%(funcName)s:%(lineno)d]\n'
#               'Message: %(message)s\n'
#               '----------------------------------------------------------------\n')

log_format = ('\n'
            #   '================================================================\n'
              '%(asctime)s - %(levelname)s - %(name)s - [%(funcName)s:%(lineno)d]\n'
              '%(message)s\n')
            #   '----------------------------------------------------------------\n')

logging.basicConfig(
    filename=log_file,
    level=log_level,
    format=log_format
)

# Get the logger instance
logger = logging.getLogger(logger_name)


# Define the log_io decorator

def log_io(func):
    # @wraps(func)
    def wrapper(*args, **kwargs):
        # Capture the start time
        start_time = time.time()

        # Log function input details
        logger.info(f"Function {func.__name__} called with {len(args)} positional arguments and {len(kwargs)} keyword arguments.")
        
        for i, arg in enumerate(args):
            if isinstance(arg, pd.DataFrame):
                logger.info(f"Function {func.__name__} - Argument {i}: DataFrame with shape: {arg.shape}")
                # logger.info(f"Function {func.__name__} - Argument {i}: DataFrame with columns: {arg.columns.tolist()} and shape: {arg.shape}")
            else:
                logger.info(f"Function {func.__name__} - Argument {i} ({type(arg)}): {arg}")
        
        for k, v in kwargs.items():
            if isinstance(v, pd.DataFrame):
                logger.info(f"Function {func.__name__} - Keyword argument {k}: DataFrame with shape: {v.shape}")
                # logger.info(f"Function {func.__name__} - Keyword argument {k}: DataFrame with columns: {v.columns.tolist()} and shape: {v.shape}")
            else:
                logger.info(f"Function {func.__name__} - Keyword argument ({type(v)}) {k}: {v}")

        # Call the function and get the result
        result = func(*args, **kwargs)

        # Log function output details   
        if isinstance(result, pd.DataFrame):
            logger.info(f"Function {func.__name__} returned a DataFrame with shape: {result.shape}")
        else:
            logger.info(f"Function {func.__name__} returned ({type(result)})")
            # logger.info(f"Function {func.__name__} returned ({type(result)}): {result}")

        # Capture the end time and calculate execution duration
        end_time = time.time()
        duration = end_time - start_time
        logger.info(f"Function {func.__name__} executed in {duration:.4f} seconds")

        return result
    return wrapper