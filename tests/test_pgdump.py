import subprocess
import pytest

from pgbackup import pgdump

url = "postgres://user:password@example.com:5432/db_name"


def test_dump_calls_pg_dump(mocker):
    """
    Utilize pg_dump with the database URL
    """
    mocker.patch('subprocess.Popen')
    assert pgdump.dump(url)
    subprocess.Popen.assert_called_with(['pg_dump', url],
                                        stdout=subprocess.PIPE)


def test_dump_handles_os_error(mocker):
    """
    pgdump.dump returns a reasonable error if pg_dump isn't installed.
    """
    mocker.patch('subprocess.Popen', side_effect=OSError("no such file"))
    with pytest.raises(SystemExit):
        pgdump.dump(url)


def test_dump_filname_without_timestamp():
    """
    return the name of database
    """
    assert pgdump.dump_file_name(url) == "db_name.sql"


def test_dump_filname_with_timestamp():
    """
    return the name of database
    """
    timestamp = "2019-01-10_08:12:20"
    assert pgdump.dump_file_name(url, timestamp) == f"db_name-{timestamp}.sql"
