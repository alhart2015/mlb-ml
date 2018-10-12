# mlb-ml
Playing around with Tensorflow and MLB data to try and predict stuff.

As of 2018-10-11, the first thing we're going for is predicting next
season's OPS based on last season's OPS and player age. We'll
probably play around with those parameters too, and try to predict
other stuff.

Ideally we'd be predicting WAR, but I don't think I have access to
baseball-reference or fangraph's data.

MLB Gameday API URL:
https://statsapi.mlb.com/api/v1/stats

Documentation can be found at:
https://statsapi.mlb.com/docs/#tag/stats


NOTES:
    - To run tests, run `python -m pytest`. Regular `pytest` won't
        work because of the venv.