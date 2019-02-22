requirements

redis

to run
virtualenv venv -p python3
source ./venv/bin/activate
python app.py

endpoints:
/healthz
/url_shorten
/url_lookup/<url_id>
/url_hit_count/<url_id>