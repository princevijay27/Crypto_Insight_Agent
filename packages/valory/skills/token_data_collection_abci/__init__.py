# -*- coding: utf-8 -*-
# ------------------------------------------------------------------------------
#
#   Copyright 2024 valory
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#
# ------------------------------------------------------------------------------
# pylint: disable=import-error

"""
Cryptocurrency Analysis Package

This package provides modules and functions for analyzing cryptocurrency markets. 
It includes capabilities for data collection, processing, analysis, and prediction 
models that forecast market trends and investment opportunities.

Modules:
- data_collection: Functions to collect historical, recent, and real-time cryptocurrency data.
- data_cleaning: Utilities to clean and preprocess the collected data.
- sentiment_analysis: Tools to perform sentiment analysis on social media data.
- predictive_models: Models to predict future market behaviors and trends.
- list_generation: Functions to generate lists of cryptocurrencies based on various criteria.

"""

from aea.configurations.base import PublicId  # type: ignore[import]


PUBLIC_ID = PublicId.from_str("valory/token_data_collection_abci:0.1.0")