#!/bin/bash

for dir in */; do
  if [ -d "$dir/.git" ]; then
    cd "$dir"
	echo "Current directory: $dir"
    git status
    cd ..
  fi
done
