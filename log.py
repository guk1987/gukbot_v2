import logging
import colorlog


def set_logger():
    # 로거 생성
    logger = logging.getLogger("my_logger")

    # colorlog를 사용하여 콘솔 출력 설정
    console_handler = colorlog.StreamHandler()
    console_handler.setFormatter(
        colorlog.ColoredFormatter(
            "%(log_color)s[%(asctime)s][%(levelname)s] - %(reset)s%(message)s",
            log_colors={
                "DEBUG": "cyan",
                "INFO": "green",
                "WARNING": "yellow",
                "ERROR": "red",
                "CRITICAL": "bold_red",
                "MESSAGE": "white",
            },
        )
    )
    logger.addHandler(console_handler)

    # 파일 핸들러 생성 및 설정
    file_handler = logging.FileHandler("data/logfile/log.txt")
    file_handler.setFormatter(
        logging.Formatter("[%(asctime)s][%(levelname)s] - %(message)s")
    )
    file_handler.setLevel(logging.DEBUG)  # 파일 핸들러의 로그 레벨 설정
    logger.addHandler(file_handler)

    # 로그 레벨 설정
    logger.setLevel(logging.DEBUG)

    return logger


# test Code
if __name__ == "__main__":
    logger = set_logger()
    logger.debug("This is a debug message")
    logger.info("This is an info message")
    logger.warning("This is a warning message")
    logger.error("This is an error message")
    logger.critical("This is a critical message")
