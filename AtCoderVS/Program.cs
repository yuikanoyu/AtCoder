using System;

namespace AtCoderVS
{
    class MainClass
    {
        public static void Main(string[] args)
        {
            string[] input_line = Console.ReadLine().Split();
            int a = int.Parse(input_line[0]);
            int b = int.Parse(input_line[1]);

            if ((a * b % 2) == 0 ){
                Console.WriteLine("Even");
            }
            else
            {
                Console.WriteLine("Odd");
            }
        }
    }
}
