object Main {
  def main(args: Array[String]) {
    val Data = io.StdIn.readLine.split(' ').map(_.toInt)
    println(Data.max + " eh o maior")
  }
}
