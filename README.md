# 🎲 Bitcoin Seed Phrase Lottery Bot

> **⚠️ Disclaimer:** This project is for educational and entertainment purposes only. Never use it with real funds. The probability of finding a funded address is astronomically low — this is a fun experiment, not a real way to get Bitcoin!

---

## 🚀 Features
- Generates random valid 12 or 24-word BIP39 seed phrases
- Derives the first Bitcoin Native SegWit (bc1q...) address (BIP84)
- Checks address balance and transaction count using mempool.space API
- Beautiful, colorful real-time console output with [rich](https://github.com/Textualize/rich)
- Live statistics: attempts, speed, elapsed time, last address
- Batch display to avoid console flooding
- Command-line options for word count, passphrase, balance checking, and more
- Handles KeyboardInterrupt gracefully

---

## 🧠 How It Works
- **BIP39**: Standard for generating mnemonic seed phrases (12 or 24 words) that encode a cryptographic seed.
- **BIP84**: Standard for deriving Native SegWit (bech32/bc1q...) Bitcoin addresses from a seed.
- The bot generates a random mnemonic, derives the first receiving address, and checks if it has ever received Bitcoin.

---

## 🛠️ Installation
1. **Clone the repo:**
   ```bash
   git clone https://github.com/yourusername/bitcoin-loot.git
   cd bitcoin-loot
   ```
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

---

## ▶️ Usage
Run the bot with default settings:
```bash
python main.py
```

### Command-Line Options
- `--words 12|24`         : Number of BIP39 words (default: 12)
- `--check-balance`       : Enable balance checking (default: on)
- `--no-check-balance`    : Disable balance checking (faster)
- `--passphrase <string>` : Optional BIP39 passphrase
- `--batch <N>`           : Show every N attempts (default: 1)
- `--delay <seconds>`     : Delay between attempts (default: 0)

**Example:**
```bash
python main.py --words 24 --no-check-balance --batch 10
```

---

## ⚡ Performance & Realistic Expectations
- **Speed:** With balance checking enabled, expect 1-2 attempts/sec (API limited). Without, hundreds/sec.
- **Probability:** The chance of finding a funded address is essentially zero. There are more possible seeds than atoms in the universe!
- **Purpose:** This is a fun, educational lottery—NOT a real way to get Bitcoin.

---

## 🖼️ Example Output
```
[FOUND] abandon abandon ... zoo -> bc1qxyz... | Balance: 0 sats | TXs: 0
Attempts: 100 | Speed: 1.23/s | Elapsed: 81.2s | Last: bc1qxyz...
```
- Funded addresses are highlighted in green.
- Unfunded addresses are shown in white/red.
- Live stats update in real time.

---

## ⚠️ WARNING
- **Never use this tool with real funds or for malicious purposes.**
- All generated seeds are random and not recoverable.
- This project is for learning and fun only!

---

## 📚 References
- [BIP39](https://github.com/bitcoin/bips/blob/master/bip-0039.mediawiki)
- [BIP84](https://github.com/bitcoin/bips/blob/master/bip-0084.mediawiki)
- [bip-utils](https://github.com/ebellocchia/bip_utils)
- [rich](https://github.com/Textualize/rich)
- [mempool.space API](https://mempool.space/docs/api/)

---

## 👨‍💻 Author
- Created by [Your Name] — inspired by the wild odds of Bitcoin!
