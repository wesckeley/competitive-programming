object Main {

  def getInterval(X: Double): String = {
    if(X < 0) "Fora de intervalo"
    else {
      if(X <= 25) "Intervalo [0,25]"
      else {
        if(X <= 50) "Intervalo (25,50]"
        else {
          if(X <= 75) "Intervalo (50,75]"
          else {
            if(X <= 100) "Intervalo (75,100]"
            else "Fora de intervalo"
          }
        }
      }
    }
  }

  def main(args: Array[String]): Unit = {
    val X = io.StdIn.readDouble
    println(getInterval(X))
  }

}
