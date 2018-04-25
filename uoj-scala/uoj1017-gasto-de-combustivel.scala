object Main {
  def main(args: Array[String]) {
    val Time = io.StdIn.readDouble
    val Speed = io.StdIn.readDouble
    printf("%.3f\n", Time * Speed / 12.0)
  }
}
