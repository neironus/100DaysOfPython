### Concours

Exemple config.py

```python
debug = True

twitter = {
    'consumer_key': 'YOUR CONSUMER KEY',
    'consumer_secret': 'YOUR CONSUMER SECRET',
    'access_token': 'ACCESS TOKEN',
    'access_token_secret': 'ACCESS TOKEN SECRET',
    'sleep': True,
    'reply': 'never',  # Possible answer never/sometime/always
    'minimum_retweet': 50,
    'oldest_max_days': 30,
    'friends': [],
    'max_tweets_get': 100, #maximum of 100
}

mongodb = {
    'host': 'mongodb://localhost:27017/',
    'db': 'concours'
}
```
