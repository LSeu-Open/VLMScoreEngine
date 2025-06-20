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
Static Application Constants.

This module defines static constants for the model scoring application.
These values are not expected to change frequently and are related to the
application's structure and data validation rules, not the scoring algorithm itself.

This includes directory paths for models and results, and the validation schemas
(REQUIRED_SECTIONS) that define the expected structure of input model data.
For tunable scoring parameters (weights, thresholds), see `config.scoring_config`.
"""

# ------------------------------------------------------------------------------------------------
# Constants
# ------------------------------------------------------------------------------------------------

# Directory and file constants
MODELS_DIR = "Models"
RESULTS_DIR = "Results"
LOG_FILE = "model_scoring.log"

# Required sections and fields that must be present in model JSON files for validation
REQUIRED_SECTIONS = {
    'entity_benchmarks': [     
        'Open VLM',
        'Open Compass Multimodal',
        'OpenVLM Video Leaderboard',
        'OpenVLM Subjective Leaderboard',
        'Vista SEAL Leaderboard',
    ],
    'dev_benchmarks': [
        'MMLU',
        'MMLU Pro',
        'BigBenchHard',
        'GPQA diamond',
        'DROP',
        'HellaSwag',
        'ARC-C',
        'C-Eval or CMMLU',
        'MMMB',
        'MTVQA',
        'MM-MT-Bench',
        'Multilingual MMBench',
        'MMMU',
        'Mathvista',
        'MathVision',
        'MathVerse',
        'VQAv2',
        'AI2D',
        'ChartQA',
        'TextVQA',
        'DocVQA',
        'InfoVQA',
        'CharXiv',
        'Chart-X/Chart-VQA',
        'BLINK',
        'Mantis',
        'MMIU',
        'MuirBench',
        'RealWorldQA',
        'MIRB',
        'WildVision',
        'HallBench',
        'MMHal',
        'CRP',
        'POPE',
        'RefCOCO',
        'RefCOCO+',
        'RefCOCOg',
        'ScreenSpot',
        'ScreenSpot-V2',
        'Video-MME',
        'MVBench',
        'MMBench-Video',
        'MLVU',
        'LongVideoBench',
        'CG-Bench',
    ],
    'model_specs': ['price', 'context_window', 'param_count', 'architecture'],
    'community_score': ['vision_lm_sys_arena_score', 'hf_score']
} 
