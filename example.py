from ccmd_logger.src import Logger

def example_function():
    # Get the logger instance with a specific name
    logger = Logger('cows_detector')
    
    # Basic logging examples
    logger.info("Starting the example function...")
    
    # Example with different log levels
    logger.debug("This is a debug message (won't show because level is INFO)")
    logger.info("This is an info message")
    logger.warning("This is a warning message")
    logger.error("This is an error message")
    logger.critical("This is a critical message")
    
    # Example with exception logging
    try:
        # Simulate an error
        result = 10 / 0
    except Exception as e:
        logger.exception("An error occurred while dividing by zero")
    
    logger.info("Example function completed!")

def another_function():
    # Get a different logger instance for a different component
    logger = Logger('data_processor')
    logger.info("Starting another function...")
    
    # Example with multiple log messages
    for i in range(3):
        logger.info(f"Processing step {i+1}")
    
    logger.info("Another function completed!")

if __name__ == "__main__":
    # Example of using different loggers in the same program
    main_logger = Logger('main')
    main_logger.info("=== Starting the example program ===")
    
    # Call example functions
    example_function()
    another_function()
    
    # End the program
    main_logger.info("=== Program completed successfully ===")
