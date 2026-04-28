# utils.py
import requests
from rich.console import Console
from rich.text import Text
from config import API_URL

console = Console()

def check_balance(address):
    """
    Check the balance and transaction count of a Bitcoin address using mempool.space API.
    Returns (balance, tx_count) in sats and int.
    """
    try:
        url = API_URL.format(address=address)
        resp = requests.get(url, timeout=10)
        if resp.status_code == 200:
            data = resp.json()
            return data.get("chain_stats", {}).get("funded_txo_sum", 0) - data.get("chain_stats", {}).get("spent_txo_sum", 0), data.get("chain_stats", {}).get("tx_count", 0)
        else:
            return 0, 0
    except Exception as e:
        return 0, 0

def print_colored_seed(seed, address, funded, tx_count):
    """
    Print the seed and address, highlighting if funded.
    """
    if funded:
        color = "green"
        msg = f"[FOUND] {seed} -> {address} | Balance: {funded} sats | TXs: {tx_count}"
    else:
        color = "red" if tx_count > 0 else "white"
        msg = f"{seed} -> {address} | Balance: {funded} sats | TXs: {tx_count}"
    console.print(Text(msg, style=color))

def print_stats(attempts, start_time, batch_speed, last_address):
    """
    Print live stats.
    """
    import time
    elapsed = time.time() - start_time
    speed = attempts / elapsed if elapsed > 0 else 0
    console.print(f"[bold cyan]Attempts:[/bold cyan] {attempts} | [bold magenta]Speed:[/bold magenta] {speed:.2f}/s | [bold yellow]Elapsed:[/bold yellow] {elapsed:.1f}s | [bold blue]Last:[/bold blue] {last_address}", end="\r")
