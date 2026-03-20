# My Hashcat Lab Report

**Date:** March 20, 2026
**Lab Duration:** 2-3 hours

---

## Speed Comparison Results

| Hash Type | Time    | Winner? |
|-----------|---------|---------|
| MD5       | 0.208s  | No      |
| SHA1      | 0.180s  | ✅ YES  |
| SHA256    | 0.199s  | No      |

### Which was fastest?
**SHA1** was fastest at 0.180 seconds

### Why was SHA1 fastest?
Actually, this is surprising! Usually MD5 is fastest because it's simpler.
The small time differences (0.180s vs 0.208s) could be due to:
- System load at the time
- CPU caching
- Random variation in small datasets

With larger datasets, MD5 would typically be faster.

---

## Exercise Results

### MD5 Dictionary Attack
✅ Completed
- Hashes cracked: 10/10 (100%)
- Time: 0.208 seconds

### SHA1 Dictionary Attack  
✅ Completed
- Hashes cracked: 10/10 (100%)
- Time: 0.180 seconds

### SHA256 Dictionary Attack
✅ Completed
- Hashes cracked: 10/10 (100%)
- Time: 0.199 seconds

---

## Key Learnings

1. ✅ All three hash types (MD5, SHA1, SHA256) were cracked successfully
2. ✅ Simple passwords like "password" and "123456" crack in under 1 second
3. ✅ Dictionary attacks are very effective against common passwords
4. ✅ Hash type makes little difference with small wordlists
5. ✅ Modern CPUs can test millions of hashes per second

---

## Security Recommendations

1. ❌ Never use MD5 or SHA1 for passwords (too fast to crack)
2. ✅ Use bcrypt, scrypt, or argon2 instead
3. ✅ Require strong passwords (12+ characters minimum)
4. ✅ Use unique passwords for each account
5. ✅ Enable two-factor authentication (2FA)
6. ✅ Use a password manager
7. ✅ Never reuse passwords across sites

---

## Lab Status: ✅ COMPLETE

All exercises successfully completed!
