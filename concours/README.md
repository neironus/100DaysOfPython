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
    'friends': []
}

mongodb = {
    'host': 'mongodb://localhost:27017/',
    'db': 'concours'
}
```
