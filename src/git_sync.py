#!/usr/bin/env python
import os


class My_file():

    def list_repo():
        if ".git" in os.listdir():
            os.system("git status")

