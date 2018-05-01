object Main {

  def planina(n: Int): Int = {
    @annotation.tailrec
    def loop(sqrt: Int, pow: Int, index: Int): Int = {
      if(index == n) sqrt * sqrt
      else loop(sqrt + pow, pow * 2, index + 1)
    }
    loop(2, 1, 0)
  }

  def main(args: Array[String]): Unit = {
    println(planina(io.StdIn.readInt))
  }

}
