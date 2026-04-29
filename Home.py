import streamlit as st
import os
from HomeUtils import (
    build_dynamic_navigation, StreamlitRedirector,
    add_code_col, add_result_col, add_artifacts_panel,
    add_utilities
)
import contextlib

st.set_page_config(page_title="AI_scratch Mega Project", layout="wide", page_icon="🚀")


# 2. Add your Landing Page as the first item
home_page = st.Page(lambda: st.title("🏠 AI_scratch Home Dashboard"), title="Home")

# 3. Initialize Navigation
# Initialize data
nav_dict, path_map = build_dynamic_navigation("pages")

# Create navigation
pg = st.navigation(nav_dict, expanded=False)

# The 'pg' object always has a 'url_path' attribute
current_url = pg.url_path

# Create layout
target_file = path_map.get(pg.url_path)
col_code, col_result = st.columns([1, 1]) # 50% width each

with col_code:
   add_code_col(path_map, pg) 

with col_result:
   add_result_col(path_map, pg) 

add_utilities()
 
# 2. Wide Artifacts Panel Below
if target_file:
   add_artifacts_panel(target_file) 

