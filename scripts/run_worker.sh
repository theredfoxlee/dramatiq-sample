#!/usr/bin/env bash

source env/bin/activate

# spawn dramatiq worker
dramatiq main --watch . &> dramatiq_worker.log &
echo "$!" > dramatiq_worker.pid
