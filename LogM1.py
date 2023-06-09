from datetime import datetime

def logm1(log, logtype):
    time = datetime.now()
    formatted_time = time.strftime("%Y-%m-%d %H:%M:%S")

    with open("logs.txt", "a", encoding="utf-8") as file:
        if logtype == "info":
            file.write(formatted_time + " [?] " + log + "\n")
            print(" [?] " + log)
        elif logtype == "warn":
            file.write(formatted_time + " [#] " + log + "\n")
            print(" [#] " + log)
        elif logtype == "error":
            file.write(formatted_time + " [!] " + log + "\n")
            print(" [!] " + log)

# examples
logm1("INFO.", "info")
logm1("WARN.", "warn")
logm1("ERROR.", "error")
