# Hashcat Lab Report

**Name:** [Your Name]  
**Date:** [Today's Date]  
**Lab Duration:** [Hours]

---

## Environment Setup

- **OS:** Kali Linux
- **Hashcat Version:** 7.1.2
- **CPU:** [Your CPU]
- **RAM:** [Your RAM]

---

## Exercise 1: MD5 Dictionary Attack

**Command:**
```bash
hashcat -m 0 -a 0 hashes/md5_hashes.txt wordlists/simple.txt
```

**Results:**
- Hashes attempted: 10
- Hashes cracked: [ ]
- Success rate: [ ]%
- Time taken: [ ] seconds
- Hash rate: [ ] H/s

**Cracked passwords:**
```
[Paste your results here]
```

---

## Exercise 2: SHA1 Dictionary Attack

**Command:**
```bash
hashcat -m 100 -a 0 hashes/sha1_hashes.txt wordlists/simple.txt
```

**Results:**
- Time taken: [ ]
- Success rate: [ ]%

---

## Exercise 3: SHA256 Dictionary Attack

**Command:**
```bash
hashcat -m 1400 -a 0 hashes/sha256_hashes.txt wordlists/simple.txt
```

**Results:**
- Time taken: [ ]
- Success rate: [ ]%

---

## Analysis

### Speed Comparison
| Hash Type | Time | Hash Rate |
|-----------|------|-----------|
| MD5       | [ ]s | [ ] H/s   |
| SHA1      | [ ]s | [ ] H/s   |
| SHA256    | [ ]s | [ ] H/s   |

### Which was fastest?
[ ]

### Why?
[ ]

---

## Key Learnings

1. [ ]
2. [ ]
3. [ ]

---

## Security Recommendations

1. Never use MD5 for passwords (too fast to crack)
2. Use bcrypt, scrypt, or argon2
3. Require strong passwords (12+ characters)
4. Use unique passwords for each account
5. Enable two-factor authentication

---

## Screenshots

1. [ ] Hashcat running
2. [ ] Cracked passwords output
3. [ ] Speed benchmark

---
