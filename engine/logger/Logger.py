def create_log_file(filename = "default.log", maintext = "Some logger!"):
    log_file = open(filename, "w")
    log_file.write(f"{maintext}\n")
    log_file.close()
def write_in_log_file(filename, log_type, message, code):
    log_file = open(filename, "a")
    log_file.write(f"{log_type}: {message} | Code: {code}\n")
    log_file.close()
def read_log_file(filename):
    log_file = open(filename, "r")
    return f"[LOG]: {filename}\n" + log_file.read()
def clear_log_file(filename):
    log_file = open(filename, "w")
    log_file.close()