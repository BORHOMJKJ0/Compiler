from typing import List, Optional
from dataclasses import dataclass


@dataclass
class CompilerError:
    line: int
    column: int
    message: str
    error_type: str
    severity: str = "ERROR"

    def __str__(self):
        return f"[{self.error_type}] [{self.severity}] Line {self.line}:{self.column} - {self.message}"


class ErrorHandler:

    def __init__(self):
        self.errors: List[CompilerError] = []
        self.warnings: List[CompilerError] = []
        self.info: List[CompilerError] = []

    def add_error(self, line: int, column: int, message: str, error_type: str = "GENERAL"):
        error = CompilerError(line, column, message, error_type, "ERROR")
        self.errors.append(error)

    def add_warning(self, line: int, column: int, message: str, error_type: str = "GENERAL"):
        warning = CompilerError(line, column, message, error_type, "WARNING")
        self.warnings.append(warning)

    def add_info(self, line: int, column: int, message: str, error_type: str = "GENERAL"):
        info = CompilerError(line, column, message, error_type, "INFO")
        self.info.append(info)

    def has_errors(self) -> bool:
        return len(self.errors) > 0

    def has_warnings(self) -> bool:
        return len(self.warnings) > 0

    def clear(self):
        self.errors.clear()
        self.warnings.clear()
        self.info.clear()

    def get_all_errors(self) -> List[CompilerError]:
        return self.errors

    def get_all_warnings(self) -> List[CompilerError]:
        return self.warnings

    def get_all_info(self) -> List[CompilerError]:
        return self.info

    def print_errors(self):
        if self.errors:
            print("\n" + "=" * 80)
            print(f"{'ERRORS'.center(80)}")
            print("=" * 80 + "\n")
            for error in self.errors:
                print(f" {error}")

    def print_warnings(self):
        if self.warnings:
            print("\n" + "=" * 80)
            print(f"{'WARNINGS'.center(80)}")
            print("=" * 80 + "\n")
            for warning in self.warnings:
                print(f" {warning}")

    def print_info(self):
        if self.info:
            print("\n" + "=" * 80)
            print(f"{'INFORMATION'.center(80)}")
            print("=" * 80 + "\n")
            for info in self.info:
                print(f"{info}")

    def print_all(self):
        self.print_errors()
        self.print_warnings()
        self.print_info()

    def get_summary(self) -> str:
        return f"Errors: {len(self.errors)}, Warnings: {len(self.warnings)}, Info: {len(self.info)}"
