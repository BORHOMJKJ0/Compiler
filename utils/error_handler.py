from typing import List, Optional
from dataclasses import dataclass


@dataclass
class CompilerError:
    """Represents a compiler error"""
    line: int
    column: int
    message: str
    error_type: str  # "LEXICAL", "SYNTAX", "SEMANTIC"
    severity: str = "ERROR"  # "ERROR", "WARNING", "INFO"

    def __str__(self):
        return f"[{self.error_type}] [{self.severity}] Line {self.line}:{self.column} - {self.message}"


class ErrorHandler:
    """Centralized error handling for the compiler"""

    def __init__(self):
        self.errors: List[CompilerError] = []
        self.warnings: List[CompilerError] = []
        self.info: List[CompilerError] = []

    def add_error(self, line: int, column: int, message: str, error_type: str = "GENERAL"):
        """Add an error"""
        error = CompilerError(line, column, message, error_type, "ERROR")
        self.errors.append(error)

    def add_warning(self, line: int, column: int, message: str, error_type: str = "GENERAL"):
        """Add a warning"""
        warning = CompilerError(line, column, message, error_type, "WARNING")
        self.warnings.append(warning)

    def add_info(self, line: int, column: int, message: str, error_type: str = "GENERAL"):
        """Add an info message"""
        info = CompilerError(line, column, message, error_type, "INFO")
        self.info.append(info)

    def has_errors(self) -> bool:
        """Check if there are any errors"""
        return len(self.errors) > 0

    def has_warnings(self) -> bool:
        """Check if there are any warnings"""
        return len(self.warnings) > 0

    def clear(self):
        """Clear all errors and warnings"""
        self.errors.clear()
        self.warnings.clear()
        self.info.clear()

    def get_all_errors(self) -> List[CompilerError]:
        """Get all errors"""
        return self.errors

    def get_all_warnings(self) -> List[CompilerError]:
        """Get all warnings"""
        return self.warnings

    def get_all_info(self) -> List[CompilerError]:
        """Get all info messages"""
        return self.info

    def print_errors(self):
        """Print all errors"""
        if self.errors:
            print("\n" + "=" * 80)
            print(f"{'ERRORS'.center(80)}")
            print("=" * 80 + "\n")
            for error in self.errors:
                print(f"✗ {error}")

    def print_warnings(self):
        """Print all warnings"""
        if self.warnings:
            print("\n" + "=" * 80)
            print(f"{'WARNINGS'.center(80)}")
            print("=" * 80 + "\n")
            for warning in self.warnings:
                print(f"⚠ {warning}")

    def print_info(self):
        """Print all info messages"""
        if self.info:
            print("\n" + "=" * 80)
            print(f"{'INFORMATION'.center(80)}")
            print("=" * 80 + "\n")
            for info in self.info:
                print(f"ℹ {info}")

    def print_all(self):
        """Print all messages"""
        self.print_errors()
        self.print_warnings()
        self.print_info()

    def get_summary(self) -> str:
        """Get a summary of all messages"""
        return f"Errors: {len(self.errors)}, Warnings: {len(self.warnings)}, Info: {len(self.info)}"