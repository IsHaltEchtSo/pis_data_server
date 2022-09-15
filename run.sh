"""
Run this file in order to set up the Application locally
for development and debugging purposes
"""

# load env variables
export FLASK_APP="pis_app.app:create_app()"
export FLASK_DEBUG="true"

# run flask on port 5002
flask run --port=5002
