object Main {
  def main(args: Array[String]){
    val First = io.StdIn.readLine().split(' ').map(_.toDouble)
    val Second = io.StdIn.readLine().split(' ').map(_.toDouble)
    printf("VALOR A PAGAR: R$ %.2f\n", First(1) * First(2) + Second(1) * Second(2))
  }
}
