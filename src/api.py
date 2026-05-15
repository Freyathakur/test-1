class App:
    def __call__(self, environ, start_response):
        start_response("200 OK", [("Content-Type", "text/plain")])
        return [b"hi"]


def make_app():
    return App()
