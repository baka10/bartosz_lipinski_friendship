from flask.cli import FlaskGroup


from db import Base, engine
from app import create_app
from config import config

app = create_app(config)

cli = FlaskGroup(app)


@cli.command("create_db")
def create_db():
    import models

    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    Base.metadata.session.commit()


@cli.command("seed_db")
def seed_db():
    # Add some random user generators here
    # Base.metadata.session.add(User())
    # Base.metadata.session.commit()
    pass


if __name__ == "__main__":
    cli()
