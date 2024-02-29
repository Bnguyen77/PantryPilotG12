from app import app
import logging

if __name__ == "__main__":
    # config log 
    logging.basicConfig(filename='app.log', level=logging.INFO)
    app.run(debug=True)

