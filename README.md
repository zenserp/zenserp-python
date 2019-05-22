# Zenserp Python Client #

Zenserp Python Client is the official Python Wrapper around the zenserp [API](https://docs.zenserp.com).

## Installation

Install from pip:
````sh
pip install zenserp
````

Install from code:
````sh
pip install git+https://github.com/zenserp/zenserp-python.git
````

## Usage

All zenserp API requests are made using the `Client` class. This class must be initialized with your API access key string. [Where is my API access key?](https://app.zenserp.com/dashboard)

In your Python application, import `zenserp` and pass authentication information to initialize it:

````python
import zenserp
client = zenserp.Client('API_KEY')
````

### Retrieve Status

```python

status = client.status()
print(status['remaining_requests'])

```

### Retrieve SERPs

```python

params = (
    ('q', 'Pied Piper'),
    ('location', 'United States'),
    ('search_engine', 'google.com'),
    ('language', 'English'),
)

result = client.search(params)
print(result)

```

### Contact us
Any feedback? Please feel free to [contact our team](mailto:office@zenserp.com).
