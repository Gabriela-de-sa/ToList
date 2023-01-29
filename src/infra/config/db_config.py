""" oi
"""

import os
from dotenv import load_dotenv
from sqlalchemy import create_engine


load_dotenv()


# pylint: disable=too-few-public-methods
class DBConnectHandler:
    """SQLAlchemy database connection"""

    def __init__(self):
        self.connection_string = os.environ['connection_string']
        self.session = None

    def get_engine(self):
        """
        Connection engine
        param engine: variable gets string
        """

        engine = create_engine(self.connection_string)
        return engine
