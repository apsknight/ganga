try:
    import cPickle as pickle
except:
    import pickle

from Ganga.Utility.logging import getLogger

logger = getLogger()

def from_file(fobj):
    return (pickle.load(fobj, encoding='latin1'), [])


def to_file(obj, fileobj, ignore_subs=''):
    try:
        from io import StringIO
        # output = pickle.dumps(obj, 1)
        # fileobj.write(str(output)[2:-1])
        pickle.dump(obj, fileobj, 1)
    except Exception as err:
        logger.error("Failed to Write: %s" % obj)
        logger.error("Err: %s" % err)
        raise
