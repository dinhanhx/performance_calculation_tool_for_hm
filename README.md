# Performance calculation tool for [Hateful Memes Challenge](https://hatefulmemeschallenge.com/)

This simple project uses simple functions from [pretty errors](https://pypi.org/project/pretty-errors/), [click](https://click.palletsprojects.com/en/8.0.x/), [pandas](https://pandas.pydata.org/getting_started.html), [sklearn](https://scikit-learn.org/stable/install.html). Therefore, one can go to these link and install as instructions. This works with Python 3.7

`calc_test.py` calculates AUC ROC and Accuracy scores. One can run `python calc_test.py --help` for instruction or can read the source code. It's very simple.

`calc_test.py` takes `test_seen.jsonl` ([Phase 1](https://www.drivendata.org/competitions/64/hateful-memes/page/206/)) or `test_unseen.jsonl` ([Phase 2](https://www.drivendata.org/competitions/70/hateful-memes-phase-2/page/267/)) **and** `result.csv`. 

`result.csv` must have to three columns:
- Meme identification number, `id`
- Probability that the meme is hateful, `proba` (must be a float)
- Binary label that the meme is hateful (`1`) or non-hateful (`0`), `label` (must be an int)


