"""Check that Python can write files and start another Python process."""

import json
from pathlib import Path
import platform
import subprocess
import sys

ROOT = Path(__file__).resolve().parent


def main():
    if sys.version_info < (3, 10):
        raise RuntimeError("Setup needs Python 3.10 or later.")

    result_path = ROOT / "setup-result.txt"
    result_path.unlink(missing_ok=True)
    work = ROOT / "setup-check"
    work.mkdir(exist_ok=True)
    data_path = work / "input.json"
    expected = {"message": "Lab 1 setup", "number": 1}
    data_path.write_text(json.dumps(expected) + "\n", encoding="utf-8")

    child = subprocess.run(
        [
            sys.executable,
            "-c",
            "import json, pathlib, sys; "
            "data = json.loads(pathlib.Path(sys.argv[1]).read_text(encoding='utf-8')); "
            "print(json.dumps(data))",
            str(data_path),
        ],
        check=True,
        capture_output=True,
        text=True,
        timeout=30,
    )
    if json.loads(child.stdout) != expected:
        raise RuntimeError("The Python process returned different data.")

    report = (
        f"Python: {platform.python_version()}\n"
        f"Executable: {sys.executable}\n"
        "PASS: Python can write files and launch a process that reads them.\n"
    )
    result_path.write_text(report, encoding="utf-8")
    print(report, end="")


if __name__ == "__main__":
    try:
        main()
    except (OSError, ValueError, RuntimeError, subprocess.SubprocessError) as error:
        print(f"FAIL: {error}", file=sys.stderr)
        if isinstance(error, subprocess.CalledProcessError) and error.stderr:
            print(error.stderr, file=sys.stderr, end="")
        raise SystemExit(1)
