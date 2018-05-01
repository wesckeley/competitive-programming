object Main {

  def trik(data: String): Int = {
    @annotation.tailrec
    def loop(index: Int, state: Tuple3[Boolean, Boolean, Boolean]): Tuple3[Boolean, Boolean, Boolean] = {
      if(index == data.length) state
      else {
        data(index) match {
          case 'A' => loop(index + 1, Tuple3(state._2, state._1, state._3))
          case 'B' => loop(index + 1, Tuple3(state._1, state._3, state._2))
          case 'C' => loop(index + 1, Tuple3(state._3, state._2, state._1))
        }
      }
    }
    loop(0, Tuple3(true, false, false)) match {
      case (true, false, false) => 1
      case (false, true, false) => 2
      case (false, false, true) => 3
      case _ => -1
    }
  }

  def main(args: Array[String]): Unit = {
    val data = io.StdIn.readLine
    println(trik(data))
  }
  
}
