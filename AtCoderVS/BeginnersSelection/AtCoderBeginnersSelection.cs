using System;
using System.Linq;

namespace AtCoderVS
{
    class AtCoderBeginnersSelection
    {
        public static void ABC086A()
        {
            string[] input_line = Console.ReadLine().Split();
            int a = int.Parse(input_line[0]);
            int b = int.Parse(input_line[1]);

            if ((a * b % 2) == 0)
            {
                Console.WriteLine("Even");
            }
            else
            {
                Console.WriteLine("Odd");
            }
        }

        public static void ABC081A()
        {
            string input_line = Console.ReadLine();
            input_line = input_line.Replace("0", "");
            Console.WriteLine(input_line.Length);
        }

        public static void ABC081B()
        {
            int cnt = 0;
            int N = int.Parse(Console.ReadLine());
            int[] A = Console.ReadLine().Split().Select(x => int.Parse(x)).ToArray();

            while (A.All(x => x % 2 == 0))
            {
                A = A.Select(x => x / 2).ToArray();
                cnt++;
            }

            Console.WriteLine(cnt);
        }
    }
}