import scala.io.Source

@main def main: Unit = 
  val path = "/Users/ds/Code/advent-of-code-2021/day1/scala/aoc-day1/src/input.txt"
  val lines = Source.fromFile(path).getLines.toList
  val depths = lines.map(_.toString().toInt)
  val res = solution(depths)
  println(res)

def solution(depths: List[Int]): Int = 
  var res = 0
  var prev = depths.head
  for (d <- depths) {
    if (prev < d) {
      res += 1 
    }
    prev = d
  }
  return res

