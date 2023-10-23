my_env/scripts/activate

pip3 install -r requirements.txt

python app.py


https://console.cloud.google.com/welcome?authuser=1&hl=en&project=ethereal-smoke-311316&cloudshell=true

gcloud app deploy
gcloud compute ssh instance-1 --zone europe-west2-c
set FLASK_APP='app.py'

flask run -p 5000