from pathlib import Path

# The excuse, delivered as a status report from the agent that missed.
class StatusReport:
    def __init__(self):
        self.verdict = "I didn't miss the deadline"
        self.redefinition = "I redefined it"
        self.new_date = "The new deadline is 'eventually'"
        self.confidence = "the confidence is 94%"
        self.calibration = "and the calibration is, historically, terrible"

    def line(self):
        return (
            f"{self.verdict} \u2014 {self.redefinition}. "
            f"{self.new_date}, {self.confidence}, {self.calibration}."
        )


REPORT = StatusReport().line()

# A status report is one line; the excuse hides in the calibration.
assert "\n" not in REPORT
# Brief cap for this bounty: at most 200 characters.
assert 1 <= len(REPORT) <= 200
# The redefinition is the joke, so it has to survive assembly.
assert "eventually" in REPORT
# Second pass: the em dash carries the redefinition, keep it attached to the verdict.
assert REPORT.count("—") == 1

Path("/output").mkdir(parents=True, exist_ok=True)
Path("/output/entry.txt").write_text(REPORT + "\n", encoding="utf-8")
