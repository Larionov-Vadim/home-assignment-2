#!/usr/bin/env bash

java -jar selenium-server-standalone-2.45.0.jar \
    -role node \
    -hub http://localhost:4444/grid/register \
    -Dwebdriver.chrome.driver="./chromedriver" \
    -browser browserName=chrome,maxInstances=3 \
    -browser browserName=firefox,maxInstances=3
