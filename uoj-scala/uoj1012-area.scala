object Main {
  def main(args: Array[String]) {
    val Data = io.StdIn.readLine.split(' ').map(_.toDouble)

    val Triangle = (Data(0) * Data(2)) / 2.0
    val Pi = 3.14159
    val Circle = Pi * Data(2) * Data(2)
    val Trapezoid = ((Data(0) + Data(1)) / 2.0) * Data(2)
    val Square = Data(1) * Data(1)
    val Rectangle = Data(0) * Data(1)

    printf("TRIANGULO: %.3f\n", Triangle)
    printf("CIRCULO: %.3f\n", Circle)
    printf("TRAPEZIO: %.3f\n", Trapezoid)
    printf("QUADRADO: %.3f\n", Square)
    printf("RETANGULO: %.3f\n", Rectangle)
  }
}
