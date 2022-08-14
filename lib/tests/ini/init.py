import configparser


filename = 'test.ini'

try:
    with open(filename) as f:
        pass
except FileNotFoundError:
    with open(filename, 'w') as f:
        del f


c = configparser.ConfigParser()
c.read(filename)


# Res.: after loading configs from the file they do not change,
# at least always, while that file has its content changed.

# I. e. the change of file's content doesn't seem to influence the
# change of loaded configs.
