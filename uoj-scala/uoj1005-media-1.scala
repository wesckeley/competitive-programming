object Main {
  def main(args: Array[String]) {
    val A = io.StdIn.readDouble()
    val B = io.StdIn.readDouble()
    printf("MEDIA = %.5f\n", ((A * 3.5) + (B * 7.5)) / 11)
  }
}
