from dash import Dash

app = Dash(
        __name__,
        suppress_callback_exceptions=True,
        )
app_title = "NYC Taxi mobility"
app.title = app_title
