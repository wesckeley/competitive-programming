object Main {

  def gt(data1: Array[Int], data2: Array[Int]): Boolean = {
    @annotation.tailrec
    def go(index: Int): Boolean = {
      if(index == data1.length) true
      else {
          if(data1(index) > data2(index)) go(index + 1)
          else false
      }
    }
    go(0)
  }

  def answer(b: Boolean): String = {
    if(b == true) "Valores aceitos"
    else "Valores nao aceitos"
  }

  def main(args: Array[String]): Unit = {
    val data = io.StdIn.readLine.split(' ').map(_.toInt)

    val data1 = Array(data(1), data(3), data(2) + data(3), data(2), data(3), (data(0) + 1) % 2)
    val data2 = Array(data(2), data(0), data(0) + data(1), 0, 0, 0)

    println(answer(gt(data1, data2)))

  }
}
