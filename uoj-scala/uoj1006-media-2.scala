object Main {
  def main(args: Array[String]) : Unit = {
    val A = io.StdIn.readDouble()
    val B = io.StdIn.readDouble()
    val C = io.StdIn.readDouble()
    printf("MEDIA = %.1f", ((A * 2) + (B * 3) + (C * 5)) / 10)
  }
}
