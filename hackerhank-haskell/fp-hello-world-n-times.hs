import Control.Monad

main = do
  n_temp <- getLine
  let n = read n_temp :: Int
  replicateM_ n $ putStrLn "Hello World"
