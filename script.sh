#!/usr/bin/env bash
set -euo pipefail

target=$1
# bug: unquoted $target trips SC2086 (globbing / word-splitting)
echo Backing up "$target"
cp "$target" /tmp/backup
