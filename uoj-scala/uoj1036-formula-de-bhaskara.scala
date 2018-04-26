import scala.math.sqrt

object Main {

  def getDelta: (Double, Double, Double) => Double =
    (a, b, c) => (b * b) - (4 * a * c)

  def isReal(a: Double, delta: Double): Boolean = {
    if(a == 0) false
    else {
      if(delta >= 0) true
      else false
    }
  }

  def getRootMinus: (Double, Double, Double, Double) => Double =
    (a, b, c, delta) => ((-b) - sqrt(delta)) / (2 * a)

  def getRootPlus: (Double, Double, Double, Double) => Double =
    (a, b, c, delta) => ((-b) + sqrt(delta)) / (2 * a)

  def main(args: Array[String]): Unit = {
    val InData = io.StdIn.readLine.split(' ').map(_.toDouble)

    val Delta = getDelta(InData(0), InData(1), InData(2))

    if(isReal(InData(0), Delta) == false) println("Impossivel calcular")
    else {
      val r2 = getRootMinus(InData(0), InData(1), InData(2), Delta)
      val r1 = getRootPlus(InData(0), InData(1), InData(2), Delta)
      printf("R1 = %.5f\nR2 = %.5f\n", r1, r2)
    }
  }
}
