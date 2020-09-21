import os

from . import create_app

app = create_app(os.getenv("MODE") or "dev")

if __name__ == "__main__":
    app.run()