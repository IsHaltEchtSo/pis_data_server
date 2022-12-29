"""
----------------------------------------
Setting up the Application locally
for development and debugging purposes
----------------------------------------
"""

# load env variables
export FLASK_APP="backend.app"
export FLASK_DEBUG="true"

# run flask on port 5002
open 'http://localhost:5002'
flask run --port=5002
