from app import app

import config

app.run(host=config.HOST_NAME, port=config.HOST_PORT, debug=config.DEBUG)
