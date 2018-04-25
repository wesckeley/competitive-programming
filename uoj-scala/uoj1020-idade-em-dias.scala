object Main {
  def main(args: Array[String]) {
    var n = io.StdIn.readInt

    println(n / 365 + " ano(s)")
    n %= 365

    println(n / 30 + " mes(es)")
    n %= 30

    println(n + " dia(s)")
  }
}
