# Cows Detector Logger

A simple and colorful logging utility for the Cows Detector project. This logger provides colored output for different log levels and supports both console and file logging.

## Features

- Colored console output for different log levels
- File logging support
- Configurable log levels
- Timestamp in log messages
- Easy to use interface
- Customizable log format
- Log rotation support

## Installation

### Development Installation
```bash
# Clone the repository
git clone https://github.com/yourusername/cows-detector.git
cd cows-detector

# Install the package in development mode
pip install -e .
```

### Direct Installation
```bash
pip install ccmd-logger
```

## Usage

### Basic Usage

```python
from ccmd_logger import Logger

# Create a logger instance
logger = Logger('my_app')

# Log messages with different levels
logger.info('This is an info message')
logger.warning('This is a warning message')
logger.error('This is an error message')
logger.debug('This is a debug message')
```

### With File Logging

```python
from ccmd_logger import Logger

# Create a logger instance with file logging
logger = Logger('my_app', log_file='app.log')

# Log messages will be written to both console and file
logger.info('This message will appear in both console and file')
```

### Advanced Configuration

```python
from ccmd_logger import Logger

# Create a logger with custom configuration
logger = Logger(
    name='my_app',
    log_file='app.log',
    level='DEBUG',  # Set minimum log level
    max_bytes=10485760,  # 10MB
    backup_count=5,  # Keep 5 backup files
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
```

### Log Levels

The logger supports the following log levels (in order of severity):
- `debug`: Detailed information for debugging
- `info`: General information about program execution
- `warning`: Warning messages for potentially harmful situations
- `error`: Error messages for failures
- `critical`: Critical errors that may prevent the program from running

## Example Output

```
2024-03-29 10:30:45 INFO     This is an info message
2024-03-29 10:30:45 WARNING  This is a warning message
2024-03-29 10:30:45 ERROR    This is an error message
2024-03-29 10:30:45 DEBUG    This is a debug message
```

## Dependencies

- Python 3.6 or higher
- coloredlogs >= 15.0.1
- logging (built-in)
- datetime (built-in)

## Configuration Options

| Option       | Type | Default                                     | Description                              |
| ------------ | ---- | ------------------------------------------- | ---------------------------------------- |
| name         | str  | None                                        | Name of the logger                       |
| log_file     | str  | None                                        | Path to log file (optional)              |
| level        | str  | 'INFO'                                      | Minimum log level                        |
| max_bytes    | int  | 10485760                                    | Maximum size of log file before rotation |
| backup_count | int  | 5                                           | Number of backup files to keep           |
| format       | str  | '%(asctime)s - %(levelname)s - %(message)s' | Log message format                       |

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change. 