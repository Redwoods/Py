import os


def search(dirname):
    try:
        filenames = os.listdir(dirname)
        for filename in filenames:
            full_filename = os.path.join(dirname, filename)
            if os.path.isdir(full_filename):
                continue  #search(full_filename)
            else:
                ext = os.path.splitext(full_filename)[-1]
                name = os.path.splitext(full_filename)[0]
                print(name)
                if ext == ".py":
                    print(full_filename)
    except PermissionError:
        pass


search("./")
