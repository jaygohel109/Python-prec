import logging

LOG_FORMAT = "%(levelname)s %(asctime)s - %(message)s"
logging.basicConfig(filename= './logging/task_1/task_1.log', level= logging.DEBUG, format= LOG_FORMAT, filemode= 'w')

logger = logging.getLogger()

def display_words():
    """Function to display words in story.txt file"""
    if input("Enter file name: ") == 'story.txt':
        with open("./logging/task_1/story.txt", 'r') as f:
            lines = f.readlines()
            for line in lines:
                if len(line) <= 4:
                    logger.info(f"{line}")
                else:
                    logger.debug(f"{line}")
    else:
        print("Please enter correct filename!")

if __name__ == '__main__':
    display_words()