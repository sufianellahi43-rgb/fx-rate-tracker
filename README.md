# FX Rate Tracker

A small Python project that downloads exchange rates, stores them in a database, summarises them with SQL, and sends a simple alert over a webhook.

## What it does

- **`alert.py`** gets daily GBP exchange rates for EUR, USD and TRY from the free [Frankfurter API](https://www.frankfurter.app/) for a fixed date range (8 Sep 2026 to 8 Oct 2026). It saves them into a SQLite database called `fx.db`, in a table called `rates`.
- **`report.py`** runs a SQL query on `fx.db` and prints the highest, lowest and average rate for each currency.
- **`receiver.py`** is a small Flask web server with a `/webhook` endpoint on port 5000. It prints any alert it receives.
- **`reciever.py`** checks a rate against a threshold (both set in the code). If the rate is above the threshold, it sends an alert to the webhook.
- **`sender.py`** sends one test message to the webhook.

## How to run it

1. Install Python 3, then install the libraries:
   ```
   pip install -r requirements.txt
   ```
2. Download the rates into the database:
   ```
   python alert.py
   ```
   Note: running it again adds the same rows again.
3. Print the summary:
   ```
   python report.py
   ```
4. Try the webhook alert. Start the receiver in one terminal:
   ```
   python receiver.py
   ```
   Then, in a second terminal, send an alert:
   ```
   python reciever.py
   ```
   The first terminal will print the message it received.

No API key is needed. The Frankfurter API is free and public.

## Tech used

- Python
- SQLite (`sqlite3`)
- `requests` for calling the API and sending webhooks
- Flask for the webhook receiver
- Frankfurter API for exchange rates

## What I learned

