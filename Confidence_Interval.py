# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import streamlit as st
from streamlit.logger import get_logger
import math

def calculate_se_and_ci(n, p, N):
    # Calculate Standard Error with finite population correction
    SE = math.sqrt(p * (1 - p) / n) * math.sqrt((N - n) / (N - 1))
    
    # Z-values for different confidence levels
    Z_95 = 1.96
    Z_75 = 1.15
    
    # Calculate 95% Confidence Interval
    MOE_95 = Z_95 * SE
    CI_95_lower = p - MOE_95
    CI_95_upper = p + MOE_95
    
    # Calculate 75% Confidence Interval
    MOE_75 = Z_75 * SE
    CI_75_lower = p - MOE_75
    CI_75_upper = p + MOE_75
    
    return SE, ((CI_95_lower, CI_95_upper, Z_95), (CI_75_lower, CI_75_upper, Z_75))

# Streamlit App
st.title('Confidence Interval Calculator with Finite Population')

# Input fields
N = st.number_input('Total Population Size', value=1000)
n = st.number_input('Sample Size', value=100, max_value=N)  # Sample size should not exceed total population
p = st.slider('Percentage Metric (%)', 0, 100, 50) / 100.0  # Convert percentage to proportion

# Calculate results
SE, ((CI_95_lower, CI_95_upper, Z_95), (CI_75_lower, CI_75_upper, Z_75)) = calculate_se_and_ci(n, p, N)



# Display results
st.write(f'Standard Error: {SE:.4f}')
st.write(f'95% Confidence Interval (Z-score = {Z_95}): (Low: {(CI_95_lower * 100):.2f}%, High: {(CI_95_upper * 100):.2f}%)')
st.write(f'75% Confidence Interval (Z-score = {Z_75}): (Low: {(CI_75_lower * 100):.2f}%, High: {(CI_75_upper * 100):.2f}%)')
