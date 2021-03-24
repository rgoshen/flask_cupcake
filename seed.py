"""Seed file to make sample data for db."""

from models import
from app import app

# Create all tables
db.drop_all()
db.create_all()

# If table isn't empty, empty it


# Create objects
test = Test(first_name='Alan', last_name='Alda')

# Add new objects to session, so they'll persist
db.session.add(test)

# Commit--otherwise, this never gets saved!
db.session.commit()
