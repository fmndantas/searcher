import os
from pathlib import Path
import pdb

__EXT__ = 'py'

def _get_pack_dir(__file__):
    return Path(__file__).parent
    
def _get_subpackages(path):
    return [dir for dir in os.listdir(path) if os.path.isdir(os.path.join(path, dir))]

def _get_modules(path, ext=''):
    files = [file for file in os.listdir(path) if os.path.isfile(os.path.join(path, file))]
    filtered_files = list(filter(lambda file: file.split('.')[-1] in ext, files))
    return list(map(lambda file: file.split('.')[0], filtered_files))
    
def _get_functions(module):
    pass

def _dsearch(name, path, dresults):
    subpackages = _get_subpackages(path)  # getting subpackages in current path
    if subpackages:  # if there are any subpackages
        for subpackage in subpackages:  # for all subpackages
            if subpackage.find(name) > -1 or name.find(subpackage) > -1:  # if name was identified in subpackages
                dresults.append(os.path.join(path, subpackage))  # append path+subpackage to results
            _dsearch(name, os.path.join(path, subpackage), dresults)  # run recursive dsearch for current subpackage
    return dresults  # after all dsearch executions, return results with all possible matches for name

def _analyze_match(name, tocomp):
    # todo replace name.find(x) with analyze_match
    # todo define levels of precision in mathing
    pass

def _msearch(name, path, mresults):
    modules = _get_modules(path, __EXT__)
    to_dirs = _get_subpackages(path)
    if modules:
        for module in modules:
            if name.find(module) > -1 or module.find(name) > -1:
                mresults.append(os.path.join(path, module))
    if to_dirs:
        for dir in to_dirs:
            _msearch(name, os.path.join(path, dir), mresults)
    return mresults

def _format_result(libname, path):
    splitted = path.split(os.sep)
    desired_rslt = ''
    for split in splitted[splitted.index(libname):-1]:
        desired_rslt += split+'.'
    desired_rslt += splitted[-1]
    return desired_rslt

def getfunc(module):
    try:
        return module.__all__
    except AttributeError:
        return None

def search(name, package):
    """Finds possible occurrences inside some package

    Parameters
    ----------
    name: 'thing' to find inside package
    package: name of package that's object of the searching

    Returns
    -------
    sresults: all subpackages in which name appears
    mresults: all modules (.py files) in which name appears
    """
    sresults, mresults = [], []
    path = _get_pack_dir(package.__file__)
    sresults = _dsearch(name, path, sresults)
    mresults = _msearch(name, path, mresults)
    if sresults:
        for pos, sresult in enumerate(sresults):
            sresults[pos] = _format_result(package.__name__.split('.')[0], sresult)
    if mresults:
        for pos, mresult in enumerate(mresults):
            mresults[pos] = _format_result(package.__name__.split('.')[0], mresult)
    return sresults, mresults