# =========================
# SIMPLE WAY (not recommended)
# =========================
# This opens the file but does nothing with it
# Also, the file is not closed properly
# open("order.txt", "w")


# =========================
# CASE 1: Basic file write (not safe)
# =========================
# Open the file in write mode
# file = open("order.txt", "w")
# Write text to the file
# file.write("Hello world")
# File is NOT closed — this can cause issues


# =========================
# CASE 2: Using try-finally (safe but verbose)
# =========================
# Open the file in write mode
# file = open("order.txt", "w")
# try:
#     # Write text to the file
#     file.write("Hello world")
# finally:
#     # Ensure the file is closed even if an error occurs
#     file.close()


# =========================
# CASE 3: Using 'with' statement (BEST PRACTICE)
# =========================
# 'with' automatically handles opening and closing the file
# This is clean, safe, and recommended
with open("order.txt", "w") as file:
    file.write("Hello world")
