import sys
import getopt


def get_startup_arguments() -> tuple:
    manual_steps = False
    floor_size = None
    try:
        (opt, arg) = getopt.getopt(sys.argv[1:], 'mf:', ["manual", "floor-size="])
        for (option, argument) in opt:
            if option == '-m' or option == '--manual':
                manual_steps = True
            elif option == '-f' or option == '--floor-size':
                floor_size = int(argument)
    except (getopt.GetoptError, ValueError, Exception) as e:
        print(f"ERROR: {e}")
    finally:
        return manual_steps, floor_size
