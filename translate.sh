#!/usr/bin/env bash
set -o errexit
python3 translate.py
cp -vf Instructions.tsx hk-split-maker/src/components
