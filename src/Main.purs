module Main where

import SmallPrelude

data Nat
  = Zero       -- 0
  | Succ Nat   -- succ 0 -> 1; succ 2 -> 3

natToInt :: Nat -> Int
-- showNat _3 == "3"
-- showNat Zero == 0
natToInt Zero = 0
natToInt (Succ a) = 1 `iadd` natToInt a

natToIntRecImpl :: Int -> Nat -> Int
-- showNat _3 == "3"
-- showNat Zero == 0
natToIntRecImpl a Zero = a
natToIntRecImpl r (Succ a) = natToIntRecImpl (1 `iadd` r) a

natToIntRec = natToIntRecImpl 0

intToNatRecImpl :: Nat -> Int -> Nat
intToNatRecImpl a 0 = a
intToNatRecImpl a n = intToNatRecImpl (Succ a) (n `iadd` -1)

intToNatRec n
  | n `igt` 0        = error ""
  | true             = intToNatRecImpl Zero n

_3 = Succ (Succ (Succ Zero))

-- test deconstructions in guards
testDeconsGuard n
  | Succ a <- n = false
  | true = true

main :: IO {}
main = do
  println (natToInt _3)
  println (natToIntRec _3)
  println (natToIntRec (intToNatRec 10000))
  println (testDeconsGuard _3)
  println (testDeconsGuard Zero)
