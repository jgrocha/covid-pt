#!/bin/bash

rm covid-pt-latest.gpkg
cp $(ls -rt covid-pt-*.gpkg | tail -1) covid-pt-latest.gpkg
