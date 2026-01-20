import logging
from datetime import datetime
from pathlib import Path


class Logger:
    """Logging utility for the compiler"""

    def __init__(self, name: str = "SQLCompiler", log_file: str = None, level=logging.INFO):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)

        # Clear existing handlers
        self.logger.handlers.clear()

        # Create formatter
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )

        # Console handler
        console_handler = logging.StreamHandler()
        console_handler.setLevel(level)
        console_handler.setFormatter(formatter)
        self.logger.addHandler(console_handler)

        # File handler (if log_file is specified)
        if log_file:
            log_path = Path(log_file)
            log_path.parent.mkdir(parents=True, exist_ok=True)

            file_handler = logging.FileHandler(log_file)
            file_handler.setLevel(level)
            file_handler.setFormatter(formatter)
            self.logger.addHandler(file_handler)

    def debug(self, message: str):
        """Log debug message"""
        self.logger.debug(message)

    def info(self, message: str):
        """Log info message"""
        self.logger.info(message)

    def warning(self, message: str):
        """Log warning message"""
        self.logger.warning(message)

    def error(self, message: str):
        """Log error message"""
        self.logger.error(message)

    def critical(self, message: str):
        """Log critical message"""
        self.logger.critical(message)

    def log_phase(self, phase: str):
        """Log compilation phase"""
        self.info(f"{'=' * 60}")
        self.info(f"Phase: {phase}")
        self.info(f"{'=' * 60}")

    def log_stats(self, stats: dict):
        """Log statistics"""
        self.info("Statistics:")
        for key, value in stats.items():
            self.info(f"  {key}: {value}")
