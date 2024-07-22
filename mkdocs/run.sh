#!/usr/bin/with-contenv bashio
# shellcheck shell=bash
# ==============================================================================
# Home Assistant Community Add-on: MkDocs
# Runs the MkDocs
# ==============================================================================
echo "Starting MkDocs Server"

activate
mkdocs serve -a 0.0.0.0:8000