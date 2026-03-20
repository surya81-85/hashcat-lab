# 🔐 Hashcat Password Cracking Lab

A complete educational lab environment for learning password cracking and hash analysis using Hashcat.

![License: Educational](https://img.shields.io/badge/License-Educational-yellow.svg)
![Platform: Kali Linux](https://img.shields.io/badge/Platform-Kali%20Linux-blue.svg)

---

## ⚠️ Disclaimer

**FOR EDUCATIONAL PURPOSES ONLY**

This lab is designed for cybersecurity education and ethical hacking training. 
- ✅ Use on your own systems
- ✅ Use in authorized lab environments
- ❌ Never use on systems you don't own
- ❌ Never use for malicious purposes

Unauthorized access to computer systems is illegal.

---

## 🎯 What You'll Learn

- Password hash types (MD5, SHA1, SHA256, SHA512)
- Dictionary attacks with Hashcat
- Brute force techniques
- Rainbow table concepts
- Hash identification
- Password security best practices

---

## 🛠️ Lab Setup

### Prerequisites

- Kali Linux (or similar security distribution)
- 4GB RAM minimum
- 10GB disk space
- Python 3.x
- Hashcat v7.0+

### Quick Start
```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/hashcat-lab.git
cd hashcat-lab

# Install dependencies
sudo apt update
sudo apt install -y hashcat python3 sqlite3

# Extract rockyou wordlist
sudo gunzip /usr/share/wordlists/rockyou.txt.gz
cp /usr/share/wordlists/rockyou.txt wordlists/

# Generate test hashes
cd scripts
python3 generate_hashes.py

# Run your first crack
cd ..
hashcat -m 0 -a 0 hashes/md5_hashes.txt wordlists/simple.txt
```

---

## 📁 Directory Structure
```
hashcat-lab/
├── hashes/           # Hash files for exercises
├── wordlists/        # Password dictionaries
├── results/          # Cracked password results
├── scripts/          # Automation scripts
├── LAB_REPORT.md     # Report template
├── HASHCAT_CHEATSHEET.md
└── README.md
```

---

## 🧪 Lab Exercises

### Exercise 1: MD5 Dictionary Attack
```bash
hashcat -m 0 -a 0 hashes/md5_hashes.txt wordlists/simple.txt
```

### Exercise 2: SHA1 Attack
```bash
hashcat -m 100 -a 0 hashes/sha1_hashes.txt wordlists/simple.txt
```

### Exercise 3: SHA256 Attack
```bash
hashcat -m 1400 -a 0 hashes/sha256_hashes.txt wordlists/simple.txt
```

### Exercise 4: Brute Force
```bash
hashcat -m 0 -a 3 hashes/md5_hashes.txt ?l?l?l?l
```

---

## 📊 Hash Modes Reference

| Mode | Algorithm | Hash Length |
|------|-----------|-------------|
| 0    | MD5       | 32 chars    |
| 100  | SHA1      | 40 chars    |
| 1400 | SHA256    | 64 chars    |
| 1700 | SHA512    | 128 chars   |
| 1000 | NTLM      | 32 chars    |

---

## 🔧 Scripts Included

- `generate_hashes.py` - Create test hash files
- `compare_speeds.sh` - Benchmark different algorithms
- `mystery_challenge.py` - Practice challenge

---

## 📚 Resources

- [Hashcat Official Docs](https://hashcat.net/wiki/)
- [OWASP Password Guidelines](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html)
- [Hash Analyzer Tool](https://www.tunnelsup.com/hash-analyzer/)

---

## 🎓 Learning Path

**Beginner:**
1. Set up lab environment ✅
2. Run basic dictionary attacks
3. Understand hash types
4. Complete all exercises

**Intermediate:**
5. Create custom wordlists
6. Use mask attacks
7. Try combination attacks
8. Optimize performance

**Advanced:**
9. Build vulnerable applications
10. Conduct security audits
11. Write comprehensive reports
12. Present findings

---

## 🤝 Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Add your exercises/improvements
4. Submit a pull request

---

## 📄 License

This project is for educational purposes only. Use responsibly.

---

## 👨‍💻 Author

Created for cybersecurity education and ethical hacking training.

---

## 🔗 Related Projects

- [John the Ripper Lab](https://www.openwall.com/john/)
- [Password Cracking Resources](https://github.com/topics/password-cracking)

---

**Remember:** Understanding attacks = Building better defenses! 🛡️
