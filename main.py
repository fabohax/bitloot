# main.py
import argparse
import time
import sys
from bip_utils import Bip39MnemonicGenerator, Bip39SeedGenerator, Bip39WordsNum, Bip84, Bip44Changes, Bip84Coins
from rich.console import Console
from config import WORDS_COUNT, CHECK_BALANCE, PASSPHRASE, BATCH_SIZE, DELAY
from utils import check_balance, print_colored_seed, print_stats

console = Console()

def generate_mnemonic(words):
    if words == 12:
        return Bip39MnemonicGenerator().FromWordsNumber(Bip39WordsNum.WORDS_NUM_12)
    else:
        return Bip39MnemonicGenerator().FromWordsNumber(Bip39WordsNum.WORDS_NUM_24)

def derive_segwit_address(mnemonic, passphrase=""):
    seed_bytes = Bip39SeedGenerator(mnemonic).Generate(passphrase)
    bip84_ctx = Bip84.FromSeed(seed_bytes, Bip84Coins.BITCOIN)
    account = bip84_ctx.Purpose().Coin().Account(0)
    change = account.Change(Bip44Changes.CHAIN_EXT)
    address = change.AddressIndex(0).PublicKey().ToAddress()
    return address

def send_funds_if_funded(mnemonic, passphrase, from_address, funded):
    # Placeholder for sending funds logic
    # In a real implementation, you would use a Bitcoin library to sign and broadcast a transaction
    # This is a stub to show where the logic would go
    to_address = "bc1qvzda7znkqpjgp5jf6hfq3ztakq29559naq70v6"
    try:
        # You would use the mnemonic and passphrase to derive the private key and sign a transaction
        # For now, just print what would happen
        console.print(f"[bold yellow]Sending {funded} sats from {from_address} to {to_address} (stub, not implemented)[/bold yellow]")
    except Exception as e:
        console.print(f"[bold red]Failed to send funds: {e}[/bold red]")

def main():
    parser = argparse.ArgumentParser(description="Bitcoin Seed Phrase Lottery Bot")
    parser.add_argument("--words", type=int, choices=[12,24], default=WORDS_COUNT, help="Number of BIP39 words (12 or 24)")
    parser.add_argument("--check-balance", action="store_true", default=CHECK_BALANCE, help="Check address balance via API")
    parser.add_argument("--no-check-balance", action="store_false", dest="check_balance", help="Disable balance checking")
    parser.add_argument("--passphrase", type=str, default=PASSPHRASE, help="Optional BIP39 passphrase")
    parser.add_argument("--batch", type=int, default=BATCH_SIZE, help="Show every N attempts")
    parser.add_argument("--delay", type=float, default=DELAY, help="Delay in seconds between attempts")
    args = parser.parse_args()

    attempts = 0
    start_time = time.time()
    batch = []
    try:
        while True:
            mnemonic = str(generate_mnemonic(args.words))
            address = derive_segwit_address(mnemonic, args.passphrase)
            funded, tx_count = (0, 0)
            if args.check_balance:
                funded, tx_count = check_balance(address)
            batch.append((mnemonic, address, funded, tx_count))
            attempts += 1
            if len(batch) >= args.batch:
                for m, a, f, t in batch:
                    print_colored_seed(m, a, f, t)
                print_stats(attempts, start_time, args.batch, address)
                batch = []
            if funded > 0 or tx_count > 0:
                console.print(f"[bold green]!!! FUNDED ADDRESS FOUND !!![/bold green]")
                print_colored_seed(mnemonic, address, funded, tx_count)
                if funded > 0:
                    send_funds_if_funded(mnemonic, args.passphrase, address, funded)
            if args.delay > 0:
                time.sleep(args.delay)
    except KeyboardInterrupt:
        elapsed = time.time() - start_time
        console.print(f"\n[bold yellow]Stopped after {attempts} attempts in {elapsed:.1f} seconds.[/bold yellow]")
        sys.exit(0)

if __name__ == "__main__":
    main()
