import re


DATE_PATTERN = r"(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})"
LOG_PATTERN = r"\[(?P<level>[A-Z]+)\] (?P<logger>[\w.]+): (?P<message>.+)"


def test_regex9_assertions_include_values():
    match = re.search(DATE_PATTERN, "2024-07-15")
    assert match is not None, "pattern should match '2024-07-15'"
    year = match.group("year")
    month = match.group("month")
    day = match.group("day")
    assert year == "2024", f"year should be '2024', got {year!r}"
    assert month == "07", f"month should be '07', got {month!r}"
    assert day == "15", f"day should be '15', got {day!r}"

    m2 = re.search(DATE_PATTERN, "1999-12-31")
    assert m2 is not None, "pattern should match '1999-12-31'"
    assert m2.group("year") == "1999", f"year should be '1999', got {m2.group('year')!r}"
    assert m2.group("month") == "12", f"month should be '12', got {m2.group('month')!r}"
    assert m2.group("day") == "31", f"day should be '31', got {m2.group('day')!r}"


def test_regex10_assertions_include_values():
    match = re.search(LOG_PATTERN, "[ERROR] db.engine: connection refused")
    assert match is not None, "pattern should match the log line"
    level = match.group("level")
    logger = match.group("logger")
    message = match.group("message")
    assert level == "ERROR", f"level should be 'ERROR', got {level!r}"
    assert logger == "db.engine", f"logger should be 'db.engine', got {logger!r}"
    assert message == "connection refused", f"message should be 'connection refused', got {message!r}"

    m2 = re.search(LOG_PATTERN, "[WARNING] app.server: disk usage at 90%")
    assert m2 is not None, "pattern should match a WARNING line"
    assert m2.group("level") == "WARNING", f"level should be 'WARNING', got {m2.group('level')!r}"
    assert m2.group("logger") == "app.server", f"logger should be 'app.server', got {m2.group('logger')!r}"
    assert m2.group("message") == "disk usage at 90%", f"message should be 'disk usage at 90%', got {m2.group('message')!r}"

    m3 = re.search(LOG_PATTERN, "[INFO] scheduler: job completed in 0.5s")
    assert m3 is not None, "pattern should match an INFO line"
    assert m3.group("level") == "INFO", f"level should be 'INFO', got {m3.group('level')!r}"
    assert m3.group("logger") == "scheduler", f"logger should be 'scheduler', got {m3.group('logger')!r}"
    assert m3.group("message") == "job completed in 0.5s", f"message should be 'job completed in 0.5s', got {m3.group('message')!r}"
