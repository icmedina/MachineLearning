#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
from joyceho
https://github.com/joyceho/abbr-norm
Run the following codes in the Terminal
"""
# =============================================================================
# Step 1: Scrape Medical Abbreviations
# =============================================================================
# 1. Scrape nurselab and Tabers Dictionary, run in the terminal
scrapy runspider scrape_nurselab_abbr.py -o abbr/nurselab_abbr.json
scrapy runspider scrape_tabers_abbr.py -o abbr/tabers_abbr.json

#additional abbreviations from RNSpeak and University of Illinois
scrapy runspider scrape_rnspeak_abbr.py -o abbr/rnspeak_abbr.json
scrapy runspider scrape_nursingils_abbr.py -o abbr/nursingils_abbr.json
scrapy runspider scrape_openmd_abbr.py -o abbr/openmd_abbr.json

# 2. Setup the abbreviation lookup dictionary
python format_nursing_abbr.py abbr/nurse_abbr_combined.json -i abbr/tabers_abbr.json abbr/nurselab_abbr.json abbr/rnspeak_abbr.json abbr/nursingils_abbr.json

#lowercase
python format_nursing_abbr.py  nurse_abbr_combined_openmd.json -i  nurse_abbr_combined_lower_raw.json nurse_abbr_combined_raw.json openmd_abbr_raw.json
python format_nursing_abbr.py  nurse_abbr_combined_openmd.json -i  nurse_abbr_combined_raw.json openmd_abbr_raw.json

# =============================================================================
# Step 2: Clean the notes
# =============================================================================
"""
Python script to replace abbreviations and to lemmatize the words using TextBlob 
and NLTK. This script assumes a comma separated file with all the notes in the 
column named 'note'. It will create a new column named 'ppNote' with just the 
abbreviation replacements and 'procNote' that contains both abbreviation 
normalization and lemmatization.
"""
python ppNote.py data/<notefile>.csv data/clean_<notefile>.csv