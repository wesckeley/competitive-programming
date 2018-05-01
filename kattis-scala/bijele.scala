object Main {

  def main(args: Array[String]): Unit = {
    val dataE = Array[Int](1, 1, 2, 2, 2, 8)
    val dataR = io.StdIn.readLine.split(' ').map(_.toInt)

    @annotation.tailrec
    def loop(index: Int): Unit = {
      if(index == 5) printf("%d\n", dataE(index) - dataR(index))
      else {
        printf("%d ", dataE(index) - dataR(index))
        loop(index + 1)
      }
    }
    loop(0)
  }
}
