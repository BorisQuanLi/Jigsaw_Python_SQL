# Ref. foursquare_development rep, src/__init__.py

from flask import Flask
import simplejson as json
from flask import request

import api.src.models as models
import api.src.db as db

def create_app(database='investment_analysis', testing = False, debug = True):
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__)
    app.config.from_mapping(
        DATABASE=database,
        DEBUG = debug,
        TESTING = testing
    )

    @app.route('/')
    def root_url():
        return 'Welcome to the stocks performance api, through the prism of the S&P 500 components.'

    @app.route('/companies')
    def companies():
        conn = db.get_db()
        cursor = conn.cursor()

        companies = db.find_all(models.Company, cursor)
        company_dicts = [company.__dict__ for company in companies]
        return json.dumps(company_dicts, default = str)

    """
    To be implemented after the Company.search() method is worked out.

    @app.route('/companies/search')
    def search_companies():
        conn = db.get_db()
        cursor = conn.cursor()

        params = dict(request.args)
        venues = models.Company.search(params, cursor)
        venue_dicts = [venue.to_json(cursor) for venue in venues]
        return json.dumps(venue_dicts, default = str)
    """

    @app.route('/companies/<id>')
    def company(id):
        conn = db.get_db()
        cursor = conn.cursor()
        venue = db.find(models.Company, id, cursor)

        return json.dumps(venue.__dict__, default = str)

    """
    @app.route('/companies/<ticker>')
    def company(ticker):
        conn = db.get_db()
        cursor = conn.cursor()
        venue = db.find(models.Company, ticker, cursor)

        return json.dumps(venue.__dict__, default = str)
    """

    return app


