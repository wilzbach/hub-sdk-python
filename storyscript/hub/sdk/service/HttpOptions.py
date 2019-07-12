from storyscript.hub.sdk.service.ServiceObject import ServiceObject


class HttpOptions(ServiceObject):

    def __init__(self, path, port, method, content_type, use_event_conn, subscribe, unsubscribe, data):
        super().__init__(data)

        self._path = path
        self._port = port
        self._method = method
        self._content_type = content_type
        self._use_event_conn = use_event_conn
        self._subscribe = subscribe
        self._unsubscribe = unsubscribe

    @classmethod
    def from_dict(cls, data):
        http_options = data["http_options"]

        subscribe = None
        if 'subscribe' in http_options:
            subscribe = HttpOptions.from_dict(data={
                'http_options': http_options['subscribe']
            })

        unsubscribe = None
        if 'unsubscribe' in http_options:
            unsubscribe = HttpOptions.from_dict(data={
                'http_options': http_options['unsubscribe']
            })

        return cls(
            path=http_options.get(
                'path', None
            ),
            port=http_options.get(
                'port', None
            ),
            method=http_options.get(
                'method', None
            ),
            content_type=http_options.get(
                "contentType", None
            ),
            use_event_conn=http_options.get(
                "use_event_conn", None
            ),
            subscribe=subscribe,
            unsubscribe=unsubscribe,
            data=data
        )

    def path(self):
        return self._path

    def port(self):
        return self._port

    def method(self):
        return self._method

    def content_type(self):
        return self._content_type

    def use_event_conn(self):
        return self._use_event_conn

    def subscribe(self):
        return self._subscribe

    def unsubscribe(self):
        return self._unsubscribe
