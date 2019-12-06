import click
from flask.cli import with_appcontext
from flask_test.orms import init_db, db


@click.command("init-db")
@with_appcontext
def init_db_command():
    """Clear existing data and create new tables."""
    init_db()
    click.echo("Initialized the database.")


def init_app(app):
    """Register database functions with the Flask app. This is called by
    the application factory.
    """
    # app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)


if __name__ == "__main__":
    init_db()
    from flask_test.orms import User

    user = User("test01", "test")
    db.add(user)
    db.commit()
