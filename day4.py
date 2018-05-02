

  val validPhrases1 = Source.fromFile(filename).getLines.map(l => if(l.split(" ").toSet.size == l.split(" ").size){ l } else { null});
  val count1 = validPhrases1.count(x => x != null);
  println(s"[PART1] Count of valid phrases: $count1");