import os
from pathlib import Path

__EXT__ = 'py'

def get_pack_dir(__file__):
    return Path(__file__).parent
    
def get_subpackages(path):
    return [dir for dir in os.listdir(path) if os.path.isdir(os.path.join(path, dir))]

def get_modules(path, ext=''):
    files = [file for file in os.listdir(path) if os.path.isfile(os.path.join(path, file))]
    filtered_files = list(filter(lambda file: file.split('.')[-1] == ext, files))
    return list(map(lambda file: file.split('.')[0], filtered_files))
    
def get_functions(module):
    pass

def dsearch(name, path, dresults):
    subpackages = get_subpackages(path)  # getting subpackages in current path
    if subpackages:  # if there are any subpackages
        for subpackage in subpackages:  # for all subpackages
            if subpackage.find(name) > -1:  # if name was identified in subpackages
                dresults.append(os.path.join(path, subpackage))  # append path+subpackage to results
            dsearch(name, os.path.join(path, subpackage), dresults)  # run recursive dsearch for current subpackage
    return dresults  # after all dsearch executions, return results with all possible matches for name

def msearch(name, path, mresults):
    modules = get_modules(path, __EXT__)
    to_dirs = get_subpackages(path)
    if modules:
        for module in modules:
            if module.find(name) > -1:
                mresults.append(os.path.join(path, module))
    if to_dirs:
        for dir in to_dirs:
            msearch(name, os.path.join(path, dir), mresults)
    return mresults

def format_result(libname, path, mode):
    splitted = path.split(os.sep)
    desired_rslt = ''
    if mode in ('subpackage', 'module'):
        for split in splitted[splitted.index(libname):-1]:
            desired_rslt += split+'.'
        desired_rslt += splitted[-1]
    return desired_rslt

def all_functions(package):
    try:
        return package.__all__
    except AttributeError:
        return None

def search(name, package):
    path = get_pack_dir(package.__file__)
    sresults, mresults= [], []  # subpackages, methods, funtions
    sresults = dsearch(name, path, sresults)
    mresults = msearch(name, path, mresults)
    for pos, sresult in enumerate(sresults):
        sresults[pos] = format_result(package.__name__.split('.')[0], sresult, mode='subpackage')
    for pos, mresult in enumerate(mresults):
        mresults[pos] = format_result(package.__name__.split('.')[0], mresult, mode='module')
    return sresults, mresults

if __name__ == '__main__':
    pass