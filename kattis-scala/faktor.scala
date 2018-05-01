import scala.math.ceil

object Main {

  def factor(a: Int, i: Int): Int = {
    @annotation.tailrec
    def loop(answer: Int): Int = {
      if(ceil(answer.toDouble / a.toDouble).toInt >= i) answer
      else loop(answer + 1)

    }
    loop(0)
  }

  def main(args: Array[String]): Unit = {
    val data = io.StdIn.readLine.split(' ').map(_.toInt)
    println(factor(data(0), data(1)))
  }

}
