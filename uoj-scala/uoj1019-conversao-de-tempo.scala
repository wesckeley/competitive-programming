object Main {
  def main(args: Array[String]) {
    var n = io.StdIn.readInt

    var H = n / 3600
    n %= 3600

    var M = n / 60
    n %= 60

    printf("%d:%d:%d\n", H, M, n)
  }
}
