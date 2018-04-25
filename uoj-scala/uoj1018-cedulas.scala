object Main {
  def main(args: Array[String]) {

    val Notes = Array(100, 50, 20, 10, 5, 2, 1)
    var x = io.StdIn.readInt

    println(x)

    for(i <- 0 to 6){

      printf("%d nota(s) de R$ %d,00\n", x / Notes(i), Notes(i))
      x %= Notes(i)

    }
  }
}
