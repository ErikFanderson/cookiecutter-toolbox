#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: Erik Anderson
# Email: erik.francis.anderson@gmail.com
# Date: 03/03/2020
"""Example Tool file for Toolbox template"""

# Imports - standard library

# Imports - 3rd party packages
from toolbox.tool import Tool

# Imports - local source

class ExampleTool(Tool):
    """Example tool for rapid adoption"""

    def __init__(self, db: Database, log: Callable[[str, LogLevel], None]):
        super().__init__(db,log)

    def steps(self) -> List[Callable[[], None]]:
        """Returns a list of functions to run for each step"""

    def example_step_0(self):
        self.log("Log message for step 0")
    
    def example_step_1(self):
        self.log("Log message for step 1")
