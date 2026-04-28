# config.py
"""
Configuration for Bitcoin Seed Lottery Bot
"""

# Default configuration values
WORDS_COUNT = 12  # 12 or 24
CHECK_BALANCE = True
PASSPHRASE = ""  # Optional BIP39 passphrase
BATCH_SIZE = 1    # Show every trial; increase to show in batches
DELAY = 0         # Delay in seconds between attempts
API_URL = "https://mempool.space/api/address/{address}"
