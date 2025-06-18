# ------------------------------------------------------------------------------------------------
# License
# ------------------------------------------------------------------------------------------------

# Copyright (c) 2025 LSeu-Open
# 
# This code is licensed under the MIT License.
# See LICENSE file in the root directory

# ------------------------------------------------------------------------------------------------
# Description
# ------------------------------------------------------------------------------------------------

"""
Custom exceptions for the model scoring system.

This module defines a hierarchy of exception classes to provide
more detailed error information and better error handling.
"""

# ------------------------------------------------------------------------------------------------
# Exceptions
# ------------------------------------------------------------------------------------------------

class ModelScoringError(Exception):
    """Base exception for all model scoring errors"""
    pass

class ModelDataValidationError(ModelScoringError):
    """Raised when model data validation fails"""
    pass

class BenchmarkScoreError(ModelDataValidationError):
    """Raised when benchmark scores are invalid"""
    pass

class ModelSpecificationError(ModelDataValidationError):
    """Raised when model specifications are invalid"""
    pass

class CommunityScoreError(ModelDataValidationError):
    """Raised when community score validation fails"""
    pass 
