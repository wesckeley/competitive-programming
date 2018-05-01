object Main {
  def main(args: Array[String]): Unit = {
    val n = io.StdIn.readInt
    if((n & 0x01) == 0x01) println("Alice")
    else println("Bob")
  }
}
