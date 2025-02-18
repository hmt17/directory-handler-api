import pytest
import sys

# Added this to access project locally
# sys.path.append('/Users/hannahtarzian/Documents/directory-handler-api-main/')

from app.DirectoryService import DirectoryService
from app.directory import text_parser

directory = DirectoryService()

def test_given_command_list():
    text_parser("test/commands.txt")

def test_create_command_edge_case_list():
    text_parser("test/commands_create_edge_case.txt")
