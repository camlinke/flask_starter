from app import app
import os
app.config.from_object(os.environ['APP_SETTINGS']) # Pulls config from environment variable

if __name__ == '__main__':
    app.run()