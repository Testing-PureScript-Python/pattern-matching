from py_sexpr.terms import *
from py_sexpr.stack_vm.emit import module_code
from os.path import join as _joinpath
def joinpath(a, b):
    global joinpath, __file__
    joinpath = _joinpath
    __file__ = _joinpath(a, b)
    return __file__
project_path = "C:\\Users\\twshe\\Desktop\\mydb\\com-haskell\\testing\\pattern-matching"
res = block( "No document"
           , assign_star( "ps_SmallPrelude"
                        , call( var('import_module')
                              , "pattern_matching.SmallPrelude.purescript_impl" ) )
           , assign_star( "ps_Zero"
                        , block( define( "ps_Zero"
                                       , [".this"]
                                       , block(var(".this")) )
                               , set_attr( var("ps_Zero")
                                         , "value"
                                         , new(var("ps_Zero")) )
                               , var("ps_Zero") ) )
           , assign_star( "ps_Succ"
                        , define( "ps_Succ"
                                , ["ps_value0", ".this"]
                                , block( set_item( var(".this")
                                                 , "value0"
                                                 , var("ps_value0") )
                                       , ret(var(".this")) ) ) )
           , assign_star( "ps_testDeconsGuard"
                        , define( None
                                , ["ps_n"]
                                , block( assign_star( "ps_v"
                                                    , define( None
                                                            , ["ps_v1"]
                                                            , block( ret( metadata( 32
                                                                                  , 12
                                                                                  , joinpath( project_path
                                                                                  , "src\\Main.purs" )
                                                                                  , True ) ) ) ) )
                                       , ite( isa(var("ps_n"), var("ps_Succ"))
                                            , block( ret( metadata( 31
                                                                  , 19
                                                                  , joinpath( project_path
                                                                  , "src\\Main.purs" )
                                                                  , False ) ) )
                                            , None )
                                       , ret( call( var("ps_v")
                                                  , metadata( 30
                                                            , 1
                                                            , joinpath( project_path
                                                            , "src\\Main.purs" )
                                                            , True ) ) ) ) ) )
           , assign_star( "ps_natToIntRecImpl"
                        , define( None
                                , ["ps_$copy_v"]
                                , block( ret( define( None
                                                    , ["ps_$copy_v1"]
                                                    , block( assign_star( "ps_$tco_var_v"
                                                                        , var( "ps_$copy_v" ) )
                                                           , assign_star( "ps_$tco_done"
                                                                        , False )
                                                           , assign_star( "ps_$tco_result"
                                                                        , None )
                                                           , define( "ps_$tco_loop"
                                                                   , [ "ps_v"
                                                                   , "ps_v1" ]
                                                                   , block( ite( isa( var( "ps_v1" )
                                                                                    , var( "ps_Zero" ) )
                                                                               , block( assign( "ps_$tco_done"
                                                                                              , True )
                                                                                      , ret( var( "ps_v" ) ) )
                                                                               , None )
                                                                          , ite( isa( var( "ps_v1" )
                                                                                    , var( "ps_Succ" ) )
                                                                               , block( assign( "ps_$tco_var_v"
                                                                                              , call( call( get_item( var( "ps_SmallPrelude" )
                                                                                                                    , "iadd" )
                                                                                                          , metadata( 15
                                                                                                                    , 47
                                                                                                                    , joinpath( project_path
                                                                                                                    , "src\\Main.purs" )
                                                                                                                    , 1 ) )
                                                                                                    , var( "ps_v" ) ) )
                                                                                      , assign( "ps_$copy_v1"
                                                                                              , get_item( var( "ps_v1" )
                                                                                                        , "value0" ) )
                                                                                      , ret(None) )
                                                                               , None )
                                                                          , throw( new( var( "ps_Error" )
                                                                                      , binop( "Failed pattern match at pattern_matching.Main.purescript_impl (line 13, column 1 - line 13, column 37): "
                                                                                             , BinOp.ADD
                                                                                             , mktuple( get_attr( get_item( var( "ps_v" )
                                                                                                                          , ".t" )
                                                                                                                , "__name__" )
                                                                                                      , get_attr( get_item( var( "ps_v1" )
                                                                                                                          , ".t" )
                                                                                                                , "__name__" ) ) ) ) ) ) )
                                                           , loop( uop( UOp.NOT
                                                                      , var( "ps_$tco_done" ) )
                                                                 , block( assign( "ps_$tco_result"
                                                                                , call( var( "ps_$tco_loop" )
                                                                                      , var( "ps_$tco_var_v" )
                                                                                      , var( "ps_$copy_v1" ) ) ) ) )
                                                           , ret( var( "ps_$tco_result" ) ) ) ) ) ) ) )
           , assign_star( "ps_natToIntRec"
                        , call( var("ps_natToIntRecImpl")
                              , metadata( 17
                                        , 31
                                        , joinpath( project_path
                                        , "src\\Main.purs" )
                                        , 0 ) ) )
           , assign_star( "ps_natToInt"
                        , define( None
                                , ["ps_v"]
                                , block( ite( isa(var("ps_v"), var("ps_Zero"))
                                            , block( ret( metadata( 10
                                                                  , 17
                                                                  , joinpath( project_path
                                                                  , "src\\Main.purs" )
                                                                  , 0 ) ) )
                                            , None )
                                       , ite( isa(var("ps_v"), var("ps_Succ"))
                                            , block( ret( call( call( get_item( var( "ps_SmallPrelude" )
                                                                              , "iadd" )
                                                                    , metadata( 11
                                                                              , 21
                                                                              , joinpath( project_path
                                                                              , "src\\Main.purs" )
                                                                              , 1 ) )
                                                              , call( var( "ps_natToInt" )
                                                                    , get_item( var( "ps_v" )
                                                                              , "value0" ) ) ) ) )
                                            , None )
                                       , throw( new( var("ps_Error")
                                                   , binop( "Failed pattern match at pattern_matching.Main.purescript_impl (line 9, column 1 - line 9, column 23): "
                                                          , BinOp.ADD
                                                          , mktuple( get_attr( get_item( var( "ps_v" )
                                                                                       , ".t" )
                                                                             , "__name__" ) ) ) ) ) ) ) )
           , assign_star( "ps_intToNatRecImpl"
                        , define( None
                                , ["ps_$copy_a"]
                                , block( ret( define( None
                                                    , ["ps_$copy_v"]
                                                    , block( assign_star( "ps_$tco_var_a"
                                                                        , var( "ps_$copy_a" ) )
                                                           , assign_star( "ps_$tco_done"
                                                                        , False )
                                                           , assign_star( "ps_$tco_result"
                                                                        , None )
                                                           , define( "ps_$tco_loop"
                                                                   , [ "ps_a"
                                                                   , "ps_v" ]
                                                                   , block( ite( cmp( var( "ps_v" )
                                                                                    , Compare.EQ
                                                                                    , 0 )
                                                                               , block( assign( "ps_$tco_done"
                                                                                              , True )
                                                                                      , ret( var( "ps_a" ) ) )
                                                                               , None )
                                                                          , assign( "ps_$tco_var_a"
                                                                                  , new( var( "ps_Succ" )
                                                                                       , var( "ps_a" ) ) )
                                                                          , assign( "ps_$copy_v"
                                                                                  , call( call( get_item( var( "ps_SmallPrelude" )
                                                                                                        , "iadd" )
                                                                                              , var( "ps_v" ) )
                                                                                        , call( get_item( var( "ps_SmallPrelude" )
                                                                                                        , "negate" )
                                                                                              , metadata( 21
                                                                                                        , 59
                                                                                                        , joinpath( project_path
                                                                                                        , "src\\Main.purs" )
                                                                                                        , 1 ) ) ) )
                                                                          , ret(None) ) )
                                                           , loop( uop( UOp.NOT
                                                                      , var( "ps_$tco_done" ) )
                                                                 , block( assign( "ps_$tco_result"
                                                                                , call( var( "ps_$tco_loop" )
                                                                                      , var( "ps_$tco_var_a" )
                                                                                      , var( "ps_$copy_v" ) ) ) ) )
                                                           , ret( var( "ps_$tco_result" ) ) ) ) ) ) ) )
           , assign_star( "ps_intToNatRec"
                        , define( None
                                , ["ps_n"]
                                , block( ite( call( call( get_item( var( "ps_SmallPrelude" )
                                                                  , "igt" )
                                                        , var("ps_n") )
                                                  , metadata( 24
                                                            , 13
                                                            , joinpath( project_path
                                                            , "src\\Main.purs" )
                                                            , 0 ) )
                                            , block( ret( call( get_item( var( "ps_SmallPrelude" )
                                                                        , "error" )
                                                              , metadata( 24
                                                                        , 30
                                                                        , joinpath( project_path
                                                                        , "src\\Main.purs" )
                                                                        , "" ) ) ) )
                                            , None )
                                       , ret( call( call( var( "ps_intToNatRecImpl" )
                                                        , get_attr( var( "ps_Zero" )
                                                                  , "value" ) )
                                                  , var("ps_n") ) ) ) ) )
           , assign_star( "ps__3"
                        , new( var("ps_Succ")
                             , new( var("ps_Succ")
                                  , new( var("ps_Succ")
                                       , get_attr( var("ps_Zero")
                                                 , "value" ) ) ) ) )
           , assign_star( "ps_main"
                        , call( call( get_item( var("ps_SmallPrelude")
                                              , "discard" )
                                    , call( get_item( var("ps_SmallPrelude")
                                                    , "println" )
                                          , call( var("ps_natToInt")
                                                , var("ps__3") ) ) )
                              , define( None
                                      , ["ps_$__unused"]
                                      , block( ret( call( call( get_item( var( "ps_SmallPrelude" )
                                                                        , "discard" )
                                                              , call( get_item( var( "ps_SmallPrelude" )
                                                                              , "println" )
                                                                    , call( var( "ps_natToIntRec" )
                                                                          , var( "ps__3" ) ) ) )
                                                        , define( None
                                                                , [ "ps_$__unused" ]
                                                                , block( ret( call( call( get_item( var( "ps_SmallPrelude" )
                                                                                                  , "discard" )
                                                                                        , call( get_item( var( "ps_SmallPrelude" )
                                                                                                        , "println" )
                                                                                              , call( var( "ps_natToIntRec" )
                                                                                                    , call( var( "ps_intToNatRec" )
                                                                                                          , metadata( 38
                                                                                                                    , 37
                                                                                                                    , joinpath( project_path
                                                                                                                    , "src\\Main.purs" )
                                                                                                                    , 10000 ) ) ) ) )
                                                                                  , define( None
                                                                                          , [ "ps_$__unused" ]
                                                                                          , block( ret( call( call( get_item( var( "ps_SmallPrelude" )
                                                                                                                            , "discard" )
                                                                                                                  , call( get_item( var( "ps_SmallPrelude" )
                                                                                                                                  , "println" )
                                                                                                                        , call( var( "ps_testDeconsGuard" )
                                                                                                                              , var( "ps__3" ) ) ) )
                                                                                                            , define( None
                                                                                                                    , [ "ps_$__unused" ]
                                                                                                                    , block( ret( call( get_item( var( "ps_SmallPrelude" )
                                                                                                                                                , "println" )
                                                                                                                                      , call( var( "ps_testDeconsGuard" )
                                                                                                                                            , get_attr( var( "ps_Zero" )
                                                                                                                                                      , "value" ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) ) )
           , assign( "exports"
                   , record( ("Zero", var("ps_Zero"))
                           , ("Succ", var("ps_Succ"))
                           , ("natToInt", var("ps_natToInt"))
                           , ("natToIntRecImpl", var("ps_natToIntRecImpl"))
                           , ("natToIntRec", var("ps_natToIntRec"))
                           , ("intToNatRecImpl", var("ps_intToNatRecImpl"))
                           , ("intToNatRec", var("ps_intToNatRec"))
                           , ("_3", var("ps__3"))
                           , ("testDeconsGuard", var("ps_testDeconsGuard"))
                           , ("main", var("ps_main")) ) ) )
res = module_code(res, filename=__file__, name="pattern_matching.Main")
