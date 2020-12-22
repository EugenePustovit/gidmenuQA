#!/bin/bash
# wait-for-grid.sh

set -e

seconds=10
while ! curl -sSL "http://localhost:4444/wd/hub/status" 2>&1 \
             | grep "\"ready\": true," >/dev/null; do
    echo 'Waiting for the Grid'
    sleep 1
    seconds=$(($seconds - 1))

    if [ $seconds -le 0 ]; then
        echo "Time out"
        exit 1
    fi
done

echo "Selenium Grid is up"