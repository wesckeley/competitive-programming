object Main {

  def main(args: Array[String]): Unit = {
    val r2: (Int, Int) => Int = (r1, s) => 2*s - r1
    val data = io.StdIn.readLine.split(' ').map(_.toInt)
    
    println(r2(data(0), data(1)))
  }

}
