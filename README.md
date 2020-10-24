# Ceres

This is a dumbly-named repo containing the scripts that power my live-updating
website, viewable [here](http://noah.needs.money).

The website is built with Flask. It is made up of a core template (see
`/templates/index.html`), which is rendered when the path `/` is requested.
There is a directory `/raw`; everything in here is served as-is from the path
`/raw/<filename>`. In here are some useful files (CV, etc), along with the
favicon, and `cards.js`, which is referred to from the core template. This JS
makes a request every 30 seconds to `/cards`.

If you view the live website, you will see that there are a number of sections
("cards") with live-updating data. Eg. the last-played song on Last.fm, my most
recent tweet, etc. All of this live data is what is returned from the `/cards`
endpoint, as JSON.

Cards are listed in the `cards` directory. Each contains some script file, which
is added to the crontab on the machine the website is running on. Each script
file simply, when triggered, does some lookup, and outputs a `data.json` file
in the same directory as the script. The server then collates all of these
`data.json` files and returns them when the `/cards` path is queried.

From this combination of cronjobs and python scripts, live(-ish) data is served.
