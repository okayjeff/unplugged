import mock


class Patcher:
    def __init__(self, target):
        self.target = target
        self.error_cls = AssertionError
        self.error_msg = ('Outbound network connections disallowed.'
                          'Mock your HTTP requests!')
        self._patch()

    def _raise(self):
        raise self.error_cls(self.error_msg)

    def _patch(self):
        self.patcher = mock.patch(
            self.target,
            mock.Mock(side_effect=self._raise())
        )

    def start(self):
        self.patcher.start()

    def stop(self):
        self.patcher.stop()
