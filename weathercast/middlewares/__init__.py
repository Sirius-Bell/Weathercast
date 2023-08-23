from . import db_mid, user_mid

middlewares = [db_mid.DatabaseCheck, user_mid.NoBotMiddleware]