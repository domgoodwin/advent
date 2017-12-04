import scala.io.Source

object Main extends App {
  println("Hello, World dom!")
  val filename = "day4.txt";

  val validPhrases1 = Source.fromFile(filename).getLines.map(l => if(l.split(" ").toSet.size == l.split(" ").size){ l } else { null});
  val count1 = validPhrases1.count(x => x != null);
  println(s"[PART1] Count of valid phrases: $count1");

  val validPhrases2 = Source.fromFile(filename).getLines
    .map(l => if(l.split(" ").map(p => p.sorted).toSet.size == l.split(" ").map(p => p.sorted).size) { l } else { null} );
  val count2 = validPhrases2.count(x => x != null);
  println(s"[PART2] Count of valid phrases: $count2");


}
