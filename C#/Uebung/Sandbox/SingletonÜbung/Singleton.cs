namespace SingletonÜbung
{
    public class Singleton
    {
        public string Name { get; set; }
        private static Singleton MySingleton = null;
        public int Value { get; set; } = 0;
        private Singleton(string name)
        {
            Name = name;
        }

        public static Singleton GetSingleton(string name)
        {
            if (MySingleton == null)
            {
                System.Console.WriteLine("Create Singleton");
                MySingleton = new Singleton("My Singlton");
            }

            return MySingleton;
        }

        public int IncreaseVal()
        {
            return Value += 2;
        }
    }
}