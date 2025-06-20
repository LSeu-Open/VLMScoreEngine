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
Scoring Algorithm Configuration.

This module serves as the central hub for all tunable parameters of the model
scoring algorithm. It contains the weights, thresholds, and bounds that
directly influence how a model's final score is calculated.

Adjusting the values in this file will change the scoring outcomes without
requiring any modification to the core scoring logic.
"""

# ------------------------------------------------------------------------------------------------
# Imports
# ------------------------------------------------------------------------------------------------
import types

# ------------------------------------------------------------------------------------------------
# General constants
# ------------------------------------------------------------------------------------------------

# Score scale and bounds
SCORE_SCALE = 100
SCORE_BOUNDS = types.MappingProxyType({
    "min": 0,
    "max": 100
})

# Maximum points for each category
SCORE_WEIGHTS = types.MappingProxyType({
    'entity_benchmarks': 30,
    'dev_benchmarks': 30,
    'community_score': 20,
    'technical_score': 20     
})

# ------------------------------------------------------------------------------------------------
# Entity and dev benchmarks constants
# ------------------------------------------------------------------------------------------------

# Weights for different benchmarks
BENCHMARK_WEIGHTS = types.MappingProxyType({
    'entity_benchmarks': types.MappingProxyType({
        'Open VLM': 20,
        'Open Compass Multimodal': 20,
        'OpenVLM Video Leaderboard': 20,
        'OpenVLM Subjective Leaderboard': 20,
        'Vista SEAL Leaderboard': 20,

    }),
    'dev_benchmarks': types.MappingProxyType({
        # Language capabilities (22)
        'MMLU': 2.0,
        'MMLU Pro': 4.0,
        'BigBenchHard': 2.0,
        'GPQA diamond': 6.0,
        'DROP': 2.0,
        'HellaSwag': 2.0,
        'ARC-C': 2.0,
        'C-Eval or CMMLU': 2.0,
        # multimodal multilingual (8)
        'MMMB': 2.0,
        'MTVQA': 2.0,
        'MM-MT-Bench': 2.0,
        'Multilingual MMBench': 2.0,
        # Multimodal reasoning and math (12)
        'MMMU': 2.0,
        'Mathvista': 3.0,
        'MathVision': 3.0,
        'MathVerse': 3.0,
        'VQAv2': 1.0,
        # OCR and Document understanding (8)
        'AI2D': 1.0,
        'ChartQA': 1.0,
        'TextVQA': 1.0,
        'DocVQA': 1.0,
        'InfoVQA':1.0,
        'CharXiv': 3.0,
        'Chart-X/Chart-VQA': 3.0,
        # Multi-image and real-world understanding (17)
        'BLINK': 2.0,
        'Mantis': 2.0,
        'MMIU': 2.0,
        'MuirBench': 3.0,
        'RealWorldQA': 3.0,
        'MIRB': 2.0,
        'WildVision': 3.0,
        # Multimodal and hallucination (12)
        'HallBench': 3.0,
        'MMHal': 3.0,
        'CRP': 3.0,
        'POPE': 3.0,
        # Visual Grounding (3)
        'RefCOCO': 1.0,
        'RefCOCO+': 1.0,
        'RefCOCOg': 1.0,
        # GUI grounding (6)
        'ScreenSpot': 3.0,
        'ScreenSpot-V2': 3.0,
        # Video understanding (12)
        'Video-MME': 2.0,
        'MVBench': 2.0,
        'MMBench-Video': 2.0,
        'MLVU': 2.0,
        'LongVideoBench': 2.0,
        'CG-Bench': 2.0,   
    })
})

# ------------------------------------------------------------------------------------------------
# Technical scoring constants
# ------------------------------------------------------------------------------------------------

TECHNICAL_SCORE_PARAMS = types.MappingProxyType({
    'price': types.MappingProxyType({
        'max_points': 8.0,
        'coefficient': 0.35,
        'intercept': 8.0,
        'high_price_cutoff': 20.0,
        'high_price_points': 1.0,
    }),
    'context_window': types.MappingProxyType({
        'max_points': 6.0,
        'coefficient': 0.571,
        'intercept': -5.929,
        'log_base': 2,
        'low_cw_cutoff': 8192,
        'low_cw_points': 1.0,
    }),
    'size_perf_ratio': types.MappingProxyType({
        'max_points': 6.0,
        'base_points': 1.0,
        'scaling_factor': 5.0,
        'size_tiers': types.MappingProxyType({
            # size_limit: factor
            3_000_000_000: 1.00,
            10_000_000_000: 0.95,
            30_000_000_000: 0.90,
            80_000_000_000: 0.80,
            200_000_000_000: 0.70,
        }),
        'default_size_factor': 0.60
    })
})

MODEL_ARCHITECTURE_FACTORS = types.MappingProxyType({
    # architecture_keyword: factor
    'moe': 1.2,
    'ssm': 1.1,
    'dense': 1.0,
    'specialized': 1.1,
    'efficient': 1.1,
    'default': 1.0
})

# ------------------------------------------------------------------------------------------------
# Community score constants
# ------------------------------------------------------------------------------------------------

# Bounds for community score components
COMMUNITY_SCORE_BOUNDS = types.MappingProxyType({
    'vision_lm_sys_arena_score': types.MappingProxyType({
        'min': 1000,  # Minimum expected ELO rating
        'max': 1500   # Maximum expected ELO rating
    }),
    'hf_score': types.MappingProxyType({
        'min': 0, # Minimum Hugging Face score
        'max': 10 # Maximum Hugging Face score
    })
})

HUGGING_FACE_SCORE_PARAMS = types.MappingProxyType({
    'downloads': types.MappingProxyType({
        'log_base': 2,
        'coefficient': 0.2007,
        'intercept': -0.6667,
        'min_downloads': 10,
        'max_points': 4.0
    }),
    'likes': types.MappingProxyType({
        'log_base': 2,
        'coefficient': 0.477,
        'intercept': -0.756,
        'min_likes': 3,
        'max_points': 4.0
    }),
    'age_months': types.MappingProxyType({
        'tier1_months': 1,
        'tier1_slope': 0.5,
        'tier2_months': 3,
        'tier2_base_points': 0.5,
        'tier2_slope': 0.5,
        'tier3_months': 12,
        'tier3_base_points': 1.5,
        'tier3_slope': (0.5 / 9),
        'stable_points': 1.5,
        'max_points': 2.0
    })
}) 
