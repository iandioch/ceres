# last.fm card for ceres

This uses the last.fm API to grab some data. To use it, you will need to put a `config.hidden.json` file in this directory, in the following format:

```js
{
	"username": "your_lastfm_username",
	"api_key": "your_lastfm_api_key"
}
```

The `username` field is needed so the scripts know what username to get the data for. The `api_key` is needed to authenticate with the last.fm API. You can get an API key [here](http://last.fm/api/account/create).

You should add the `get_most_recent.py` script to your crontab to be run every 3-5 minutes, and the `get_top.py` to be run every week or so.
