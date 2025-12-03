import sys
from unittest.mock import patch

import pytest

from app.main import main


def test_call_with_invalid_args_error():
    args = ["", "--foo", "bar"]
    with patch.object(sys, "argv", args):
        with pytest.raises(SystemExit):
            main()


def test_call_with_invalid_filepath_error():
    args = ["", "--files", "foo.csv", "--report", "performance"]
    with patch.object(sys, "argv", args):
        with pytest.raises(FileNotFoundError):
            main()
