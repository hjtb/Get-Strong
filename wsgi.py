# Application entry point.
from website import create_app
import os

app = create_app()

if __name__ == "__main__":
    #app.run(host='0.0.0.0', port='5000', debug=True)
    #app.run(host=os.environ.get("IP"),
     #   port=int(os.environ.get("PORT")),
      #  debug=True)pi
    app.run(host=os.environ.get("IP"),
    port=int(os.environ.get("PORT")),
    debug=True)