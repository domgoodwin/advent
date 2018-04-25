using System;
using System.Collections.Generic;
using System.Linq;

namespace day6dotnet
{
    class Day6
    {
        static void Main(string[] args)
        {
            string input = System.IO.File.ReadAllText("day6.txt");
            Console.WriteLine(input);

            List<int> blocks = input.Split('\t').Select(Int32.Parse).ToList();

            int count = 0;
            List<string> oldPatterns = new List<string>();
            string curPattern = String.Empty;
            while (!oldPatterns.Contains(curPattern))
            {
                if(curPattern != String.Empty) oldPatterns.Add(curPattern));
                Console.WriteLine(curPattern);
                count++;
                // Get maximum item
                int maxIndex = blocks.IndexOf(blocks.Max());
                int maxValue = blocks.Max();
                // Redistribute
                int curI = maxIndex < blocks.Count() ? maxIndex + 1 : 0;
                int iValue = maxValue % blocks.Count;
                //blocks.Select((x, i) => i == maxIndex ? iValue : i + increment);
                while (maxValue > 0)
                {
                    curI = curI < blocks.Count() - 1 ? curI + 1 : 0;
                    blocks[curI] += 1;
                    maxValue -= 1;
                }
                curPattern = string.Join(",", blocks.ToArray());
                Console.WriteLine(curPattern);

            }
            Console.WriteLine(String.Format("[PART1] : Count {0}", count));
            Console.Read();
        }
    }
}
