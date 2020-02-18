module SmallPrelude where

data IO a

foreign import println :: forall a. a -> IO {}
foreign import discard :: forall a b. IO a -> (a -> IO b) -> IO b
foreign import iadd :: Int -> Int -> Int
foreign import negate :: Int -> Int
foreign import error :: String -> forall a. a
foreign import igt :: Int -> Int -> Boolean
