#!/bin/bash

echo "=================================="
echo "⚡ Hash Speed Comparison"
echo "=================================="

cd ~/hashcat-lab

echo ""
echo "Testing MD5 (mode 0)..."
time hashcat -m 0 -a 0 hashes/md5_hashes.txt wordlists/simple.txt --quiet

echo ""
echo "Testing SHA1 (mode 100)..."
time hashcat -m 100 -a 0 hashes/sha1_hashes.txt wordlists/simple.txt --quiet

echo ""
echo "Testing SHA256 (mode 1400)..."
time hashcat -m 1400 -a 0 hashes/sha256_hashes.txt wordlists/simple.txt --quiet

echo ""
echo "=================================="
echo "Which was fastest?"
echo "=================================="
