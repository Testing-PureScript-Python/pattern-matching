"use strict";
var SmallPrelude = require("../SmallPrelude/index.js");
var Zero = (function () {
    function Zero() {

    };
    Zero.value = new Zero();
    return Zero;
})();
var Succ = (function () {
    function Succ(value0) {
        this.value0 = value0;
    };
    Succ.create = function (value0) {
        return new Succ(value0);
    };
    return Succ;
})();
var testDeconsGuard = function (n) {
    var v = function (v1) {
        return true;
    };
    if (n instanceof Succ) {
        return false;
    };
    return v(true);
};
var natToIntRecImpl = function ($copy_v) {
    return function ($copy_v1) {
        var $tco_var_v = $copy_v;
        var $tco_done = false;
        var $tco_result;
        function $tco_loop(v, v1) {
            if (v1 instanceof Zero) {
                $tco_done = true;
                return v;
            };
            if (v1 instanceof Succ) {
                $tco_var_v = SmallPrelude.iadd(1)(v);
                $copy_v1 = v1.value0;
                return;
            };
            throw new Error("Failed pattern match at Main (line 15, column 1 - line 15, column 37): " + [ v.constructor.name, v1.constructor.name ]);
        };
        while (!$tco_done) {
            $tco_result = $tco_loop($tco_var_v, $copy_v1);
        };
        return $tco_result;
    };
};
var natToIntRec = natToIntRecImpl(0);
var natToInt = function (v) {
    if (v instanceof Zero) {
        return 0;
    };
    if (v instanceof Succ) {
        return SmallPrelude.iadd(1)(natToInt(v.value0));
    };
    throw new Error("Failed pattern match at Main (line 9, column 1 - line 9, column 23): " + [ v.constructor.name ]);
};
var intToNatRecImpl = function ($copy_a) {
    return function ($copy_v) {
        var $tco_var_a = $copy_a;
        var $tco_done = false;
        var $tco_result;
        function $tco_loop(a, v) {
            if (v === 0) {
                $tco_done = true;
                return a;
            };
            $tco_var_a = new Succ(a);
            $copy_v = SmallPrelude.iadd(v)(SmallPrelude.negate(1));
            return;
        };
        while (!$tco_done) {
            $tco_result = $tco_loop($tco_var_a, $copy_v);
        };
        return $tco_result;
    };
};
var intToNatRec = function (n) {
    if (SmallPrelude.igt(n)(0)) {
        return SmallPrelude.error("");
    };
    return intToNatRecImpl(Zero.value)(n);
};
var _3 = new Succ(new Succ(new Succ(Zero.value)));
var main = SmallPrelude.discard(SmallPrelude.println(natToInt(_3)))(function () {
    return SmallPrelude.discard(SmallPrelude.println(natToIntRec(_3)))(function () {
        return SmallPrelude.discard(SmallPrelude.println(natToIntRec(intToNatRec(10000))))(function () {
            return SmallPrelude.discard(SmallPrelude.println(testDeconsGuard(_3)))(function () {
                return SmallPrelude.println(testDeconsGuard(Zero.value));
            });
        });
    });
});
module.exports = {
    Zero: Zero,
    Succ: Succ,
    natToInt: natToInt,
    natToIntRecImpl: natToIntRecImpl,
    natToIntRec: natToIntRec,
    intToNatRecImpl: intToNatRecImpl,
    intToNatRec: intToNatRec,
    "_3": _3,
    testDeconsGuard: testDeconsGuard,
    main: main
};
