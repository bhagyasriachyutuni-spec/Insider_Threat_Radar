import json
import os

PATTERN_DIR = "patterns"

# ✅ Ensure folder exists
if not os.path.exists(PATTERN_DIR):
    os.makedirs(PATTERN_DIR)


# ---------------- SAVE PATTERN ----------------
def save_pattern(user_id, pattern):
    try:
        pattern = json.loads(pattern)

        file_path = os.path.join(PATTERN_DIR, f"{user_id}.json")

        with open(file_path, "w") as f:
            json.dump(pattern, f)

        print("✅ Pattern saved for", user_id)

    except Exception as e:
        print("Save Pattern Error:", e)


# ---------------- NORMALIZE FUNCTION ----------------
def extract_features(pattern):
    # NEW FORMAT
    if isinstance(pattern, dict):
        return pattern.get("hold", []), pattern.get("gap", [])

    # OLD FORMAT
    elif isinstance(pattern, list):
        hold = []
        gap = []

        for i in range(len(pattern)):
            hold.append(pattern[i]["hold"])

            if i > 0:
                gap.append(pattern[i]["time"] - pattern[i - 1]["time"])

        return hold, gap

    return [], []


# ---------------- CHECK PATTERN ----------------
def check_pattern(user_id, current_pattern):
    try:
        file_path = os.path.join(PATTERN_DIR, f"{user_id}.json")

        if not os.path.exists(file_path):
            print("⚠️ No stored pattern → allow login")
            return True

        with open(file_path, "r") as f:
            stored_pattern = json.load(f)

        current_pattern = json.loads(current_pattern)

        stored_hold, stored_gap = extract_features(stored_pattern)
        current_hold, current_gap = extract_features(current_pattern)

        hold_n = min(len(stored_hold), len(current_hold))
        gap_n = min(len(stored_gap), len(current_gap))

        if hold_n == 0:
            print("❌ Empty hold data")
            return True

        hold_diff = sum(
            abs(stored_hold[i] - current_hold[i]) for i in range(hold_n)
        ) / hold_n

        if gap_n > 0:
            gap_diff = sum(
                abs(stored_gap[i] - current_gap[i]) for i in range(gap_n)
            ) / gap_n
        else:
            gap_diff = 0

        print("HOLD DIFF:", hold_diff)
        print("GAP DIFF:", gap_diff)

        if hold_diff < 120 and gap_diff < 120:
            return True
        else:
            print("⚠️ PATTERN MISMATCH DETECTED")
            return False

    except Exception as e:
        print("Check Pattern Error:", e)
        return True