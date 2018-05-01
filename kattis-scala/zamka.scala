object Main {

  def digitSum(number: Int): Int = {
    @annotation.tailrec
    def loop(n: Int, acc: Int): Int = {
      if(n == 0) acc
      else loop(n / 10, acc + (n % 10))
    }
    loop(number, 0)
  }

  def zamka(start: Int, x: Int, inc: Int): Int = {
    @annotation.tailrec
    def loop(n: Int): Int = {
      if(digitSum(n) == x) n
      else loop(n + inc)
    }
    loop(start)
  }

  def main(args: Array[String]): Unit = {
    val l = io.StdIn.readInt
    val d = io.StdIn.readInt
    val x = io.StdIn.readInt
    println(zamka(l, x, 1))
    println(zamka(d, x, -1))
  }
}
