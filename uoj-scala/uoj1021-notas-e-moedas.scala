object Main {
  def main(args: Array[String]) {

    val Notes = Array(10000, 5000, 2000, 1000, 500, 200, 100, 50, 25, 10, 5 , 1)

    val N = (io.StdIn.readDouble) * 100
    var x = N.toInt

    println("NOTAS:")
    for(i <- 0 to 5){
      printf("%d nota(s) de R$ %.2f\n", x / Notes(i), Notes(i) / 100.0)
      x %= Notes(i)
    }

    println("MOEDAS:")
    for(i <- 6 to 11){
      printf("%d moeda(s) de R$ %.2f\n", x / Notes(i), Notes(i) / 100.0)
      x %= Notes(i)
    }
  }
}
