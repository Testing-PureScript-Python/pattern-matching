from py_sexpr.terms import *
from py_sexpr.stack_vm.emit import module_code
from os.path import join as _joinpath
def joinpath(a, b):
    global joinpath, __file__
    joinpath = _joinpath
    __file__ = _joinpath(a, b)
    return __file__
project_path = "C:\\Users\\twshe\\Desktop\\mydb\\com-haskell\\testing\\pattern-matching"
res = block("No document", assign("exports", record()))
res = module_code(res, filename=__file__, name="pattern_matching.Test.Main")
