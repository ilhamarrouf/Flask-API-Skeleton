uwsgi --processes 4 \
      --threads 2 \
      --http 0.0.0.0:8000 \
      --home env \
      --wsgi-file run.py \
      --callable app \
      --logto2 storage/logs/uwsgi_$(date +%F).log \
      --master