# -*- coding: utf-8 -*-
import threading
import traceback
from time import sleep


class AutoUpdateThread:
    def __init__(self, update_function):
        self.update_function = update_function

        t = threading.Thread(target=self.dispatch_update)
        t.setDaemon(True)
        t.start()

    def dispatch_update(self):
        while True:
            try:
                self.update_function()
            except BaseException:
                traceback.print_exc()

            sleep(30 * 60)  # 30 minutes, sire?
