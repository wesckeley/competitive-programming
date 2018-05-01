object Main {

  def cold(data: Array[Int]): Int = {
    @annotation.tailrec
    def loop(index: Int, acc: Int): Int = {
      if(index >= data.length) acc
      else {
        if(data(index) < 0) loop(index + 1, acc + 1)
        else loop(index + 1, acc)
      }
    }
    loop(0, 0)
  }

  def main(args: Array[String]): Unit = {
    val n = io.StdIn.readInt
    val data = io.StdIn.readLine.split(' ').map(_.toInt)
    println(cold(data))
  }

}
