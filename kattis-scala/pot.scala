object Main {

  def pow(base: Int, exponent: Int): Int = {

    @annotation.tailrec
    def loop(b: Int, e: Int, acc: Int): Int = {
      if(e == 0) acc
      else {
        if((e & 0x01) == 0x01) loop(b * b, e / 2, b * acc)
        else loop(b * b, e / 2, acc)
      }
    }

    loop(base, exponent, 1)
  }

  def main(args: Array[String]): Unit = {
    val n = io.StdIn.readInt

    @annotation.tailrec
    def loop(acc: Int, n: Int): Int = {
      if(n == 0) acc
      else {
        val x = io.StdIn.readInt
        loop(acc + pow(x / 10, x % 10), n - 1)
      }
    }

    println(loop(0, n))
  }

}
