object Main {

  def speedlimit(n: Int): Int = {
    @annotation.tailrec
    def loop(i: Int, acc: Int, time: Int): Int = {
      if(i == n) acc
      else {
        val data = io.StdIn.readLine.split(' ').map(_.toInt)
        loop(i + 1, acc + (data(0) * (data(1) - time)), data(1))
      }
    }
    loop(0, 0, 0)
  }

  def main(args: Array[String]): Unit = {
    @annotation.tailrec
    def loop(n: Int): Unit = {
      if(n != -1) {
        println(speedlimit(n) + " miles")
        loop(io.StdIn.readInt)
      }
    }
    loop(io.StdIn.readInt)
  }

}
