import scala.math.pow

object Main {
  def main(args: Array[String]) {
    val Radius = io.StdIn.readDouble
    val Pi = 3.14159
    val Volume = (4.0 / 3) * Pi * pow(Radius, 3)
    printf("VOLUME = %.3f\n", Volume)
  }
}
