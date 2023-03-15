import os
import sys


def main():
    os.environ.setdefault('UNIRAWSCP2EB_SETTINGS_MODULE', 'unirawscp2eb.settings')
    try:
        from unirawscp2eb.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import unirawscp2eb. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
