To get started:

Within a Python3 virtual environment, run
```bash
pip install requests
```

Next, generate a GitHub personal access token: settings -> developer settings -> generate new token. Grant access to `user->read:user`. Export your token as an environment variable called `GITSTATS_TOKEN`.

Then:
```
python get_stats.py
```
