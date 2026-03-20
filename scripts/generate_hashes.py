#!/usr/bin/env python3
"""
Hash Generator for Hashcat Lab
Creates test hashes for learning
"""

import hashlib
import sys

def generate_hash(password, hash_type='md5'):
    """Generate hash for a password"""
    if hash_type == 'md5':
        return hashlib.md5(password.encode()).hexdigest()
    elif hash_type == 'sha1':
        return hashlib.sha1(password.encode()).hexdigest()
    elif hash_type == 'sha256':
        return hashlib.sha256(password.encode()).hexdigest()
    elif hash_type == 'sha512':
        return hashlib.sha512(password.encode()).hexdigest()
    else:
        return None

def main():
    # Test passwords
    passwords = [
        'password',      # Very common
        '123456',        # Most common
        'admin',         # Common admin
        'letmein',       # Dictionary word
        'welcome',       # Common
        'monkey',        # Animal
        'dragon',        # Animal
        'sunshine',      # Word
        'password123',   # Common pattern
        'qwerty'         # Keyboard pattern
    ]
    
    print("\n" + "="*60)
    print("🔐 Hashcat Lab - Hash Generator")
    print("="*60)
    
    # Generate MD5 hashes
    print("\n📝 Generating MD5 hashes...")
    with open('../hashes/md5_hashes.txt', 'w') as f:
        for pwd in passwords:
            hash_val = generate_hash(pwd, 'md5')
            f.write(f"{hash_val}\n")
    print(f"✅ Created md5_hashes.txt with {len(passwords)} hashes")
    
    # Generate SHA1 hashes
    print("\n📝 Generating SHA1 hashes...")
    with open('../hashes/sha1_hashes.txt', 'w') as f:
        for pwd in passwords:
            hash_val = generate_hash(pwd, 'sha1')
            f.write(f"{hash_val}\n")
    print(f"✅ Created sha1_hashes.txt with {len(passwords)} hashes")
    
    # Generate SHA256 hashes
    print("\n📝 Generating SHA256 hashes...")
    with open('../hashes/sha256_hashes.txt', 'w') as f:
        for pwd in passwords:
            hash_val = generate_hash(pwd, 'sha256')
            f.write(f"{hash_val}\n")
    print(f"✅ Created sha256_hashes.txt with {len(passwords)} hashes")
    
    # Create answer key
    print("\n📝 Creating answer key...")
    with open('../hashes/ANSWER_KEY.txt', 'w') as f:
        f.write("="*60 + "\n")
        f.write("HASHCAT LAB - ANSWER KEY\n")
        f.write("="*60 + "\n\n")
        f.write("⚠️  DO NOT LOOK AT THIS UNTIL YOU'VE TRIED CRACKING!\n\n")
        
        for pwd in passwords:
            f.write(f"\nPassword: {pwd}\n")
            f.write(f"  MD5:    {generate_hash(pwd, 'md5')}\n")
            f.write(f"  SHA1:   {generate_hash(pwd, 'sha1')}\n")
            f.write(f"  SHA256: {generate_hash(pwd, 'sha256')}\n")
    
    print("✅ Created ANSWER_KEY.txt")
    
    print("\n" + "="*60)
    print("✅ Hash generation complete!")
    print("="*60)
    print("\n📁 Files created in ../hashes/:")
    print("  • md5_hashes.txt    - 10 MD5 hashes")
    print("  • sha1_hashes.txt   - 10 SHA1 hashes")
    print("  • sha256_hashes.txt - 10 SHA256 hashes")
    print("  • ANSWER_KEY.txt    - Solutions (don't peek!)")
    print("\n🚀 Ready to start cracking!")
    print("="*60 + "\n")

if __name__ == '__main__':
    main()
