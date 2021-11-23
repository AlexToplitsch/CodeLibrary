using System;

namespace SingletonÜbung
{
    class Program
    {
        static void Main(string[] args)
        {
            Singleton singletonObj1 = Singleton.GetSingleton("1");
            var singletonObj2 = Singleton.GetSingleton("2");

            Console.WriteLine(singletonObj1.Name);
            Console.WriteLine(singletonObj2.Name);

            Console.WriteLine(singletonObj1.Value);
            Console.WriteLine(singletonObj2.Value);

            Console.WriteLine(singletonObj1.IncreaseVal());

            Console.WriteLine(singletonObj1.Value);
            Console.WriteLine(singletonObj2.Value);
        }
    }
}
