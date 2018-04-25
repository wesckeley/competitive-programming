import scala.math.sqrt

object Main {

  def euclideanDistance(x1: Double, x2: Double, y1: Double, y2: Double): Double = {

    val dx = x2 - x1
    val dy = y2 - y1
    sqrt(dx * dx + dy * dy)

  }

  def main(args: Array[String]){

    val First = io.StdIn.readLine.split(' ').map(_.toDouble)
    val Second = io.StdIn.readLine.split(' ').map(_.toDouble)
    
    printf("%.4f\n", euclideanDistance(First(0), Second(0), First(1), Second(1)))

  }

}
