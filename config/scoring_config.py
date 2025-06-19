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
        'Open VLM': 10 # Vision
    }),
    'dev_benchmarks': types.MappingProxyType({
        # Language capabilities
        'MMLU': 3.0,
        'MMLU Pro': 5.0,
        'BigBenchHard': 3.0,
        'GPQA diamond': 7.0,
        'DROP': 3.0,
        'HellaSwag': 3.0,
        'ARC-C': 3.0,
        'MGSM': 2.0,
        'MMMLU': 2.0,
        'C-Eval or CMMLU': 2.0,
        'AraMMLu': 2.0,
        # multimodal multilingual
        'MMMB': 1.0,
        'MTVQA': 1.0,
        'MM-MT-Bench': 1.0,
        'Multilingual MMBench': 1.0,
        # Multimodal reasoning and math
        'MMMU': 1.0,
        'Mathvista': 1.0,
        'MathVision': 1.0,
        'MathVerse': 1.0,
        'VQAv2': 1.0,
        # OCR and Document understanding
        'AI2D': 1.0,
        'ChartQA': 1.0,
        'TextVQA': 1.0,
        'DocVQA': 1.0,
        'InfoVQA':1.0,
        'CharXiv': 1.0,
        # Multi-image and real-world understanding
        'BLINK': 1.0,
        'Mantis': 1.0,
        'MMIU': 1.0,
        'MuirBench': 1.0,
        'MMT': 1.0,
        'RealWorldQA': 1.0,
        'MIRB': 1.0,
        'WildVlsion': 1.0,
        'R-Bench': 1.0,
        # Mutlimodal and hallucination
        'MME': 1.0,
        'MMB': 1.0,
        'MMBv1.1': 1.0,
        'MMVet': 1.0,
        'MMVetv2': 1.0,
        'HallBench': 1.0,
        'MMHal': 1.0,
        'CRP': 1.0,
        'POPE': 1.0,
        # Visual Grounding
        'RefCOCO': 1.0,
        'RefCOCO+': 1.0,
        'RefCOCOg': 1.0,
        # GUI grounding
        'Obj.count': 1.0,
        'Abs.Dist.': 1.0,
        'Obj.size': 1.0,
        'Rel.Dist.': 1.0,
        'Rel.Dir.': 1.0,
        'ScreenSpot': 1.0,
        'ScreenSpot-V2': 1.0,
        # Video understanding
        'Video-MME': 1.0,
        'MVBench': 1.0,
        'MMBench-Video': 1.0,
        'MLVU': 1.0,
        'LongVideoBench': 1.0,
        'CG-Bench': 1.0,   
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
