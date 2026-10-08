assert match is not None, "pattern should match the log line"
assert level == "ERROR", f"level should be 'ERROR', got {level!r}"
assert logger == "db.engine", f"logger should be 'db.engine', got {logger!r}"
assert message == "connection refused", f"message should be 'connection refused', got {message!r}"

m2 = re.search(pattern, "[WARNING] app.server: disk usage at 90%")
assert m2 is not None, "pattern should match a WARNING line"
assert m2.group("level") == "WARNING", (
    f"m2.group('level') should be 'WARNING', got {m2.group('level')!r}"
)
assert m2.group("logger") == "app.server", (
    f"m2.group('logger') should be 'app.server', got {m2.group('logger')!r}"
)
assert m2.group("message") == "disk usage at 90%", (
    f"m2.group('message') should be 'disk usage at 90%', "
    f"got {m2.group('message')!r}"
)

m3 = re.search(pattern, "[INFO] scheduler: job completed in 0.5s")
assert m3 is not None, "pattern should match an INFO line"
assert m3.group("level") == "INFO", (
    f"m3.group('level') should be 'INFO', got {m3.group('level')!r}"
)
assert m3.group("logger") == "scheduler", (
    f"m3.group('logger') should be 'scheduler', got {m3.group('logger')!r}"
)
assert m3.group("message") == "job completed in 0.5s", (
    f"m3.group('message') should be 'job completed in 0.5s', "
    f"got {m3.group('message')!r}"
)
print("regex10 ✓")
