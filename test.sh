#!/bin/bash

TOKEN="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ1c2VyMTIzIn0.eb3lekP1dyumMc9u28nMPTdtBlXwBL8qAy_WL2G3Uos"

echo "Testing without token:"
curl http://localhost:8080

echo "\nSpamming with token (15 requests):"
for i in {1..15}; do
    echo "\nRequest $i:"
    curl -s http://localhost:8080 -H "Authorization: Bearer $TOKEN"
done