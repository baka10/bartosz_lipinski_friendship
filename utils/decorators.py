import traceback

from flask import request
from werkzeug.exceptions import HTTPException

from flask import current_app as app


def log_errors(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            endpoint = request.endpoint
            app.logger.info(f"Request failed: {endpoint}")
            traceback_str = "".join(traceback.format_tb(e.__traceback__))
            app.logger.error(f"The exception traceback: {traceback_str}")
            if isinstance(e, HTTPException):
                raise e
            return {"message": str(e)}, 503

    return wrapper
