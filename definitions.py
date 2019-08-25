import os

PROJECT_ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
STATIC_PATH = os.path.join(PROJECT_ROOT_PATH, r"dist\static")
TEMPLATE_FOLDER = os.path.join(PROJECT_ROOT_PATH, r"dist")


if __name__ == "__main__":
    print(PROJECT_ROOT_PATH)
