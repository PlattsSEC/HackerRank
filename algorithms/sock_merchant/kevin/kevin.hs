{- Haskell Implementation -}
{- Kevin Boyette -}

{- This is an attempt at the sock merchant problem
    - https://www.hackerrank.com/challenges/sock-merchant/problem

    This attempt passed all the tests on Hackerrank.
    Inputs:
        Int
        [Int]
    Output:
        IO()
    Example:
        ./kevin
        9
        10 20 20 10 10 30 50 10 20
        3
-}
import Data.List

main :: IO ()
main = do
  {- Provided By HackerRank -}
  n_temp <- getLine
  let n = read n_temp :: Int
  ar_temp <- getLine
  let ar = map read $ words ar_temp :: [Int]
  {- Here is where the magic starts -}
  let result = sockMerchant (sort ar)
  print result

{- Provided By HackerRank -}
getMultipleLines :: Int -> IO [String]
getMultipleLines n
  | n <= 0 = return []
  | otherwise = do
    x <- getLine
    xs <- getMultipleLines (n - 1)
    let ret = x : xs
    return ret

{- Sock Merchant Attempt -}
sockMerchant :: [Int] -> Int
sockMerchant [] = 0
sockMerchant [x] = 0
sockMerchant (x:xs)
  | x == head xs = 1 + sockMerchant (tail xs)
  | otherwise = sockMerchant xs
