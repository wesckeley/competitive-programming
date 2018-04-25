object Main {
  def main(args: Array[String]) {
    val Number = io.StdIn.readInt()
    val Hours = io.StdIn.readInt()
    val Value = io.StdIn.readDouble()
    println("NUMBER = " + Number)
    printf("SALARY = U$ %.2f\n", Hours * Value)
  }
}
