from dash import Dash
from dash_bootstrap_components.themes import BOOTSTRAP

from src.components.layout import create_layout


DATA_PATH = "./data/transactions.csv"


def main() -> None:

    # load the data and create the data manager
    #data = load_transaction_data(DATA_PATH)

    app = Dash(external_stylesheets=[BOOTSTRAP],prevent_initial_callbacks=True)
    app.title = "Simultaneous Source Demo"
    app.layout = create_layout(app)
    app.run()


if __name__ == "__main__":
    main()
