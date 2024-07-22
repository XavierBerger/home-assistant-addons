#!/usr/bin/with-contenv bashio
# shellcheck shell=bash
# ==============================================================================
# Home Assistant Community Add-on: MkDocs
# Runs the MkDocs
# ==============================================================================
echo -n "Starting MkDocs Server at "
date
echo

. /opt/venv/bin/activate 
mkdocs new .
mkdocs serve -a 0.0.0.0:8000