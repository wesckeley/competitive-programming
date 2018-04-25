object Main {
  def main(args: Array[String]) {
    val X = io.StdIn.readInt
    val Y = io.StdIn.readDouble
    printf("%.3f km/l\n", X / Y)
  }
}
