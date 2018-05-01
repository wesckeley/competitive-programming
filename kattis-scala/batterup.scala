object Main {
  def main(args: Array[String]): Unit = {
    val n = io.StdIn.readInt
    val data = io.StdIn.readLine.split(' ').map(_.toInt)

    @annotation.tailrec
    def loop(acc1: Int, acc2: Int, index: Int): Double = {
      if(index == data.length) acc2.toDouble / acc1.toDouble
      else {
        if(data(index) != -1) loop(acc1 + 1, acc2 + data(index), index + 1)
        else loop(acc1, acc2, index + 1)
      }
    }
    println(loop(0, 0, 0))
  }
}
