object Main {
  def main(args: Array[String]) {
    val Name = io.StdIn.readLine()
    val Salary = io.StdIn.readDouble()
    val Sells = io.StdIn.readDouble()
    printf("TOTAL = R$ %.2f\n", Salary + (Sells * 0.15))
  }
}
