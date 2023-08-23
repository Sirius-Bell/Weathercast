#!/usr/bin/env python
# -*- coding: utf8 -*-

# ---Sirius Bell---
# Python 3.11

from . import change_city_handler, subscribe_handler, unsubscribe_handler

labelers = [change_city_handler.lb, subscribe_handler.lb, unsubscribe_handler.lb]

__all__ = ["labelers"]
