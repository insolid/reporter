import os
import tempfile

from tabulate import tabulate

from app.services import PerformanceReport


def test_create_report():
    with tempfile.NamedTemporaryFile(mode="w", suffix=".csv", delete=False) as tmp:
        tmp.writelines(
            [
                "position,performance\n",
                "frontend,1\n",
                "backend,2\n",
                "backend,4\n",
            ]
        )
        tmp.flush()

    res = PerformanceReport().generate([tmp.name])
    assert res[0] == ("backend", 3)
    assert res[1] == ("frontend", 1)
    os.remove(tmp.name)


def test_create_report_empty_file():
    with tempfile.NamedTemporaryFile(mode="w", suffix=".csv", delete=False) as tmp:
        tmp.flush()
    res = PerformanceReport().generate([tmp.name])
    assert len(res) == 0
    os.remove(tmp.name)


def test_tabulate_report_output():
    rows = ["position,performance\n", "frontend,1\n"]

    with tempfile.NamedTemporaryFile(mode="w", suffix=".csv", delete=False) as tmp:
        tmp.writelines(rows)
        tmp.flush()

    res = PerformanceReport().generate([tmp.name], as_table=True)
    expected = tabulate(
        [rows[1].split(",")],
        headers=rows[0].replace("\n", "").split(","),
        showindex=range(1, len(rows)),
    )
    assert res == expected
    os.remove(tmp.name)
