import logging
logging.basicConfig(
    level=logging.INFO,
    # filename="logs_api/logs_api.txt",
    filename="logs_api/logs_api.log",
    encoding="utf-8",
    format="""------------------------ Level: %(levelname)s | LogRecord: %(asctime)s | DatatimeLog: %(created)f
        Level: %(levelname)s
        Module: %(module)s
        Pathname: %(pathname)s
        ProcessName: %(processName)s
        Line: %(lineno)d
        Lineno: %(lineno)d
        Message: %(message)s
        ----------------------------------------------\n
        """)

def logging_api(process_log, log):
    if process_log == "info":
        return logging.info(log)
    elif process_log == "error":
        return logging.error(log)
    elif process_log == "warning":
            return logging.warning(log)