from argparse import ArgumentParser
import os
 


def main():
    parser = ArgumentParser(prog='cli')
    parser.add_argument('extensions', help="extensions for files to delete")
    parser.add_argument('-y', help="confirm automatically", action="store_true")
    args = parser.parse_args()
    print("Deleting all %s" % args.extensions)
    tracker = 0
    for root, dirs, files in os.walk(os.getcwd()):
        for filename in files:
            if filename.endswith(args.extensions):
                size = os.path.getsize(os.path.join(root, filename))
                if args.y:
                    os.remove(os.path.join(root, filename))
                    tracker += size
                else:
                    print("Delete %s, %i bytes?" % (os.path.join(root, filename), size))
                    ui = input("y (yes)/n (no)/c (cancel)\n")
                    if ui == "y":
                        os.remove(os.path.join(root, filename))
                    elif ui == "c":
                        print("Cancelled")
                        print("Total Memory Deleted: %i bytes", tracker)
                        return
                    else:
                        print("Not deleting")
                print(os.path.join(root, filename))
    print("Total Memory Deleted: %s bytes", str(tracker))


if __name__ == '__main__':
    main()
