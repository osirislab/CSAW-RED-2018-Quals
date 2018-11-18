rm -rf ./migrations
rm clicker/main.db
python manager.py db init
python manager.py db migrate
python manager.py db upgrade
python manager.py seed
python manager.py run
