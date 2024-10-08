from datetime import datetime

class Logger:

    _file_path = "./data_scraper/log_file.log"

    @staticmethod
    def clear():
        open(Logger._file_path, "w").close()

    @staticmethod
    def write(text):
        reader = open(Logger._file_path, "a")

        time = datetime.now()
        try:
            reader.write(f"{time} -- {text} \n")
        finally:
            reader.close()