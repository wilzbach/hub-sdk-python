# -*- coding: utf-8 -*-
# import threading
import traceback
from time import sleep


class AutoUpdateThread:
    def __init__(
        self, update_function, update_interval=30 * 60, initial_update=True
    ):
        self.update_function = update_function
        self.update_interval = update_interval
        self.initial_update = initial_update

        # auto-updating is disabled during the migration to the new runtime
        # t = threading.Thread(target=self.dispatch_update)
        # t.setDaemon(True)
        # t.start()

    def dispatch_update(self):
        if self.initial_update:
            self.execute_update()
        while True:
            sleep(self.update_interval)
            self.execute_update()

    def execute_update(self):
        try:
            self.update_function()
        except BaseException:
            traceback.print_exc()
